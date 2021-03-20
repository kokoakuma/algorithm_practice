#A

a, b, c = list(map(int, input().split()))


a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

ans = b - c

print(ans)



#B
import math
x = input()

if '.' in x:
  print(x.split('.')[0])
else:
  print(x)


#C
x = input()
ans = 0
len_c = len(x)
if len_c >= 3:
  ans = int((len_c - 1) // 2 * '9')
 
x = int(x)
 
if len_c % 2 != 0:
  print(ans)
else:
  str_x = str(x)
  middle = len_c // 2
  left = int(str_x[:middle])
  right = int(str_x[middle:])
  base = 1 * (10 ** (middle - 1))
  if right < left:
    ans += left - base
    print(ans)
  else:
    ans += left - base + 1
    print(ans)





