import random

print("跟我猜拳吧！")

guess = input("你先出:")
nick = random.randrange(2)
answer = ["剪刀","石頭","布"]

if nick == 0 :
  nick = answer[0]
elif nick == 1 :
  nick = answer[1]
else :
  nick = answer[2]

def rps(guess,nick):
    if guess == answer[0] :
      if nick == answer[0] :
        print(f"Nick:{nick}") 
        print("平手")
      elif nick == answer[1] :
        print(f"Nick:{nick}") 
        print("Nick wins!")
      else :
        print(f"Nick:{nick}") 
        print("You win!")
    elif guess == answer[1]:
      if nick == answer[0] :
        print(f"Nick:{nick}") 
        print("You win!")
      elif nick == answer[1] :
        print(f"Nick:{nick}") 
        print("draw!")
      else :
        print(f"Nick:{nick}") 
        print("Nick wins!")
    else:
      if nick == answer[0] :
        print(f"Nick:{nick}") 
        print("Nick wins!")
      elif nick == answer[1] :
        print(f"Nick:{nick}") 
        print("You win!")
      else :
        print(f"Nick:{nick}") 
        print("draw QQ")

rps(guess,nick)
