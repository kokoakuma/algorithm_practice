### ABC175

# A
N = input()
result = 0
if N == "RRR":
  print('3')
elif N == 'RRS' or 'SRR':
  print('2')
elif N == 'RSS' or 'SRS' or 'SSR' or 'RSR':
  print('1')
else:
  print('0')

def mulit(a):
  a_copy = list(a)
  return len(a) == len(set(a_copy))
def isTriangle(x):
  return x[0] + x[1] > x[2]

# B
N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
a_len = len(A)
answer = []
for i in range(0, a_len-2):
  for j in range(i+1, a_len-1):
    for k in range(j+1, a_len):
      answer.append([A[i], A[j], A[k]])

answer = [i for i in answer if mulit(i)]
answer = [i for i in answer if isTriangle(i)]
answer_len = len(answer)
print(f"{answer_len}")

# C
X, K, D = map(int,input().split())
X = abs(X)
time = X // D
time = min(K, time)
X = X - (D * time)
K = K - time

if K % 2 == 0:
  print(X)
else:
  print(abs(X - D))