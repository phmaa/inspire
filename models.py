from app import db
from flask_table import Table, Col


class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  role = db.Column(db.String(100), nullable=False)

  def __init__(self, username, password, role):
    self.username = username
    self.password = password
    self.role = role

def create_user():
  db.drop_all()
  db.create_all()
  
  admin1 = User(username = 'admin1', password = 'admin1', role = 'admin' )
  admin2 = User(username = 'admin2', password = 'admin2', role = 'admin' )
  db.session.add_all([admin1, admin2])
  db.session.commit()
  return admin1, admin2

class Song(db.Model):
  __tablename__ = 'songs'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  artist = db.Column(db.String(100))
  genre = db.Column(db.String(100))

  def __init__(self, title, artist, genre):
    self.title = title
    self.artist = artist
    self.genre = genre

def create_song(new_title, new_artist, new_genre):
  song = Song(new_title, new_artist, new_genre)
  db.session.add(song)
  db.session.commit()
  return song


#  https://dzone.com/articles/flask-101-adding-editing-and-displaying-data
class Results(Table):
  id = Col('id', show=False)
  title = Col('Title')
  artist = Col('Artist')
  genre = Col('Genre')

if __name__ == '__main__':
  print("Creating database table...")
  db.create_all()
  print("Done!")