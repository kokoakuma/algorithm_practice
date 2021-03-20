#A
a, b, c = list(map(int, input().split()))
if a < b:
  print('Aoki')
elif b < a:
  print('Takahashi')
else:
  if c == 0:
    print('Aoki')
  else:
    print('Takahashi')




#B
n, s, d = list(map(int, input().split()))
ans = False

for i in range(n):
  x, y = list(map(int, input().split()))
  if x < s and y > d:
    ans = True

if ans:
  print('Yes')
else:
  print('No')




#C
ans = 0
n, m = list(map(int, input().split()))
conditions = []
for i in range(m):
  x, y = list(map(int, input().split()))
  conditions.append([x, y])

k = int(input())
choices = []
for i in range(k):
  x, y = list(map(int, input().split()))
  choices.append([x, y])

for i in range(2 ** k):
  tmp_ans = 0
  output_list = []
  ## どの桁が1になっているかをチェックするために2進数の各桁をループ
  for j in range(k):
    ## i >> jで確認したい桁を一番右までずらして1と論理積をとって「選択」している要素を確認
    if (i >> j) & 1:
      output_list.append(choices[j][0])
    else:
      output_list.append(choices[j][1])
  output_list = set(output_list)

  for c in conditions:
    if set(c) <= output_list:
      tmp_ans += 1
  if ans < tmp_ans:
    ans = tmp_ans

print(ans)

＃D
# 等差数列の総和 = (初項+末項) / 2 * 項数
# 末項 = 初項 + 項数 - 1
# 条件に適した初項と項数の組み合わせを求める
# 初項を求める 初項 = ((2 * 総和 / 項数) - 項数 + 1) / 2 初項が整数になるには前半が偶数になる必要あり①
# そのためには、2 * 総和 / 項数が整数 → 項数が (2 * 総和)の約数である必要あり
# ２ * 総和 の約数を計算する。その約数の中で①に当てはまるものを計算する
S = int(input())
def make_divisors(n):
  lower_divisors , upper_divisors = [], []
  i = 1
  while i*i <= n:
    if n % i == 0:
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]

div_list = make_divisors(2 * S)
ans = 0
for div in div_list:
  if ((2 * S / div) - div + 1) % 2 == 0:
    ans += 1

print(ans)