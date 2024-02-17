from traceback import print_tb


data = [32, 57, 106, 110, 143, 249, 296, 349, 365, 431, 640, 661, 759, 871, 918, 982]

a = int(input("探す数を入力してください"))
i = 1
left = 0
right = len(data) - 1
while left <= right:
  mid = int((left+right) / 2 )
  print(f"data[{mid}]を調べています")
  if data[mid] == a:
    print(str(mid+1) + "番目にあります")
    break
  elif a < data[mid]:
    right = mid - 1
  else:
    left = mid + 1
if left > right:
  print("見つかりません")
