# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/NewReport.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import SessionState_pb2 as streamlit_dot_proto_dot_SessionState__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/NewReport.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fstreamlit/proto/NewReport.proto\x1a\"streamlit/proto/SessionState.proto\"\xcb\x01\n\tNewReport\x12\x1f\n\ninitialize\x18\x01 \x01(\x0b\x32\x0b.Initialize\x12\x11\n\treport_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0bscript_path\x18\x04 \x01(\t\x12$\n\rdeploy_params\x18\x05 \x01(\x0b\x32\r.DeployParams\x12\x17\n\x06\x63onfig\x18\x06 \x01(\x0b\x32\x07.Config\x12(\n\x0c\x63ustom_theme\x18\x07 \x01(\x0b\x32\x12.CustomThemeConfig\"\xa6\x01\n\nInitialize\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12*\n\x10\x65nvironment_info\x18\x03 \x01(\x0b\x32\x10.EnvironmentInfo\x12$\n\rsession_state\x18\x04 \x01(\x0b\x32\r.SessionState\x12\x14\n\x0c\x63ommand_line\x18\x05 \x01(\t\x12\x12\n\nsession_id\x18\x06 \x01(\t\"\x8e\x01\n\x06\x43onfig\x12\x17\n\x0fsharing_enabled\x18\x01 \x01(\x08\x12\x1a\n\x12gather_usage_stats\x18\x02 \x01(\x08\x12\x1e\n\x16max_cached_message_age\x18\x03 \x01(\x05\x12\x14\n\x0cmapbox_token\x18\x04 \x01(\t\x12\x19\n\x11\x61llow_run_on_save\x18\x05 \x01(\x08\"\xe1\x01\n\x11\x43ustomThemeConfig\x12\x15\n\rprimary_color\x18\x01 \x01(\t\x12\"\n\x1asecondary_background_color\x18\x02 \x01(\t\x12\x18\n\x10\x62\x61\x63kground_color\x18\x03 \x01(\t\x12\x12\n\ntext_color\x18\x04 \x01(\t\x12+\n\x04\x66ont\x18\x05 \x01(\x0e\x32\x1d.CustomThemeConfig.FontFamily\"6\n\nFontFamily\x12\x0e\n\nSANS_SERIF\x10\x00\x12\t\n\x05SERIF\x10\x01\x12\r\n\tMONOSPACE\x10\x02\"\x86\x01\n\x08UserInfo\x12\x17\n\x0finstallation_id\x18\x01 \x01(\t\x12\x1a\n\x12installation_id_v1\x18\x03 \x01(\t\x12\x1a\n\x12installation_id_v2\x18\x04 \x01(\t\x12\x1a\n\x12installation_id_v3\x18\x05 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"D\n\x0f\x45nvironmentInfo\x12\x19\n\x11streamlit_version\x18\x01 \x01(\t\x12\x16\n\x0epython_version\x18\x02 \x01(\t\"B\n\x0c\x44\x65ployParams\x12\x12\n\nrepository\x18\x01 \x01(\t\x12\x0e\n\x06\x62ranch\x18\x02 \x01(\t\x12\x0e\n\x06module\x18\x03 \x01(\tb\x06proto3')
  ,
  dependencies=[streamlit_dot_proto_dot_SessionState__pb2.DESCRIPTOR,])



_CUSTOMTHEMECONFIG_FONTFAMILY = _descriptor.EnumDescriptor(
  name='FontFamily',
  full_name='CustomThemeConfig.FontFamily',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SANS_SERIF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERIF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONOSPACE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=763,
  serialized_end=817,
)
_sym_db.RegisterEnumDescriptor(_CUSTOMTHEMECONFIG_FONTFAMILY)


_NEWREPORT = _descriptor.Descriptor(
  name='NewReport',
  full_name='NewReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initialize', full_name='NewReport.initialize', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='report_id', full_name='NewReport.report_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='NewReport.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script_path', full_name='NewReport.script_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deploy_params', full_name='NewReport.deploy_params', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='NewReport.config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_theme', full_name='NewReport.custom_theme', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=72,
  serialized_end=275,
)


_INITIALIZE = _descriptor.Descriptor(
  name='Initialize',
  full_name='Initialize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='Initialize.user_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environment_info', full_name='Initialize.environment_info', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_state', full_name='Initialize.session_state', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command_line', full_name='Initialize.command_line', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='Initialize.session_id', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=278,
  serialized_end=444,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sharing_enabled', full_name='Config.sharing_enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gather_usage_stats', full_name='Config.gather_usage_stats', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_cached_message_age', full_name='Config.max_cached_message_age', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapbox_token', full_name='Config.mapbox_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_run_on_save', full_name='Config.allow_run_on_save', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=447,
  serialized_end=589,
)


_CUSTOMTHEMECONFIG = _descriptor.Descriptor(
  name='CustomThemeConfig',
  full_name='CustomThemeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='primary_color', full_name='CustomThemeConfig.primary_color', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_background_color', full_name='CustomThemeConfig.secondary_background_color', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background_color', full_name='CustomThemeConfig.background_color', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_color', full_name='CustomThemeConfig.text_color', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='font', full_name='CustomThemeConfig.font', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CUSTOMTHEMECONFIG_FONTFAMILY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=817,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='installation_id', full_name='UserInfo.installation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installation_id_v1', full_name='UserInfo.installation_id_v1', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installation_id_v2', full_name='UserInfo.installation_id_v2', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installation_id_v3', full_name='UserInfo.installation_id_v3', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='UserInfo.email', index=4,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=820,
  serialized_end=954,
)


_ENVIRONMENTINFO = _descriptor.Descriptor(
  name='EnvironmentInfo',
  full_name='EnvironmentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='streamlit_version', full_name='EnvironmentInfo.streamlit_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='python_version', full_name='EnvironmentInfo.python_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=956,
  serialized_end=1024,
)


_DEPLOYPARAMS = _descriptor.Descriptor(
  name='DeployParams',
  full_name='DeployParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='DeployParams.repository', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='branch', full_name='DeployParams.branch', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module', full_name='DeployParams.module', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1026,
  serialized_end=1092,
)

_NEWREPORT.fields_by_name['initialize'].message_type = _INITIALIZE
_NEWREPORT.fields_by_name['deploy_params'].message_type = _DEPLOYPARAMS
_NEWREPORT.fields_by_name['config'].message_type = _CONFIG
_NEWREPORT.fields_by_name['custom_theme'].message_type = _CUSTOMTHEMECONFIG
_INITIALIZE.fields_by_name['user_info'].message_type = _USERINFO
_INITIALIZE.fields_by_name['environment_info'].message_type = _ENVIRONMENTINFO
_INITIALIZE.fields_by_name['session_state'].message_type = streamlit_dot_proto_dot_SessionState__pb2._SESSIONSTATE
_CUSTOMTHEMECONFIG.fields_by_name['font'].enum_type = _CUSTOMTHEMECONFIG_FONTFAMILY
_CUSTOMTHEMECONFIG_FONTFAMILY.containing_type = _CUSTOMTHEMECONFIG
DESCRIPTOR.message_types_by_name['NewReport'] = _NEWREPORT
DESCRIPTOR.message_types_by_name['Initialize'] = _INITIALIZE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['CustomThemeConfig'] = _CUSTOMTHEMECONFIG
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['EnvironmentInfo'] = _ENVIRONMENTINFO
DESCRIPTOR.message_types_by_name['DeployParams'] = _DEPLOYPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NewReport = _reflection.GeneratedProtocolMessageType('NewReport', (_message.Message,), dict(
  DESCRIPTOR = _NEWREPORT,
  __module__ = 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:NewReport)
  ))
_sym_db.RegisterMessage(NewReport)

Initialize = _reflection.GeneratedProtocolMessageType('Initialize', (_message.Message,), dict(
  DESCRIPTOR = _INITIALIZE,
  __module__ = 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:Initialize)
  ))
_sym_db.RegisterMessage(Initialize)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  ))
_sym_db.RegisterMessage(Config)

CustomThemeConfig = _reflection.GeneratedProtocolMessageType('CustomThemeConfig', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMTHEMECONFIG,
  __module__ = 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:CustomThemeConfig)
  ))
_sym_db.RegisterMessage(CustomThemeConfig)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)

EnvironmentInfo = _reflection.GeneratedProtocolMessageType('EnvironmentInfo', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENTINFO,
  __module__ = 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:EnvironmentInfo)
  ))
_sym_db.RegisterMessage(EnvironmentInfo)

DeployParams = _reflection.GeneratedProtocolMessageType('DeployParams', (_message.Message,), dict(
  DESCRIPTOR = _DEPLOYPARAMS,
  __module__ = 'streamlit.proto.NewReport_pb2'
  # @@protoc_insertion_point(class_scope:DeployParams)
  ))
_sym_db.RegisterMessage(DeployParams)


# @@protoc_insertion_point(module_scope)
