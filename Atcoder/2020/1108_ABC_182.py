#A
a, b = list(map(int, input().split()))
total = a * 2 + 100
remain = total - b
print(int(remain))


#B
table = [0] * 1001
n = int(input())
nums = list(map(int, input().split()))

for i in range(2, 1001):
  for num in nums:
    if num % i == 0:
      table[i] += 1

ans = table.index(max(table))

print(str(ans))


#C
a = int(input())
n = len(str(a))
a_list = list(str(a))
a_list = list(map(int, a_list))
ans = -1

if n == 1:
  if a % 3 == 0:
    print("0")
  else:
    print('-1')

else:
  for i in range(1, 2 ** n): # 1から順に試す
    out_list = []
    ## どの桁が1になっているかをチェックするために2進数の各桁をループ
    for j in range(n):
        ## i >> jで確認したい桁を一番右までずらして1と論理積をとって「選択」している要素を確認
        if (i >> j) & 1:
            out_list.append(a_list[j])
    num_digit_to_use = len(out_list) # 何桁使用するか
    total = sum(out_list) # 桁それぞれの合計値
    if total % 3 == 0:
      if ans == -1:
        ans = n - num_digit_to_use
      else:
        ans = min(ans, (n - num_digit_to_use))

  print(str(ans))


#D
import numpy as np
n = int(input())
a = list(map(int, input().split()))
cumsum_a = np.cumsum(a) # 累積和

end_table = [None] * n
max_table = [None] * n

end_table[0] = a[0]
for i in range(1, n):
  end_table[i] = cumsum_a[i] + cumsum_a[i]

max_cumsum_a[0] = cumsum_a[0]
for i in range(1, n):
  max_num = 0
  num = a[i]
  max_cumsum_a[i] = max(max_cumsum_a[i-1], max_cumsum_a[i-1] + num))

table = [None] * n
table[0] = a[0]
for i in range(1, n):
  table[i] = max_cumsum_a[i] + cumsum_a[i]

ans = max(table)
print(ans)

#D 
N = int(input())
tmp_str = input().split()
A = [int(i) for i in tmp_str]
now = 0
max_ans = 0
moved = 0
max_move = 0
 
for i in range(N):
    moved += A[i]
    if max_move < moved:
        max_move = moved
    if max_ans < now + max_move:
        max_ans = now + max_move
    now = now + moved
 
print(max_ans)

n = int(input())
a = list(map(int, input().split()))

now = 0
nax_ans = 0
moved = 0
max_move = 0

for i in range(n):
  moved += a[i]
  if max_move < moved:
    max_move = moved
  if max_ans < now + max_move:
    max_ans = now + max_move
  now += moved

print(nax_ans)

