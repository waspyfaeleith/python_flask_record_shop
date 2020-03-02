import sys
sys.path.append("..")
from models.album import Album
from models.artist import Artist
from repositories.album_repository import AlbumRepository
from repositories.artist_repository import ArtistRepository
from flask import Flask, render_template, request, redirect
from flask import Blueprint

albums_blueprint = Blueprint('albums', __name__)
album_repository = AlbumRepository()
artist_repository = ArtistRepository()

@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template('albums/index.html', albums = albums)

@albums_blueprint.route("/albums/new", methods=['GET'])
def create_album():
    artists = artist_repository.select_all()
    return render_template('albums/create.html', artists = artists)

@albums_blueprint.route("/albums", methods=['POST'])
def new_album():
    title = request.form['title']
    artist_id = request.form['artist_id']
    quantity = request.form['quantity']
    artist = artist_repository.select(artist_id)
    album = Album(title, artist, quantity)
    album_repository.save(album)
    return redirect('/albums')

@albums_blueprint.route("/albums/<id>", methods=['GET'])
def show_album(id):
    album = album_repository.select(id)
    return render_template('albums/show.html', album = album)

@albums_blueprint.route("/albums/<id>/edit", methods=['GET'])
def edit_album(id):
    album = album_repository.select(id)
    artists = artist_repository.select_all()
    return render_template('albums/edit.html', album = album, artists = artists)

@albums_blueprint.route("/albums/<id>", methods=['POST'])
def update_album(id):
    title = request.form['title']
    artist_id = request.form['artist_id']
    quantity = request.form['quantity']
    artist = artist_repository.select(artist_id)
    album = Album(title, artist, quantity, id)
    album_repository.update(album)
    return redirect('/albums')

@albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
def delete_album(id):
    album_repository.delete(id)
    return redirect('/albums')
