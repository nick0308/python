word = input("key a word:")

anti_word =word[::-1]
if anti_word == word :
  print("是回文")
else :
  print("its not.")
