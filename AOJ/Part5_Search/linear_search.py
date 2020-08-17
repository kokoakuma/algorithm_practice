a_N = int(input())
a_list = list(map(int, input().split()))
b_N = int(input())
b_list = list(map(int, input().split()))

answer = 0
for i in b_list:
  if i in a_list:
    answer += 1

print(answer)

# 番兵方
def linear_search(a, li) -> bool:
  i = 0
  li.append(a)
  N = len(li) - 1
  while a != li[i]:
    i += 1
  if i == N:
    return False
  else:
    return True

answer = 0
for i in b_list:
  if linear_search(i, a_list):
    answer += 1
print(answer)
