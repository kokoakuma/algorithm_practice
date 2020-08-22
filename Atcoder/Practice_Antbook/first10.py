# ABC086 A
# 二つの正整数 a, b が与えられます。 a と b の積が偶数か奇数か判定してください。
# A B

a, b = map(int, input().split())
multi = a * b

if multi % 2 == 0:
  print('Even')
else:
  print('Odd')

# ABC082 A
# 2つの正整数a,bが与えられます。
# a,bの平均値をxとします。xの小数点以下を切り上げて得られる整数を出力してください。
import math
a, b = map(int, input().split())
multi = math.ceil((a + b) / 2)

print(str(multi))

# ABC081 A
# 0 と 1 のみから成る 3 桁の番号 s が与えられます。1 が何個含まれるかを求めてください。
# ex. '101'
a = input()

counter = 0
if a[0] == '1':
  counter += 1
if a[1] == '1':
  counter += 1
if a[2] == '1':
  counter += 1
print(str(counter))

# ABC082 B
# 英小文字のみからなる文字列 s, tが与えられます。
# あなたは、sの文字を好きな順に並べ替え、文字列 s′を作ります。
# また、tの文字を好きな順に並べ替え、文字列t′を作ります。
# このとき、辞書順でs′<t′となるようにできるか判定してください。
a = list(input())
b = list(input())
 
a.sort()
b.sort(reverse=True)
print(a)
if ''.join(a) < ''.join(b):
  print('Yes')
else:
  print('No')

# ABC081 B
# 黒板に NN 個の正の整数 A1,…,ANA1,…,AN が書かれています。
# すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます。
# 黒板に書かれている整数すべてを，22 で割ったものに置き換える。
# すぬけ君は最大で何回操作を行うことができるかを求めてください。
N = int(input())
A = list(map(int, input().split()))

counter = 0
while True:
  hasOdd = 0
  for i in range(N):
    if A[i] % 2 == 1:
      hasOdd += 1

  if hasOdd > 0:
    break

  A = [i / 2 for i in A]
  counter += 1
print(str(counter))

#ABC087 B
# 500 円玉を AA 枚、100 円玉を BB 枚、50 円玉を CC 枚持っています。
# これらの硬貨の中から何枚かを選び、合計金額をちょうど XX 円にする方法は
# 何通りあるでしょうか？


A = int(input())
B = int(input())
C = int(input())
X = int(input())

answer = 0
for i in range(A+1):
  for j in range(B+1):
    for k in range(C+1):
      total = 500 * i + 100 * j + 50 * k
      if total == X:
        answer += 1
print(str(answer))

# ARC004 A
# 平面上にN個の点があり、それぞれ0からN−1までの番号が付けられており、
# それぞれの点についてx座標とy座標が与えられています。
# そのN点のうち2点を選び結んで得られる線分のうち、最も長くなる線分の長さを求めてください。
import math
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

biggest_e = 0
for i in range(N):
  for j in range(i+1, N):
    E = math.sqrt((A[i][0] -  a[j][0])**2 + (A[i][1] - A[j][1])**2)
    if E > biggest_e:
      biggest_e = E
print(f"{biggest_e:.6f}")

# 4問目終了

# ABC083 B
# 1以上N以下の整数のうち、10進法での各桁の和が
# A以上B以下であるものの総和を求めてください。

N, A, B = list(map(int, input().split()))

r_sum = 0
for i in range(1, N+1):
  sum_digit = 0
  n_str = str(i)
  for j in range(len(n_str))
    sum_digit += int(n_str[j])
  if A <= sum_digit and sum_digit <= B:
    r_sum += sum_digit
print(str(r_sum))



# AABC088 B
# 【問題概要】NN 枚のカードがあり、ii 枚目のカードには aiai という数が書かれています。
#Alice と Bob はこれらのカードを使ってゲームを行います。
# ゲームでは 2 人が交互に 1 枚ずつカードを取っていきます。Alice が先にカードを取ります。
# 2人がすべてのカードを取ったときゲームは終了し、取ったカードの数の合計がその人の得点になります。2 人とも自分の得点を最大化するように最適戦略をとったとき、Alice は Bob より何点多くの得点を獲得できるかを求めてください。

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

Alice = 0
Bob = 0
for i in range(N):
  temp = A.pop(0)
  if i % 2 == 0:
    Alice += temp
  else:
    Bob += temp

print(str(Alice - Bob))

# AGC012 A
# AtCoder Group Contestの参加者に3N人が参加します。i番目の参加者の 強さ は整数aiで表されます。 
# 参加者が3人 1組となるようにチームをN組作ることにしました1人の参加者が複数のチームに所属することはできません。
# チームの強さはチームメンバーの強さのうち2番目に大きい値で表されます。 
# 例えば、強さが1,5,2のメンバーからなるチームの強さは2になり、強さが3,2,3のメンバーからなるチームの強さは3になります。
# N組のチームの強さの和としてありうる値のうち、最大の値を求めてください。

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

answer = 0
for i in (range(1, N+1)):
  answer += A[i*2 - 1]

print(str(answer))

# 1 2 3 4 5 6
# 1 3
# 2 4
# 5 6
# 2番目、4番目、六番目、、、、となっていく
# ソート後、N[i] * 2番目の数字をとっていけばOK

#ABC 085 B
# NN 個の整数 d[0],d[1],…,d[N−1]d[0],d[1],…,d[N−1] が与えられます。
# この中に何種類の異なる値があるでしょうか？

N = int(input())
A = [int(input()) for _ in range(N)]
A = set(A)
print(str(len(A)))

# ABC 071 B
# 英小文字からなる文字列Sが与えられます．Sに現れない英小文字であって，最も辞書順（アルファベット順）で小さいものを求めてください．
#  ただし，Sにすべての英小文字が現れる場合は，代わりに None を出力してください．

A = list(input())
A = set(A)

x = 0
for c in 'abcdefghijklmnopqrstuvwxyz':
  if c not in A:
    print(c)
    x = 1
    break
if x == 0:
  print('None')

# ABC061 B
# N個の都市があり、M本の道路があります。
# i(1≦i≦M)番目の道路は、都市aiと 都市bi (1≦ai, i≦N)を双方向に結んでいます。
# 同じ2つの都市を結ぶ道路は1本とは限りません各都市から他の都市に向けて、何本の道路が伸びているか求めてください。
N, M = list(map(int, input().split()))
A = [0 for _ in range(N)]

for i in range(M):
   a, b = list(map(int, input().split()))
   A[a-1] += 1
   A[b-1] += 1

for i in range(N):
  print(A[i])

#ABC085 C
# 日本でよく使われる紙幣は、10000円札、5000円札、1000円札です。
# 以下、「お札」とはこれらのみを指します。青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札がN枚入っていて、
# 合計でY円だったそうですが、嘘かもしれません。このような状況がありうるか判定し、
# ありうる場合はお年玉袋の中身の候補を一つ見つけてください。なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。

N, Y = list(map(int, input().split()))

r10000 = -1
r5000 = -1
r1000 = -1

for a in range(1,N+1):
  for b in range(1,N+1-a):
    c = N - a - b
    sum = 10000*a + 5000*b + 1000*c
    if sum == Y:
      r10000 = a
      r5000 = b
      r1000 = c

print(f"{r10000} {r5000} {r1000}")

