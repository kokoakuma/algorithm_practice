def lcs(txt1, txt2):
  m = len(txt1)
  n = len(txt2)
  table = [[0 for j in range(n)] for i in range(m)]

  for i in range(m):
    for j in range(n):
      if txt1[i] == txt2[j] and i > 0 and j > 0:
        table[i][j] = table[i-1][j-1] + 1
      elif txt1[i] == txt2[j]:
        table[i][j] = 1
      else:
        table[i][j] = max(table[i][j-1], table[i-1][j])

  return table[m-1][n-1]

N = int(input())
for i in range(N):
  text1 = input()
  text2 = input()
  print(lcs(text1, text2))

# ?一致個数だけ求めるらしい
def lcs(a: str, b: str):
    L = []
    for bk in b:
        bgn_idx = 0  # 検索開始位置
        for i, cur_idx in enumerate(L):
            # ※1
            chr_idx = a.find(bk, bgn_idx) + 1
            if not chr_idx:
                break
            L[i] = min(cur_idx, chr_idx)
            bgn_idx = cur_idx
        else:
            # ※2
            chr_idx = a.find(bk, bgn_idx) + 1
            if chr_idx:
                L.append(chr_idx)
    return len(L)
 
# ---------------------------------------
print(lcs('>abcbdabc', 'bdcaba'))  # => 4