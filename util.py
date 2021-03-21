import random
from models import Song
def shuffle_song():
  songlist = []  
  songs = Song.query.all()
  for song in songs:
    songlist.append(song.id)
  random.shuffle(songlist)
  song_id = songlist.pop()
  return song_id

def shuffle_img():
  img_range = list(range(1,24))
  random.shuffle(img_range)
  img_id = img_range.pop()
  return img_id


