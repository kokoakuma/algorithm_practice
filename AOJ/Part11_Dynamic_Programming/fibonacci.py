table = [None] * 100
table[0] = table[1] = 1

def fibonacci(n):
  if n == 0 or n == 1:
    return 1
  if table[n] != None:
    return table[n]
  table[n] = fibonacci(n-2) + fibonacci(n-1)
  return table[n]

A = int(input())
print(fibonacci(A))

table2 = [None] * 10
def makeFibonacci(n):
  table2[0] = table2[1] = 1
  for i in range(2, n+1):
    if len(table2)-1 < i:
      table2.append([None] * 10)
    table2[i] = table2[i-2] + table2[i-1]
  return table2

print(makeFibonacci(25))