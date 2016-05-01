import kv_pb2
import time
import kv_store

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_GRPC_HOST = "[::]:50051"

class KVServer(kv_pb2.BetaKVServicer):
  def __init__(self):
    self.store = kv_store.KVStore()
    kv_pb2.BetaKVServicer.__init__(self)

  def Get(self, request, context):
    print("received: get %s" % request.key)
    value = self.store.get(request.key)

    return kv_pb2.GetResponse(value=value)

  def Set(self, request, context):
    print("received: set %s=%s" % (request.key, request.value))
    self.store.set(request.key, request.value)
    return kv_pb2.SetResponse(ok=True)


def serve():
  server = kv_pb2.beta_create_KV_server(KVServer())
  server.add_insecure_port(_GRPC_HOST)
  server.start()

  print "gRPC server started on %s" % _GRPC_HOST

  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)
  except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

if __name__ == '__main__':
  serve()
