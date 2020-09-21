class Node:
  def __init__(self, key):
    self.key = key
    self.parent_key = -float('inf')
    self.left_key = -float('inf')
    self.right_key = -float('inf')

nodes = {}
root = Node(-float('inf'))

# 先行順巡回
def preOrder(key):
  if key == -float('inf'):
    return
  current_node = nodes[key]
  print(f" {current_node.key}", end='')
  preOrder(current_node.left_key)
  preOrder(current_node.right_key)

# 中間順巡回
def inOrder(key):
  if key == -float('inf'):
    return
  current_node = nodes[key]
  inOrder(current_node.left_key)
  print(f" {current_node.key}", end='')
  inOrder(current_node.right_key)

# キー挿入
def insert(z):
  global nodes
  global root
  y = Node(-float('inf'))
  x = root
  while x.key != -float('inf'):
    y = x
    if z.key < x.key and x.left_key != -float('inf'):
      x = nodes[x.left_key]
    elif x.key <= z.key and x.right_key != -float('inf'):
      x = nodes[x.right_key]
    else:
      break
  nodes[z.key].parent_key = y.key
  if y.key == -float('inf'):
    root = z
  elif z.key < y.key:
    nodes[y.key].left_key = z.key
  else:
    nodes[y.key].right_key = z.key

def find_key(z):
  global nodes
  global root
  x = root
  while x.key != -float('inf') and z != x.key:
    if z < x.key and x.left_key != -float('inf'):
      x = nodes[x.left_key]
    elif x.key <= z and x.right_key != -float('inf'):
      x = nodes[x.right_key]
    else:
      break
  if z == x.key:
    return True
  else:
    return False

def delete_key(z):
  global nodes
  global root
  x = root
  while x.key != -float('inf') and z != x.key:
    if z < x.key and x.left_key != -float('inf'):
      x = nodes[x.left_key]
    elif x.key <= z and x.right_key != -float('inf'):
      x = nodes[x.right_key]
    else:
      break
    # TODO 削除する子にさらに子がいる場合の整理
  if z == x.key:
    parent = x.parent_key
    if nodes[parent].left_key == x.key:
      nodes[parent].left_key = -float('inf')
    else:
      nodes[parent].right_key = -float('inf')
    nodes.pop(x.key)
  else:
    return
V = int(input())

# ノード情報取得
for i in range(V):
  order = list(input().split())
  if order[0] == 'print':
    inOrder(root.key)
    print('')
    preOrder(root.key)
    print('')
  elif order[0] == 'find':
    flag = find_key(int(order[1]))
    if flag:
      print('yes')
    else:
      print('no')
  elif order[0] == 'delete':
    delete_key(int(order[1]))
  else:
    k = int(order[1])
    new_Node = Node(k)
    nodes[k] = new_Node
    insert(new_Node)

