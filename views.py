from flask import request, render_template, session, abort, redirect, url_for
from models import Song, create_song, User, create_user, Results
from app import app, db
import json
import util

@app.route('/')
def index():
  db.create_all()
  return render_template('index.html')

# https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/

@app.route('/team_space', methods=['POST', 'GET'])
def login():
  error = None
  if request.method == 'POST':
    if ( ( request.form['password'] == 'admin1' and request.form['username'] == 'admin1') or 
    (request.form['password'] == 'admin2' and request.form['username'] == 'admin2' ) ):
      session['logged_in'] = True
      return render_template('/daily_song.html')
    
    else:
      error = 'Unauthorized user.'
      session['logged_in'] = True
      
      return render_template('team_space.html', error=error)
  else:
    return render_template('team_space.html')

@app.route('/about')
def team():
  return render_template('about.html')

@app.route('/main')
def main():
  new_id = util.shuffle_song()
  song = Song.query.filter_by(id=new_id).first()
  img_id = util.shuffle_img()
  return render_template('main.html', songtitle=song.title, artist=song.artist, img_id = img_id)


@app.route('/api/show_all', methods=['POST'])
def show_all():
  all_songs = Song.query.order_by(Song.id.desc()).all()
  db.session.commit()
  return render_template('daily_song.html', all_songs=all_songs)
    

# function to query data
@app.route('/daily_song')
def show_songs():  
  all_songs = Song.query.order_by(Song.id.desc()).all()
  return render_template('daily_song.html', all_songs=all_songs)
  

@app.route('/api/add_songs', methods=['POST', 'GET'])
def add_songs():
  if request.method == 'POST':    
    song_title = request.form.get('title')
    song_artist = request.form.get('artist')
    song_genre = request.form.get('genre')
    daily_song = create_song(song_title, song_artist, song_genre)
    return render_template('daily_song.html', daily_song = daily_song)
  else:
    return render_template('daily_song.html')

# https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
# delete entry
@app.route('/api/delete', methods=['POST'])
def delete_song(): 
  title=request.form['title']
  if request.method== 'POST': 
    song = Song.query.filter_by(title=title).first()
    db.session.delete(song)
    db.session.commit()
    return redirect(url_for('add_songs'))
  else:
    render_template('daily_song.html')
