#A
"https://zenn.dev/magurofly/articles/188ce2e0215345"
N, M = list(map(int, input().split()))
ans = pow(10, N, M**2) // M
print(ans)
# ans = pow(10, N, M**2)
# M進数で考えた場合、
# 切り捨てて、Mで割った余り＝M進数の下から二桁目の数
# 三桁目以降は必要ない
# M**2の余り（下二桁）だけ見れば良い




