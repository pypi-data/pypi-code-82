# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/MultiSelect.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/MultiSelect.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!streamlit/proto/MultiSelect.proto\"X\n\x0bMultiSelect\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x03(\x05\x12\x0f\n\x07options\x18\x04 \x03(\t\x12\x0c\n\x04help\x18\x05 \x01(\tb\x06proto3')
)




_MULTISELECT = _descriptor.Descriptor(
  name='MultiSelect',
  full_name='MultiSelect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MultiSelect.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='MultiSelect.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='MultiSelect.default', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='MultiSelect.options', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='help', full_name='MultiSelect.help', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=37,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['MultiSelect'] = _MULTISELECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MultiSelect = _reflection.GeneratedProtocolMessageType('MultiSelect', (_message.Message,), dict(
  DESCRIPTOR = _MULTISELECT,
  __module__ = 'streamlit.proto.MultiSelect_pb2'
  # @@protoc_insertion_point(class_scope:MultiSelect)
  ))
_sym_db.RegisterMessage(MultiSelect)


# @@protoc_insertion_point(module_scope)
