from collections import deque
# 両端しか操作しない場合はdequeが高速
# 途中の値も操作するならリストの方が高速

# queue
q = deque()
q.append('a')
q.popleft()

# stack
stk = deque()
stk.appendleft('a')
stk.popleft()

# deque 両端キュー
deq = deque()
deq.append('a')
deq.appendleft('a')
deq.pop()
deq.popleft()

# マッチする要素の個数確認
q.count('a')

# 要素の削除
q.clear()

# 挿入
q.insert(index, x)

# 最初にマッチした値を削除する
q.remove('a')
