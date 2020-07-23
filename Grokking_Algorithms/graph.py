from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = [] # チェックリスト

  while search_queue:
    person = search_queue.popleft() # 先頭から一つ取り出す
    if not person in searched:
      if person_is_seller(person):
        print(f"{person} is a mango seller! I can start my business!")
        return True
      else:
        search_queue += graph[person] # 隣接ノードをキューに入れる
        searched.append(person) # チェックリストに名前を追加する

  return False

def person_is_seller(name):
  if 'nn' in name:
    return True
  else:
    return False

