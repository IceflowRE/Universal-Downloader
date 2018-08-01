# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unidown/plugin/protobuf/save_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from unidown.plugin.protobuf import plugin_info_pb2 as unidown_dot_plugin_dot_protobuf_dot_plugin__info__pb2
from unidown.plugin.protobuf import link_item_pb2 as unidown_dot_plugin_dot_protobuf_dot_link__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='unidown/plugin/protobuf/save_state.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(unidown/plugin/protobuf/save_state.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a)unidown/plugin/protobuf/plugin_info.proto\x1a\'unidown/plugin/protobuf/link_item.proto\"\xdf\x01\n\x0eSaveStateProto\x12\x0f\n\x07version\x18\x01 \x01(\t\x12/\n\x0blast_update\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x0bplugin_info\x18\x03 \x01(\x0b\x32\x10.PluginInfoProto\x12\'\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x19.SaveStateProto.DataEntry\x1a;\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.LinkItemProto:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,unidown_dot_plugin_dot_protobuf_dot_plugin__info__pb2.DESCRIPTOR,unidown_dot_plugin_dot_protobuf_dot_link__item__pb2.DESCRIPTOR,])




_SAVESTATEPROTO_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='SaveStateProto.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SaveStateProto.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='SaveStateProto.DataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=385,
)

_SAVESTATEPROTO = _descriptor.Descriptor(
  name='SaveStateProto',
  full_name='SaveStateProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='SaveStateProto.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_update', full_name='SaveStateProto.last_update', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plugin_info', full_name='SaveStateProto.plugin_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='SaveStateProto.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SAVESTATEPROTO_DATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=385,
)

_SAVESTATEPROTO_DATAENTRY.fields_by_name['value'].message_type = unidown_dot_plugin_dot_protobuf_dot_link__item__pb2._LINKITEMPROTO
_SAVESTATEPROTO_DATAENTRY.containing_type = _SAVESTATEPROTO
_SAVESTATEPROTO.fields_by_name['last_update'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SAVESTATEPROTO.fields_by_name['plugin_info'].message_type = unidown_dot_plugin_dot_protobuf_dot_plugin__info__pb2._PLUGININFOPROTO
_SAVESTATEPROTO.fields_by_name['data'].message_type = _SAVESTATEPROTO_DATAENTRY
DESCRIPTOR.message_types_by_name['SaveStateProto'] = _SAVESTATEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SaveStateProto = _reflection.GeneratedProtocolMessageType('SaveStateProto', (_message.Message,), dict(

  DataEntry = _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), dict(
    DESCRIPTOR = _SAVESTATEPROTO_DATAENTRY,
    __module__ = 'unidown.plugin.protobuf.save_state_pb2'
    # @@protoc_insertion_point(class_scope:SaveStateProto.DataEntry)
    ))
  ,
  DESCRIPTOR = _SAVESTATEPROTO,
  __module__ = 'unidown.plugin.protobuf.save_state_pb2'
  # @@protoc_insertion_point(class_scope:SaveStateProto)
  ))
_sym_db.RegisterMessage(SaveStateProto)
_sym_db.RegisterMessage(SaveStateProto.DataEntry)


_SAVESTATEPROTO_DATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
