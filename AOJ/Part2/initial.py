# 為替の最大利益
maxv = -float('inf') # 入力値に対して余裕のある値を使用する
N = int(input())
R_list = [int(input()) for _ in range(N)] # Nの回数だけ入力を受け取る
minv = R_list[0]
for j in range(1, N):
    if R_list[j] - minv > maxv:
        maxv = R_list[j] - minv
    if minv > R_list[j]:
        minv = R_list[j] # 最小値を保存する

print(str(maxv))