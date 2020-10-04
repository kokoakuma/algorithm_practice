# A

A, B = list(map(int, input().split()))
x = (A + B) // 2
y = A - x
print(f"{x} {y}")


# B
import collections
N, A = list(input().split())
N = int(N)
A = list(A)
setValues = ['A', 'T', 'C', 'G']

counter = 0
for i in range(N-1):
  for j in range(i+2, N+1, 2):
    arr = A[i:j]
    if len(arr) % 2 != 0:
      continue
    arr_c = dict((x, arr.count(x)) for x in setValues)
    if arr_c['A'] == arr_c['T'] and arr_c['C'] == arr_c['G']:
      counter += 1

print(int(counter))

def Z_algo(S):
    n = len(S)
    LCP = [0]*n
    i = 1
    j = 0
    c = 0#最も末尾側までLCPを求めたインデックス
    for i in range(1, n):
        #i番目からのLCPが以前計算したcからのLCPに含まれている場合
        if i+LCP[i-c] < c+LCP[c]:
            LCP[i] = LCP[i-c]
        else:
            j = max(0, c+LCP[c]-i)
            while i+j < n and S[j] == S[i+j]: j+=1
            LCP[i] = j
            c = i
    LCP[0] = n
    return LCP

import collections
N, A = list(input().split())
N = int(N)
A = list(A)

counter = 0
for i in range(N-1):
  cnt_a = cnt_b = 0
  for a in A[i:]:
    if a == 'A':
      cnt_a += 1
    elif a == 'T':
      cnt_a -= 1
    elif a == 'C':
      cnt_b += 1
    else:
      cnt_b -= 1
    if cnt_a == 0 and cnt_b == 0:
      counter += 1

print(int(counter))

import itertools
N, A = list(input().split())
N = int(N)
A = list(A)

counter = 0
arr = [0]
for a in A:
  if a == 'A':
    arr.append(1)
  elif a == 'T':
    arr.append(-1)
  elif a == 'C':
    arr.append(10000)
  else:
    arr.append(-10000)

arr = list(itertools.accumulate(arr))
arr = arr[1:]

for i in range(len(arr)-1):
  for j in range(i+1, len(arr)):
    if arr[j] - arr[i] == 0:
      counter += 1

print(counter)

