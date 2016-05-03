class KVStore():

  def __init__(self):
    self.store = {}

  def get(self, key):
    return self.store.get(key, key + " not found")

  def set(self, key, value):
    self.store[key] = value
