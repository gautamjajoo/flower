# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/driver.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import message_pb2 as flwr_dot_proto_dot_message__pb2
from flwr.proto import task_pb2 as flwr_dot_proto_dot_task__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2
from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x66lwr/proto/driver.proto\x12\nflwr.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x18\x66lwr/proto/message.proto\x1a\x15\x66lwr/proto/task.proto\x1a\x14\x66lwr/proto/run.proto\x1a\x14\x66lwr/proto/fab.proto\"!\n\x0fGetNodesRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\"3\n\x10GetNodesResponse\x12\x1f\n\x05nodes\x18\x01 \x03(\x0b\x32\x10.flwr.proto.Node\"@\n\x12PushTaskInsRequest\x12*\n\rtask_ins_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.TaskIns\"\'\n\x13PushTaskInsResponse\x12\x10\n\x08task_ids\x18\x02 \x03(\t\"F\n\x12PullTaskResRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x10\n\x08task_ids\x18\x02 \x03(\t\"A\n\x13PullTaskResResponse\x12*\n\rtask_res_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.TaskRes\",\n\x1aPullServerAppInputsRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\"\x7f\n\x1bPullServerAppInputsResponse\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.flwr.proto.Context\x12\x1c\n\x03run\x18\x02 \x01(\x0b\x32\x0f.flwr.proto.Run\x12\x1c\n\x03\x66\x61\x62\x18\x03 \x01(\x0b\x32\x0f.flwr.proto.Fab\"S\n\x1bPushServerAppOutputsRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.flwr.proto.Context\"\x1e\n\x1cPushServerAppOutputsResponse2\xfc\x05\n\x06\x44river\x12J\n\tCreateRun\x12\x1c.flwr.proto.CreateRunRequest\x1a\x1d.flwr.proto.CreateRunResponse\"\x00\x12G\n\x08GetNodes\x12\x1b.flwr.proto.GetNodesRequest\x1a\x1c.flwr.proto.GetNodesResponse\"\x00\x12P\n\x0bPushTaskIns\x12\x1e.flwr.proto.PushTaskInsRequest\x1a\x1f.flwr.proto.PushTaskInsResponse\"\x00\x12P\n\x0bPullTaskRes\x12\x1e.flwr.proto.PullTaskResRequest\x1a\x1f.flwr.proto.PullTaskResResponse\"\x00\x12\x41\n\x06GetRun\x12\x19.flwr.proto.GetRunRequest\x1a\x1a.flwr.proto.GetRunResponse\"\x00\x12\x41\n\x06GetFab\x12\x19.flwr.proto.GetFabRequest\x1a\x1a.flwr.proto.GetFabResponse\"\x00\x12h\n\x13PullServerAppInputs\x12&.flwr.proto.PullServerAppInputsRequest\x1a\'.flwr.proto.PullServerAppInputsResponse\"\x00\x12k\n\x14PushServerAppOutputs\x12\'.flwr.proto.PushServerAppOutputsRequest\x1a(.flwr.proto.PushServerAppOutputsResponse\"\x00\x12\\\n\x0fUpdateRunStatus\x12\".flwr.proto.UpdateRunStatusRequest\x1a#.flwr.proto.UpdateRunStatusResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.driver_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETNODESREQUEST']._serialized_start=155
  _globals['_GETNODESREQUEST']._serialized_end=188
  _globals['_GETNODESRESPONSE']._serialized_start=190
  _globals['_GETNODESRESPONSE']._serialized_end=241
  _globals['_PUSHTASKINSREQUEST']._serialized_start=243
  _globals['_PUSHTASKINSREQUEST']._serialized_end=307
  _globals['_PUSHTASKINSRESPONSE']._serialized_start=309
  _globals['_PUSHTASKINSRESPONSE']._serialized_end=348
  _globals['_PULLTASKRESREQUEST']._serialized_start=350
  _globals['_PULLTASKRESREQUEST']._serialized_end=420
  _globals['_PULLTASKRESRESPONSE']._serialized_start=422
  _globals['_PULLTASKRESRESPONSE']._serialized_end=487
  _globals['_PULLSERVERAPPINPUTSREQUEST']._serialized_start=489
  _globals['_PULLSERVERAPPINPUTSREQUEST']._serialized_end=533
  _globals['_PULLSERVERAPPINPUTSRESPONSE']._serialized_start=535
  _globals['_PULLSERVERAPPINPUTSRESPONSE']._serialized_end=662
  _globals['_PUSHSERVERAPPOUTPUTSREQUEST']._serialized_start=664
  _globals['_PUSHSERVERAPPOUTPUTSREQUEST']._serialized_end=747
  _globals['_PUSHSERVERAPPOUTPUTSRESPONSE']._serialized_start=749
  _globals['_PUSHSERVERAPPOUTPUTSRESPONSE']._serialized_end=779
  _globals['_DRIVER']._serialized_start=782
  _globals['_DRIVER']._serialized_end=1546
# @@protoc_insertion_point(module_scope)
