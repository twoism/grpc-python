import kv_pb2
import time
import kv_server

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_GRPC_HOST = "127.0.0.1:50051"

def serve():
  server = kv_pb2.beta_create_KV_server(kv_server.Server())
  server.add_insecure_port(_GRPC_HOST)
  server.start()
  print("[kv-server] started on %s" % _GRPC_HOST)

  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)
  except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

if __name__ == '__main__':
  serve()
