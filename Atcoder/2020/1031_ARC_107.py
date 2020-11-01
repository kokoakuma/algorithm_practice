#A
a,b,c = list(map(int, input().split()))

mod = 998244353
a_sum = (a * (a + 1)) // 2
b_sum = (b * (b + 1)) // 2
c_sum = (c * (c + 1)) // 2

ans = ( ( (a_sum * b_sum) % mod) * c_sum) % mod

print(int(ans))

#B
