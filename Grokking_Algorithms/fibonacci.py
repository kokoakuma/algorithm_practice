import timeit
# f[0]=1, f[1]=1, f[2]=2とする
def fib(n):
  if n < 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

# tail recursion 末尾再帰
def fib_acum(n, x1=1, x2=0):
  if n < 1:
    return x1
  else:
    return fib_acum(n-1, x1+x2, x1)


result3 = timeit.timeit('fib(10)', globals=globals(), number=10)
result4 = timeit.timeit('fib_acum(10)', globals=globals(), number=10)
print(result3 / 10)
print(result4 / 10)