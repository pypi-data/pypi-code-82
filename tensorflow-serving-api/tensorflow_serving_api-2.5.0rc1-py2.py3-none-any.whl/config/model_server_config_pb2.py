# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/config/model_server_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from tensorflow_serving.config import file_system_storage_path_source_pb2 as tensorflow__serving_dot_config_dot_file__system__storage__path__source__pb2
from tensorflow_serving.config import logging_config_pb2 as tensorflow__serving_dot_config_dot_logging__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_serving/config/model_server_config.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\n3tensorflow_serving/config/model_server_config.proto\x12\x12tensorflow.serving\x1a\x19google/protobuf/any.proto\x1a?tensorflow_serving/config/file_system_storage_path_source.proto\x1a.tensorflow_serving/config/logging_config.proto\"\xb1\x03\n\x0bModelConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tbase_path\x18\x02 \x01(\t\x12\x35\n\nmodel_type\x18\x03 \x01(\x0e\x32\x1d.tensorflow.serving.ModelTypeB\x02\x18\x01\x12\x16\n\x0emodel_platform\x18\x04 \x01(\t\x12i\n\x14model_version_policy\x18\x07 \x01(\x0b\x32K.tensorflow.serving.FileSystemStoragePathSourceConfig.ServableVersionPolicy\x12J\n\x0eversion_labels\x18\x08 \x03(\x0b\x32\x32.tensorflow.serving.ModelConfig.VersionLabelsEntry\x12\x39\n\x0elogging_config\x18\x06 \x01(\x0b\x32!.tensorflow.serving.LoggingConfig\x1a\x34\n\x12VersionLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01J\x04\x08\x05\x10\x06J\x04\x08\t\x10\n\"B\n\x0fModelConfigList\x12/\n\x06\x63onfig\x18\x01 \x03(\x0b\x32\x1f.tensorflow.serving.ModelConfig\"\x94\x01\n\x11ModelServerConfig\x12@\n\x11model_config_list\x18\x01 \x01(\x0b\x32#.tensorflow.serving.ModelConfigListH\x00\x12\x33\n\x13\x63ustom_model_config\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06\x63onfig*N\n\tModelType\x12\x1e\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x1a\x02\x08\x01\x12\x12\n\nTENSORFLOW\x10\x01\x1a\x02\x08\x01\x12\r\n\x05OTHER\x10\x02\x1a\x02\x08\x01\x42\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,tensorflow__serving_dot_config_dot_file__system__storage__path__source__pb2.DESCRIPTOR,tensorflow__serving_dot_config_dot_logging__config__pb2.DESCRIPTOR,])

_MODELTYPE = _descriptor.EnumDescriptor(
  name='ModelType',
  full_name='tensorflow.serving.ModelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODEL_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=_b('\010\001'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TENSORFLOW', index=1, number=1,
      serialized_options=_b('\010\001'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=2, number=2,
      serialized_options=_b('\010\001'),
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=870,
  serialized_end=948,
)
_sym_db.RegisterEnumDescriptor(_MODELTYPE)

ModelType = enum_type_wrapper.EnumTypeWrapper(_MODELTYPE)
MODEL_TYPE_UNSPECIFIED = 0
TENSORFLOW = 1
OTHER = 2



_MODELCONFIG_VERSIONLABELSENTRY = _descriptor.Descriptor(
  name='VersionLabelsEntry',
  full_name='tensorflow.serving.ModelConfig.VersionLabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.serving.ModelConfig.VersionLabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.serving.ModelConfig.VersionLabelsEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=585,
  serialized_end=637,
)

_MODELCONFIG = _descriptor.Descriptor(
  name='ModelConfig',
  full_name='tensorflow.serving.ModelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.serving.ModelConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_path', full_name='tensorflow.serving.ModelConfig.base_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_type', full_name='tensorflow.serving.ModelConfig.model_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_platform', full_name='tensorflow.serving.ModelConfig.model_platform', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_version_policy', full_name='tensorflow.serving.ModelConfig.model_version_policy', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_labels', full_name='tensorflow.serving.ModelConfig.version_labels', index=5,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logging_config', full_name='tensorflow.serving.ModelConfig.logging_config', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MODELCONFIG_VERSIONLABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=649,
)


_MODELCONFIGLIST = _descriptor.Descriptor(
  name='ModelConfigList',
  full_name='tensorflow.serving.ModelConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='tensorflow.serving.ModelConfigList.config', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=651,
  serialized_end=717,
)


_MODELSERVERCONFIG = _descriptor.Descriptor(
  name='ModelServerConfig',
  full_name='tensorflow.serving.ModelServerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_config_list', full_name='tensorflow.serving.ModelServerConfig.model_config_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_model_config', full_name='tensorflow.serving.ModelServerConfig.custom_model_config', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='config', full_name='tensorflow.serving.ModelServerConfig.config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=720,
  serialized_end=868,
)

_MODELCONFIG_VERSIONLABELSENTRY.containing_type = _MODELCONFIG
_MODELCONFIG.fields_by_name['model_type'].enum_type = _MODELTYPE
_MODELCONFIG.fields_by_name['model_version_policy'].message_type = tensorflow__serving_dot_config_dot_file__system__storage__path__source__pb2._FILESYSTEMSTORAGEPATHSOURCECONFIG_SERVABLEVERSIONPOLICY
_MODELCONFIG.fields_by_name['version_labels'].message_type = _MODELCONFIG_VERSIONLABELSENTRY
_MODELCONFIG.fields_by_name['logging_config'].message_type = tensorflow__serving_dot_config_dot_logging__config__pb2._LOGGINGCONFIG
_MODELCONFIGLIST.fields_by_name['config'].message_type = _MODELCONFIG
_MODELSERVERCONFIG.fields_by_name['model_config_list'].message_type = _MODELCONFIGLIST
_MODELSERVERCONFIG.fields_by_name['custom_model_config'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MODELSERVERCONFIG.oneofs_by_name['config'].fields.append(
  _MODELSERVERCONFIG.fields_by_name['model_config_list'])
_MODELSERVERCONFIG.fields_by_name['model_config_list'].containing_oneof = _MODELSERVERCONFIG.oneofs_by_name['config']
_MODELSERVERCONFIG.oneofs_by_name['config'].fields.append(
  _MODELSERVERCONFIG.fields_by_name['custom_model_config'])
_MODELSERVERCONFIG.fields_by_name['custom_model_config'].containing_oneof = _MODELSERVERCONFIG.oneofs_by_name['config']
DESCRIPTOR.message_types_by_name['ModelConfig'] = _MODELCONFIG
DESCRIPTOR.message_types_by_name['ModelConfigList'] = _MODELCONFIGLIST
DESCRIPTOR.message_types_by_name['ModelServerConfig'] = _MODELSERVERCONFIG
DESCRIPTOR.enum_types_by_name['ModelType'] = _MODELTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelConfig = _reflection.GeneratedProtocolMessageType('ModelConfig', (_message.Message,), {

  'VersionLabelsEntry' : _reflection.GeneratedProtocolMessageType('VersionLabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _MODELCONFIG_VERSIONLABELSENTRY,
    '__module__' : 'tensorflow_serving.config.model_server_config_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.serving.ModelConfig.VersionLabelsEntry)
    })
  ,
  'DESCRIPTOR' : _MODELCONFIG,
  '__module__' : 'tensorflow_serving.config.model_server_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ModelConfig)
  })
_sym_db.RegisterMessage(ModelConfig)
_sym_db.RegisterMessage(ModelConfig.VersionLabelsEntry)

ModelConfigList = _reflection.GeneratedProtocolMessageType('ModelConfigList', (_message.Message,), {
  'DESCRIPTOR' : _MODELCONFIGLIST,
  '__module__' : 'tensorflow_serving.config.model_server_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ModelConfigList)
  })
_sym_db.RegisterMessage(ModelConfigList)

ModelServerConfig = _reflection.GeneratedProtocolMessageType('ModelServerConfig', (_message.Message,), {
  'DESCRIPTOR' : _MODELSERVERCONFIG,
  '__module__' : 'tensorflow_serving.config.model_server_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ModelServerConfig)
  })
_sym_db.RegisterMessage(ModelServerConfig)


DESCRIPTOR._options = None
_MODELTYPE.values_by_name["MODEL_TYPE_UNSPECIFIED"]._options = None
_MODELTYPE.values_by_name["TENSORFLOW"]._options = None
_MODELTYPE.values_by_name["OTHER"]._options = None
_MODELCONFIG_VERSIONLABELSENTRY._options = None
_MODELCONFIG.fields_by_name['model_type']._options = None
# @@protoc_insertion_point(module_scope)
