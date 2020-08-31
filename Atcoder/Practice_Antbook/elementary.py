# ABC051 B
# 2つの整数K,Sが与えられます。3つの変数X,Y,Zがあり、
# 0≦X,Y,Z≦Kを満たす整数の値を取ります。X+Y+Z=Sを満たすX,Y,Zへの値の割り当ては何通りありますか。

K, S = list(map(int, input().split()))

answer = 0
for i in range(K+1):
  for j in range(K+1):
    if 0 <= S - (i + j) <= K:
      answer += 1

print(answer)


#ABC045 C
A = input()
a_len = len(A)

answer = 0
for i in range(2**(a_len-1)):
  a_tmp = A
  bin_index = format(i, 'b').zfill(a_len-1)
  for j in range(a_len-1):
    a_tmp = list(a_tmp)
    if bin_index[j] == '1':
      a_tmp.insert(2*j+1, '+')
    else:
      a_tmp.insert(2*j+1, '#')
    a_tmp = ''.join(a_tmp)
  a_tmp = a_tmp.replace('#', '')
  a_tmp = map(int, a_tmp.split('+'))
  answer += sum(a_tmp)
print(str(answer))