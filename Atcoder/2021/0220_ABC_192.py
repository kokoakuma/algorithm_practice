#A
a, b, c = list(map(int, input().split()))


x = int(input())
a = x % 100

print(str(100 - a))

#B
x = list(input())

length = len(x)
odd = []
even = []
for i in range(length):
  if i % 2 == 0:
    odd.append(x[i])
  else:
    even.append(x[i])

odd = ''.join(odd)
even = ''.join(even)

if length == 1 and odd.islower():
  print('Yes')
elif length == 1 and not odd.islower():
  print('No')
elif odd.islower() and even.isupper():
  print('Yes')
else:
  print('No')






#C
n, k = list(map(int, input().split())) # n=初項, k=求めたい項の序数
currentIndex = 0
currentNum = n

def fx(num):
  splitNum = [x for x in str(num)]
  up = sorted(splitNum)
  down = sorted(splitNum, reverse=True)
  upNum = int(''.join(up))
  downNum = int(''.join(down))
  return downNum - upNum

if k == 0:
  print(n)
else:
  while k > currentIndex:
    tmp = fx(currentNum)
    if sorted(list(str(tmp))) == sorted(list(str(currentNum))):
      currentNum = tmp
      break
    currentNum = tmp
    currentIndex += 1

  print(currentNum)



#D
x = input()
m = int(input())
count = 0
maxNum = max(map(int, list(x)))
minBase = maxNum + 1
currentBase = minBase

while int(x, currentBase) <= m:
  count += 1
  currentBase += 1

print(count)


x = input()
m = int(input())
count = 0
maxNum = max(map(int, list(x)))
minBase = maxNum + 1
currentBase = minBase

def calcWithBase(n, base);
  ans = 0
  length = len(n)
  for i in range(length):
    ans += int(n[i]) * base ** (length - i - 1)
  return ans

while calcWithBase(x, currentBase) <= m:
  count += 1
  currentBase += 1

print(count)