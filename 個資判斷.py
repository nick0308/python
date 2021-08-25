name =input("打名字啦,哪次沒名字:")
gender =input("性別:")
email =input("電子信箱:")
dinner =input("晚餐吃:")

if name.count("*") != 0 :
  print("不要亂打啦")
else :
  print(f"名字:{name}")
  print(f"性別:{gender}")
  print(f"電子信箱：{email}")
  print(f"晚餐吃:{dinner}")
