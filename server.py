import kv_pb2, kv_pb2_grpc
import time
import kv_server
import grpc
from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_GRPC_HOST = "127.0.0.1:50051"

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  kv_pb2_grpc.add_KVServicer_to_server(kv_server.Server(), server)

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
