#A
a, b, x, y = list(map(int,input().split()))

distance = 0
diff = abs(b - a)

if a < b:
  if x * 2 <= y:
    distance += diff * x * 2
    distance += x
  else:
    distance += diff * y
    distance += x

elif diff == 0:
  distance += x

elif diff == 1 and a > b:
  distance += x

else:
  if (diff - 1) * y + x <= x * (2 * diff - 1):
    distance += (diff - 1) * y
    distance += x
  else:
    distance += x * (2 * diff - 1)


print(distance)


#B


