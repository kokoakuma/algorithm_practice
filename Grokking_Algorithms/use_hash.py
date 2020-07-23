voted = {}
def check_voter(name):
  if voted.get(name):
    print('Thank you. you have already voted')
  else:
    voted[name] = True
    print("Let's vote!")

###################################

import random

cache = { 'a': '11', 'b': '22', 'c': '33' }
def get_cache(key):
  if cache.get(key):
    print(cache[key])
  else:
    newData = random.random()
    cache[key] = f"{newData}"
    print(f"{newData} is added")

get_cache('a')
get_cache('b')
get_cache('c')
get_cache('d')
get_cache('d')