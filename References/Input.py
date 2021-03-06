### 1文字
s = input()
s = int(input()) # 数字

### １つの文字列を分割してリストに入れる
a = list(input())

### １行に複数 ex) aa bb cc
a,b,c = input().split()
a,b,c = map(int, input().split())

### １行に複数入力があり、リストに格納する ex) aa bb cc
a_list = list(input().split())
a_list = list(map(int, input().split()))

### n行に1文字ずつ入力
# ex)
# 3
# 100
# 250
# 300
N = int(input())  # nは入力回数 "_"はこの変数を使用しない合図
str_list = [input() for _ in range(N)]

N = int(input())  # nは入力回数
int_list = [int(input()) for _ in range(N)]

### n行に複数入力 二次元配列に格納する
# ex)
# 3
# 100 200 300
# 250 300 450
# 300 444 555
N = int(input())  # nは入力回数
str_list = [list(input().split()) for _ in range(N)]

N = int(input())  # nは入力回数
imt_list = [list(map(int, input().split())) for _ in range(N)]


# 高速？
# １行
from sys import stdin
a = stdin.readline().rstrip()
# 複数行を全て読み込む
a = stdin.read()

### 番外編
# 入力値に対して余裕のある値を使用する
maxv = -float('inf') # 負の無限大
minv = float('inf') # 正の無限大



### ソート & 並び替え
a.sort()
a.sort(reverse=True)
a = sorted(a)
a = sorted(a, reverse=True)

a.reverse()
reversed(a)

### 文字列の並び替え
list(a)
reversed(a)
''.join(a)
# or
a[::-1] # :: →最初から最後まで、-1 →ステップがマイナス方向に1ずつ

### 小数点の計算
from decimal import Decimal
A = Decimal('1.111')

### ラムダ式とmap
# map内でint str以上の複雑な処理をしたい時に式を簡単に書ける
sy, sx = map(lambda x: int(x)-1, input().split())
