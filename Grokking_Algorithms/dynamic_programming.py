# 最長共通部分文字列
def find_longest_common_substring(word_a, word_b):
  a = list(word_a)
  b = list(word_b)
  len_a = len(a)
  len_b = len(b)
  table = [[ 0 for i in range(len_b)] for i in range(len_a)]
  for i in range(len_a):
    for j in range(len_b):
      if a[i] == b[j]:
        table[i][j] = table[i-1][j-1] + 1
      else:
        table[i][j] = 0
  print(table)

find_longest_common_substring('fish','fosh')

# 最長共通部分列(一致している文字の個数)
def find_longest_common_subsequence(word_a, word_b):
  a = list(word_a)
  b = list(word_b)
  len_a = len(a)
  len_b = len(b)
  table = [[ 0 for i in range(len_b)] for i in range(len_a)]
  for i in range(len_a):
    for j in range(len_b):
      if a[i] == b[j]:
        table[i][j] = table[i-1][j-1] + 1
      else:
        table[i][j] = max(table[i][j-1], table[i-1][j])

  result = []
  for i in range(len_a):
    result.extend(table[i])
  print(f"Number of longest common subsequence is {max(result)}")
  print(table)

find_longest_common_subsequence('fish','fosh')
