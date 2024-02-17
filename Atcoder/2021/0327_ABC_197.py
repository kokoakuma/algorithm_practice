#A
a, b, c = list(map(int, input().split()))

a, b, c = list(input())
ans = b + c + a
print(ans)



#B
h, w, x, y = list(map(int, input().split()))
table = []
for _ in range(h):
  table.append(list(input()))

ans = 0
left = True
right = True
top = True
bottom = True
if table[x-1][y-1] == '#':
  print(ans)
else:
  # top
  ans += 1
  pointx = x - 1
  while top and pointx > 0:
    pointx -= 1
    if table[pointx][y-1] == '.':
      ans += 1
    else:
      top = False
  # bottom
  pointx = x - 1
  while bottom and pointx < h - 1:
    pointx += 1
    if table[pointx][y-1] == '.':
      ans += 1
    else:
      bottom = False
  # left
  pointy = y - 1
  while left and pointy > 0:
    pointy -= 1
    if table[x-1][pointy] == '.':
      ans += 1
    else:
      left = False
  # right
  pointy = y - 1
  while right and pointy < w - 1:
    pointy += 1
    if table[x-1][pointy] == '.':
      ans += 1
    else:
      right = False
  
  print(ans)




#C

n = int(input())
nums = list(map(int, input().split()))
ans = float('inf')

for i in range(0, 2 ** n-1):
    slice_index = []
    sliced_nums = []
    or_nums = []
    xor_num = 0
    tmp_nums = nums
    for j in range(n-1):
        if (i >> j) & 1:
            slice_index.append(j+1)
    # 分けない場合
    if len(slice_index) == 0:
      or_num = 0
      for num in tmp_nums:
        or_num = or_num | num
      xor_num = or_num
    # 分ける場合
    else:
      for k in slice_index:
        sliced_nums.append(tmp_nums[:k])
        tmp_nums = tmp_nums[k:]
      sliced_nums.append(tmp_nums)
  
      for m1 in sliced_nums:
        or_num = 0
        for m2 in m1:
          or_num = or_num | m2
        or_nums.append(or_num)
    
      xor_num = or_nums[0]
      for o in or_nums[1:]:
        xor_num = xor_num ^ o
    
    if xor_num < ans:
      ans = xor_num
    
    if ans == 0:
      break

print(ans)



n = int(input())
nums = list(map(int, input().split()))
ans = float('inf')

for i in range(0, 2 ** n-1):
  _or = nums[0]
  _xor = []
  for j in range(n-1):
    if (i >> j) & 1:
      _xor.append(_or)
      _or = nums[j+1]
    else:
      _or |= nums[j+1]
  _xor.append(_or)

  res = 0
  for k in _xor:
    res ^= k
  
  ans = min(ans, res)

print(ans)