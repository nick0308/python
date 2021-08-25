import random

guess = int(input("猜一個0~100以內數字:"))
num = random.randrange(100)
count = 0
while guess != num :
  if guess > 100 :
      print("不要超過範圍")
      guess = int(input("重新輸入:"))
      count += 1
  elif guess > num :
      print("太多囉！")
      guess = int(input("繼續猜："))
      count += 1
  else :
      print("太少囉！")
      guess = int(input("繼續猜："))
      count += 1

print("Bingo!")
if count <= 3:
  print(f"超猛！ 猜了{count}次就答對")
elif count > 3 and count <= 10 :
  print(f"一般般！你猜了{count}次答對")
else :
  print(f"雷雷！猜{count}次才答對")
