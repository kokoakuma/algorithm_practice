#A
a, b, c = list(map(int, input().split()))

n = int(input())

if n == 1:
  print(0)
else:
  print(n-1)



#B

n = list(input())

if len(n) == 1:
  print('Yes')

else:
  rev_n = list(reversed(n))
  for i in range(len(rev_n)):
    if rev_n[i] == '0':
      rev_n.pop(0)
    else:
      break
  n_txt = ''.join(rev_n)
  if n_txt == n_txt[::-1]:
    print('Yes')
  else:
    print('No')


#C
r, x, y = list(map(int, input().split()))

goal_euclid = pow(x**2 + y**2, 0.5)

if goal_euclid % r == 0:
  print(int(goal_euclid // r))
else:
  counter = 0
  while goal_euclid >= r * 2:
    counter += 1
    goal_euclid -= r
  counter += 2
  print(counter)

