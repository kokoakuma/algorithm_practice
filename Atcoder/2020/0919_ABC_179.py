# A
N = input()
n_len = len(N)
if N[n_len-1] == 's':
  print(N + 'es')
else:
  print(N + 's')


# B
N = int(input())
ans = 'No'
count = 0
for i in range(N):
  a, b = list(map(int, input().split()))
  if a == b:
    count += 1
  else:
    count = 0
  if count == 3:
    ans = 'Yes'

print(ans)






# C
# 素数
def make_perfect_table(n):
  A=list(range(2,n+1))
  p=[1]
  while A[0]**2<=n:
  	tmp=A[0]
  	p.append(tmp)
  	A=[e for e in A if e%tmp!=0]
  return p+A+[n]

# 約数を求める
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return len(divisors)


def count_perfect(N):
  i=2
  ans=dict()
  div_sum=1
  n=N
  while i*i <=N:
  	while n%i==0:
  		n=n//i
  		if i in ans:
  			ans[i]+=1
  		else:
  			ans[i]=1
  	i+=1
  if n!=1:
  	ans[n]=1
  ans_list=list(ans.items())
  for j in ans_list:
  	div_sum*=j[1]+1
  return div_sum


N = int(input())
ans = 0
for i in range(1, N):
  ans += count_perfect(i)

print(ans)

####

def make_perfect_table(n):
  A=list(range(2,n+1))
  p=[]
  while A[0]**2<=n:
  	tmp=A[0]
  	p.append(tmp)
  	A=[e for e in A if e%tmp!=0]
  return p+A

def count_perfect(N):
  ans=dict()
  div_sum=1
  n=N
  while i*i <=N:
	  while n%i==0:
  		n=n//i
  		if i in ans:
  			ans[i]+=1
  		else:
  			ans[i]=1
  	i+=1
  if n!=1:
  	ans[n]=1
  ans_list=list(ans.items())
  for j in ans_list:
  	div_sum*=j[1]+1
  return div_sum

def count_divide(n):
  ans=list()
  i=1
  while i*i<=n:
  	if n%i==0:
  		ans.append(i)
  		ans.append(n//i)
  	i+=1
  return len(ans)


def make_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors == 1
            if i != n // i:
              divisors == 1
    return divisors

num = int(input())
ans = 0
for i in range(1, num):
  ans += make_divisors(i)

print(ans)

N = int(input())
ans = 0
for a in range(1, N+1):
  ans += N // A

print(ans)


# 解答
# A * B <= C - 1
# B <= (C - 1) // A
# Aを全探索し、1からBまでの個数がある
N = int(input())
ans = 0
for a in range(1, N):
  ans += (N-1) // a

print(ans)


# D

