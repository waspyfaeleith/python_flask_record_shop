from album import Album
from artist import Artist
from flask import Flask, render_template, request, redirect
from flask import Blueprint

albums_blueprint = Blueprint('albums', __name__)

@albums_blueprint.route("/albums")
def albums():
    albums = Album.all()
    return render_template('albums/index.html', albums = albums)

@albums_blueprint.route("/albums/new", methods=['GET'])
def create_album():
    artists = Artist.all()
    return render_template('albums/create.html', artists = artists)

@albums_blueprint.route("/albums", methods=['POST'])
def new_album():
    title = request.form['title']
    artist_id = request.form['artist_id']
    quantity = request.form['quantity']
    album = Album(title, artist_id, quantity)
    album.save()
    return redirect('/albums')

@albums_blueprint.route("/albums/<id>", methods=['GET'])
def show_album(id):
    album = Album.find(id)
    return render_template('albums/show.html', album = album)

@albums_blueprint.route("/albums/<id>/edit", methods=['GET'])
def edit_album(id):
    album = Album.find(id)
    artists = Artist.all()
    return render_template('albums/edit.html', album = album, artists = artists)

@albums_blueprint.route("/albums/<id>", methods=['POST'])
def update_album(id):
    title = request.form['title']
    artist_id = request.form['artist_id']
    quantity = request.form['quantity']
    album = Album(title, artist_id, quantity, id)
    album.update()
    return redirect('/albums')

@albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
def delete_album(id):
    Album.delete(id)
    return redirect('/albums')
