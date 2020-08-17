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