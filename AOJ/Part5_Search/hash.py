class Dictionary:
  def __init__(self):
    self.elements = set()
  def insert(self, x):
    self.elements.add(x)
  def find(self, y):
    if y in self.elements:
      print('yes')
    else:
      print('no')

dic = Dictionary()

N = int(input())
for i in range(N):
  command = input()
  if command[0] == 'i':
    dic.insert(command[7:])
  else:
    dic.find(command[5:])

######

class LinearMap(object):
  def __init__(self):
    self.items = []

  def add(self, key, value):
    self.items.append((key, value))

  def get(self, key):
    for k, v in self.items:
      if key  == k:
        return v
      print('key error')

  def __str__(self):
    return str(self.items)

####
class BetterMap(object):
  def __init__(self, n=100):
    self.maps = []
    for i in range(n):
      self.maps.append(LinearMap())
  
  def find_map(self, key):
    index = self.index(key)
    return self.maps[index]
  
  def index(self, key):
    return lash(key) % len(self.maps)

  def add(self, key, value):
    m = self.find_map(key)
    m.add((key, value))
  
  def get(self, key):
    m = self.find_map(key)
    return m.get(key)

  def __str__(self):
    return str(self.maps)

####
class HashMap(object):
  def __init__(self):
    self.maps = BetterMap(2)
    self.num = 0

  def get(self, key):
    return self.maps.get(key)
  
  def add(self, key, value):
    if self.num == len(self.maps.maps):
      self.resize()
    
    self.maps.add(key, value)
    self.num += 1
  
  def resize(self):
    new_maps = BetterMap(self.nums * 2)

    for m in self.maps.maps:
      for k, v in m.items:
        new_maps.add(k,v)
    
    self.maps = new_maps