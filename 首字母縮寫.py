i = input("請任意輸入一段英文:")
i_list = i.split()
words = []

for a in range(len(i_list)):
  words.append(i_list[a][0])

print(''.join(words).upper())
