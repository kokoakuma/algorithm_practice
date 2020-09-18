class Node:
  def __init__(self, key):
    self.key = key
    # self.parent_key = -1
    self.left_key = -1
    self.right_key = -1

nodes = {}
root = Node(-1)

# 先行順巡回
def preOrder(key):
  if key == -1:
    return
  current_node = nodes[key]
  print(f" {current_node.key}", end='')
  preOrder(current_node.left_key)
  preOrder(current_node.right_key)

# 中間順巡回
def inOrder(key):
  if key == -1:
    return
  current_node = nodes[key]
  inOrder(current_node.left_key)
  print(f" {current_node.key}", end='')
  inOrder(current_node.right_key)

# キー挿入
def insert(z):
  global nodes
  global root
  y = Node(-1)
  x = root
  while x.key != -1:
    y = x
    if z.key < x.key and x.left_key != -1:
      x = nodes[x.left_key]
    elif x.key <= z.key and x.right_key != -1:
      x = nodes[x.right_key]
    else:
      break
  # nodes[z.key].parent_key = y.key
  if y.key == -1:
    root = z
  elif z.key < y.key:
    nodes[y.key].left_key = z.key
  else:
    nodes[y.key].right_key = z.key

V = int(input())

# ノード情報取得
for i in range(V):
  order = list(input().split())
  if order[0] == 'print':
    inOrder(root.key)
    print('')
    preOrder(root.key)
    print('')
  else:
    k = int(order[1])
    new_Node = Node(k)
    nodes[k] = new_Node
    insert(new_Node)


##################################

class Node:
  def __init__(self, key):
    self.key = key
    self.left_key = -1
    self.right_key = -1

nodes = []
root = -1

# 先行順巡回
def preOrder(key):
  if key == -1:
    return
  current_node = nodes[key]
  print(f" {current_node.key}", end='')
  preOrder(current_node.left_key)
  preOrder(current_node.right_key)

# 中間順巡回
def inOrder(key):
  if key == -1:
    return
  current_node = nodes[key]
  inOrder(current_node.left_key)
  print(f" {current_node.key}", end='')
  inOrder(current_node.right_key)

# キー挿入
def insert(z):
  global nodes
  global root
  index = len(nodes)
  nodes.append(z)
  y = -1
  x = root
  while x != -1:
    y = x
    if z.key < nodes[x].key and nodes[x].left_key != -1:
      x = nodes[x].left_key
    elif nodes[x].key <= z.key and nodes[x].right_key != -1:
      x = nodes[x].right_key
    else:
      break
  if y == -1:
    root = index
  elif z.key < nodes[y].key:
    nodes[y].left_key = index
  else:
    nodes[y].right_key = index

V = int(input())

# ノード情報取得
for i in range(V):
  order = list(input().split())
  if order[0] == 'print':
    inOrder(root)
    print('')
    preOrder(root)
    print('')
  else:
    k = int(order[1])
    new_Node = Node(k)
    insert(new_Node)