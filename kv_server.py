import kv_pb2
import kv_store

class Server(kv_pb2.BetaKVServicer):
  def __init__(self):
    self.store = kv_store.KVStore()
    kv_pb2.BetaKVServicer.__init__(self)

  def Get(self, request, context):
    print("[kv-server] get %s" % request.key)
    value = self.store.get(request.key)

    return kv_pb2.GetResponse(value=value)

  def Set(self, request, context):
    print("[kv-server] set %s=%s" % (request.key, request.value))
    self.store.set(request.key, request.value)

    return kv_pb2.SetResponse(ok=True)
