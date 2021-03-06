# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_example/proto/calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_example/proto/calculator.proto',
  package='calculator',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#grpc_example/proto/calculator.proto\x12\ncalculator\"\"\n\nSumRequest\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x05\"\x16\n\x05\x46loat\x12\r\n\x05value\x18\x01 \x01(\x02\x32\x87\x02\n\x11\x43\x61lculatorService\x12\x33\n\x03Sum\x12\x16.calculator.SumRequest\x1a\x12.calculator.Number\"\x00\x12\x42\n\x14PrimeNumberGenerator\x12\x12.calculator.Number\x1a\x12.calculator.Number\"\x00\x30\x01\x12<\n\x0f\x43omputerAverage\x12\x12.calculator.Number\x1a\x11.calculator.Float\"\x00(\x01\x12;\n\x0b\x46indMaximum\x12\x12.calculator.Number\x1a\x12.calculator.Number\"\x00(\x01\x30\x01\x62\x06proto3'
)




_SUMREQUEST = _descriptor.Descriptor(
  name='SumRequest',
  full_name='calculator.SumRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='calculator.SumRequest.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='calculator.SumRequest.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=51,
  serialized_end=85,
)


_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='calculator.Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='calculator.Number.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=87,
  serialized_end=110,
)


_FLOAT = _descriptor.Descriptor(
  name='Float',
  full_name='calculator.Float',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='calculator.Float.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=112,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['SumRequest'] = _SUMREQUEST
DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
DESCRIPTOR.message_types_by_name['Float'] = _FLOAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SumRequest = _reflection.GeneratedProtocolMessageType('SumRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUMREQUEST,
  '__module__' : 'grpc_example.proto.calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.SumRequest)
  })
_sym_db.RegisterMessage(SumRequest)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'grpc_example.proto.calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.Number)
  })
_sym_db.RegisterMessage(Number)

Float = _reflection.GeneratedProtocolMessageType('Float', (_message.Message,), {
  'DESCRIPTOR' : _FLOAT,
  '__module__' : 'grpc_example.proto.calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.Float)
  })
_sym_db.RegisterMessage(Float)



_CALCULATORSERVICE = _descriptor.ServiceDescriptor(
  name='CalculatorService',
  full_name='calculator.CalculatorService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=137,
  serialized_end=400,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sum',
    full_name='calculator.CalculatorService.Sum',
    index=0,
    containing_service=None,
    input_type=_SUMREQUEST,
    output_type=_NUMBER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PrimeNumberGenerator',
    full_name='calculator.CalculatorService.PrimeNumberGenerator',
    index=1,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ComputerAverage',
    full_name='calculator.CalculatorService.ComputerAverage',
    index=2,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_FLOAT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FindMaximum',
    full_name='calculator.CalculatorService.FindMaximum',
    index=3,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATORSERVICE)

DESCRIPTOR.services_by_name['CalculatorService'] = _CALCULATORSERVICE

# @@protoc_insertion_point(module_scope)
