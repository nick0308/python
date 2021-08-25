singer = input("選擇歌手:")
song = input("選擇歌曲:")

class Data:
  
  def __init__(self,singer,song):
    self.singer = singer
    self.song = song
  
  def printSinger(self):
    if singer == "周杰倫" :
       print("你選周杰倫")
    elif singer == "陳奕迅" :
       print("你選陳奕迅")
    else :
       print("還沒儲存這個歌手")
       
  def printSong(self):
    if song == "安靜" :
      print("只剩下鋼琴陪我")
    elif song == "淘汰" :
      print("只能說我輸了")
    else :
      print("歌詞庫沒有")
      
a = Data(singer,song)

a.printSinger()
a.printSong()
