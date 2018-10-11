import grpc

import sys
import kv_pb2, kv_pb2_grpc

_TIMEOUT_SECONDS = 10
_GRPC_HOST = "127.0.0.1:50051"
_USAGE = """
script/client usage:
  script/client set <key> <value> - sets the <key> and <value>
  script/client get <key>         - gets the value for <key>
  """

def run():
  if len(sys.argv) == 1:
    print(_USAGE)

    sys.exit(0)

  cmd = sys.argv[1]

  channel = grpc.insecure_channel(_GRPC_HOST)
  client_stub = kv_pb2_grpc.KVStub(channel)

  if cmd == "get":
    # ensure a key was provided
    if len(sys.argv) != 3:
      print(_USAGE)
      sys.exit(1)

    # get the key to fetch
    key = sys.argv[2]

    # create the request
    get_request = kv_pb2.GetRequest(key=key)

    # send the request to the server
    response = client_stub.Get(get_request, _TIMEOUT_SECONDS)

    print(response.value)
    sys.exit(0)

  elif cmd == "set":
    # ensure a key and value were provided
    if len(sys.argv) < 4:
      print(_USAGE)
      sys.exit(1)

    # get the key and the full text of value
    key = sys.argv[2]
    value = " ".join(sys.argv[3:])

    # create the request
    set_request = kv_pb2.SetRequest(key=key, value=value)

    # send the request to the server
    md = (('md-key', 'some value'),)
    response = client_stub.Set(set_request, _TIMEOUT_SECONDS, metadata=md)

    print("set %s to %s" % (key, value))

if __name__ == '__main__':
  run()
