import kv_pb2, kv_pb2_grpc
import kv_store
import grpc
import pprint

class Server(kv_pb2_grpc.KVServicer):
  def __init__(self):
    self.store = kv_store.KVStore()

  def Get(self, request, context):
    print("[kv-server] get %s" % request.key)
    value = self.store.get(request.key)

    return kv_pb2.GetResponse(value=value)

  def Set(self, request, context):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(context.invocation_metadata())
    print("[kv-server] set %s=%s" % (request.key, request.value))
    self.store.set(request.key, request.value)

    return kv_pb2.SetResponse(ok=True)
