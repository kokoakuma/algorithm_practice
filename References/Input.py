### 1文字
s = input()
s = int(input()) # 数字

### １つの文字列を分割してリストに入れる
a = list(input())
# ex
a.sort()
a.sort(reverse=True)
a = sorted(a)
a = sorted(a, reverse=True)

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
