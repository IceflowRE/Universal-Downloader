"""
Manager of the whole program, contains the most important functions as well as the download routine.
"""
import logging
import multiprocessing
import platform
from typing import List

from unidown import static_data
from unidown.core import updater
from unidown.core.plugin_state import PluginState
from unidown.plugin.a_plugin import APlugin
from unidown.plugin.exceptions import PluginException
from unidown.plugin.link_item_dict import LinkItemDict
from core.settings import Settings


def init_logging(settings: Settings):
    """
    Initialize the _downloader.

    :param settings: settings
    """
    logging.basicConfig(filename=str(settings.log_file), filemode='a', level=settings.log_level,
                        format='%(asctime)s.%(msecs)03d | %(levelname)s - %(name)s | %(module)s.%(funcName)s: %('
                               'message)s', datefmt='%Y.%m.%d %H:%M:%S')
    logging.captureWarnings(True)

    info = f"{static_data.NAME} {static_data.VERSION}\n\n" \
           f"System: {platform.system()} - {platform.version()} - {platform.machine()} - {multiprocessing.cpu_count()} cores\n" \
           f"Python: {platform.python_version()} - {' - '.join(platform.python_build())}\n" \
           f"Arguments: main={settings.root_dir.resolve()} | logfile={settings.log_file} | loglevel={settings.log_level}\n" \
           f"Using cores: {settings.cores}\n\n"

    settings.log_file.parent.mkdir(parents=True, exist_ok=True)
    with settings.log_file.open(mode='w', encoding="utf8") as writer:
        writer.write(info)


def shutdown():
    """
    Close and exit important things.
    """
    logging.shutdown()


def download_from_plugin(plugin: APlugin):
    """
    Download routine.

    1. get newest update time
    2. load savestate
    3. compare last update time with savestate time
    4. get download links
    5. compare with savestate
    6. download new/updated data
    7. check downloads
    8. update savestate
    9. write new savestate

    :param plugin: plugin
    """
    # get last update date
    plugin.log.info('Get last update')
    plugin.update_last_update()
    # load old save state
    plugin.load_savestate()
    if plugin.last_update <= plugin.savestate.last_update:
        plugin.log.info('No update. Nothing to do.')
        return
    # get download links
    plugin.log.info('Get download links')
    plugin.update_download_links()
    # compare with save state
    new_items = LinkItemDict.get_new_items(plugin.savestate.link_items, plugin.download_data)
    plugin.log.info('Compared with save state: ' + str(len(plugin.download_data)))
    if not new_items:
        plugin.log.info('No new data. Nothing to do.')
        return
    # download new/updated data
    plugin.log.info(f"Download new {plugin.unit}s: {len(new_items)}")
    plugin.download(new_items, plugin.download_path, 'Download new ' + plugin.unit + 's', plugin.unit)
    # check which downloads are succeeded
    succeeded, lost = plugin.check_download(new_items, plugin.download_path)
    plugin.log.info(f"Downloaded: {len(succeeded)}/{len(new_items)}")
    # update savestate link_item_dict with succeeded downloads dict
    plugin.log.info('Update savestate')
    plugin.update_savestate(succeeded)
    # write new savestate
    plugin.log.info('Write savestate')
    plugin.save_savestate()


def run(settings: Settings, plugin_name: str, options: List[str]) -> PluginState:
    """
    Run a plugin so use the download routine and clean up after.

    :param settings: settings to use
    :param plugin_name: name of plugin
    :param options: parameters which will be send to the plugin initialization
    :return: success
    """
    if options is None:
        options = []

    available_plugins = APlugin.get_plugins()
    if plugin_name not in available_plugins:
        msg = 'Plugin ' + plugin_name + ' was not found.'
        logging.error(msg)
        return PluginState.NotFound

    try:
        plugin_class = available_plugins[plugin_name].load()
        plugin = plugin_class(settings, options)
    except Exception as ex:
        msg = 'Plugin ' + plugin_name + ' crashed while loading.'
        logging.exception(msg, ex)
        print(msg + ' Check log for more information.')
        return PluginState.LoadCrash
    else:
        logging.info('Loaded plugin: ' + plugin_name)

    try:
        download_from_plugin(plugin)
        plugin.clean_up()
    except PluginException as ex:
        msg = f"Plugin {plugin.name} stopped working. Reason: {'unknown' if (ex.msg == '') else ex.msg}"
        logging.error(msg)
        print(msg)
        return PluginState.RunFail
    except Exception as ex:
        msg = 'Plugin ' + plugin.name + ' crashed.'
        logging.exception(msg, ex)
        print(msg + ' Check log for more information.')
        return PluginState.RunCrash
    else:
        logging.info(plugin.name + ' ends without errors.')
        return PluginState.EndSuccess


def check_update():
    """
    Check for app updates and print/log them.
    """
    logging.info('Check for app updates.')
    try:
        update = updater.check_for_app_updates()
    except Exception:
        logging.exception('Check for updates failed.')
        return
    if update:
        print("!!! UPDATE AVAILABLE !!!\n"
              "" + static_data.PROJECT_URL + "\n\n")
        logging.info("Update available: " + static_data.PROJECT_URL)
    else:
        logging.info("No update available.")
