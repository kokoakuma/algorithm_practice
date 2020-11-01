#A

N = int(input())

if N % 2 == 0:
  print('White')
else:
  print('Black')



#B
ans = 0
table = []
N = int(input())
for _ in range(N):
  nums = list(map(int, input().split()))
  table.append(nums)

for i in range(N):
  a,b = table[i]
  x = b - a + 1
  row_sum = (a + b) * x // 2
  ans += row_sum

print(int(ans))

#C

N = int(input())
table = []
ans = False

for _ in range(N):
  num = list(map(int, input().split()))
  table.append(num)

for first in range(N-2):
  for second in range(first+1, N-1):
    for third in range(second+1, N):
      if ans == True:
        continue
      f = table[first]
      s = table[second]
      t = table[third]
      fs_y = f[1] - s[1]
      fs_x = f[0] - s[0]
      st_y = s[1] - t[1]
      st_x = s[0] - t[0]
      if fs_y == 0 and st_y == 0:
        ans = True
      if fs_x == 0 and st_x == 0:
        ans = True
      if fs_y != 0 and st_y != 0 and fs_x != 0 and st_x != 0:
        fs = fs_y / fs_x
        st = st_y / st_x
        if fs == st:
          ans = True

if ans == True:
  print('Yes')
else:
  print('No')

#D


table = [0] * 10
ans = False
num_list = []

# 数字それぞれの個数をカウントする
N = list(input())
for num in N:
  table[int(num)] += 1

# 下三桁で計算するため、３つ以上ある場合は３個に減らす
for i in range(10):
  if table[i] > 3:
    table[i] = 3

# 数字のリストを作成する
for i in range(1, 10):
  for _ in range(table[i]):
    num_list.append(i)

num_len = len(num_list)

# 一桁の場合
if num_len == 1:
  if num_list[0] % 8 == 0:
    ans = True

# 二桁の場合ß
elif num_len == 2:
  a,b = list(map(str, num_list))
  ab = int(a + b)
  ba = int(b + a)
  if ab % 8 == 0 or ba % 8 == 0:
    ans = True

# 三桁以上の場合、全ての組み合わせを試す。 最大でも30個 * 30個 * 30個
else:
  for first in range(num_len-2):
    for second in range(first+1, num_len-1):
      for third in range(second+1, num_len):
        f = str(num_list[first])
        s = str(num_list[second])
        t = str(num_list[third])
        # 3つの数字の並べ方（６通り）を全て試す
        x1 = int(f + s + t)
        x2 = int(f + s + t)
        x3 = int(s + f + t)
        x4 = int(s + t + f)
        x5 = int(t + f + s)
        x6 = int(t + s + f)

        if x1 % 8 == 0 or x2 % 8 == 0 or x3 % 8 == 0 or x4 % 8 == 0 or x5 % 8 == 0 or x6 % 8 == 0:
          ans = True
          break

if ans == True:
  print('Yes')
else:
  print('No')