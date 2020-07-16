def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

# tail recursion 末尾再帰
def accumulateFact(x,acum=1):
  if x == 0:
    return acum
  else:
    return accumulateFact(x-1, x*acum)

