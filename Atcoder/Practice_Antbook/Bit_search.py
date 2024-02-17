
# ABC173 C
H,W,K = list(map(int, input().split()))
table = [input() for _ in range(H)]
ans = 0

for mask_h in range(2 ** H):
  for mask_w in range(2 ** W):
    black = 0
    for i in range(H):
      for j in range(W):
        if ((mask_h >> i) & 1 == 0) and ((mask_w >> j) & 1 == 0) and table[i][j] == '#': # 塗り潰し行、列ではなくて、色が黒'#'の場合
          black += 1

    if black == K:
      ans += 1
print(str(ans))

len_sample_list = len(sample_list)

## 2 ** len_sample_listで選択する全パターンを探索
for i in range(2 ** len_sample_list):
    out_list = []
    ## どの桁が1になっているかをチェックするために2進数の各桁をループ
    for j in range(len_sample_list):
        ## i >> jで確認したい桁を一番右までずらして1と論理積をとって「選択」している要素を確認
        if (i >> j) & 1:
            out_list.append(sample_list[j])
    print(out_list)

#ABC197 C

n = int(input())
nums = list(map(int, input().split()))
ans = float('inf')
# 逐一処理をする
# 間に合わない時はpypyを使用する
for i in range(0, 2 ** n-1):
  _or = nums[0]
  _xor = []
  for j in range(n-1):
    if (i >> j) & 1:
      _xor.append(_or)
      _or = nums[j+1]
    else:
      _or |= nums[j+1]
  _xor.append(_or)

  res = 0
  for k in _xor:
    res ^= k
  
  ans = min(ans, res)

print(ans)