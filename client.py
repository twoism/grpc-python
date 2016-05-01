from __future__ import print_function

from grpc.beta import implementations

import sys
import kv_pb2

_TIMEOUT_SECONDS = 10
_GRPC_PORT = 4222
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

  channel = implementations.insecure_channel('localhost', 50051)
  client_stub = kv_pb2.beta_create_KV_stub(channel)

  if cmd == "get":
    # ensure a key was provided
    if len(sys.argv) != 3:
      print(_USAGE)
      sys.exit(1)

    key = sys.argv[2]

    # create the request
    get_request = kv_pb2.GetRequest(key=key)

    # send the request to the server
    response = client_stub.Get(get_request, _TIMEOUT_SECONDS)

    print(response.value)
    sys.exit(0)

  elif cmd == "set":
    # ensure a key and value were provided
    if len(sys.argv) != 5:
      print(_USAGE)
      sys.exit(1)

    key = sys.argv[2]
    value = " ".join(sys.argv[3:])

    # create the request
    set_request = kv_pb2.SetRequest(key=key, value=value)

    # send the request to the server
    response = client_stub.Set(set_request, _TIMEOUT_SECONDS)

    print("set %s to %s" % (key, value))


if __name__ == '__main__':
  run()
