import sys
sys.path.append("..")
from models.artist import Artist
from flask import Flask, render_template, request, redirect
from flask import Blueprint

artists_blueprint = Blueprint('artists', __name__)

@artists_blueprint.route("/artists")
def artists():
    artists = Artist.all()
    return render_template('artists/index.html', artists = artists)

@artists_blueprint.route("/artists/new", methods=['GET'])
def create_artist():
    return render_template('artists/create.html')

@artists_blueprint.route("/artists", methods=['POST'])
def new_artist():
    name = request.form['name']
    artist = Artist(name)
    artist.save()
    return redirect('/artists')

@artists_blueprint.route("/artists/<id>", methods=['GET'])
def show_artist(id):
    artist = Artist.find(id)
    return render_template('artists/show.html', artist=artist)

@artists_blueprint.route("/artists/<id>/edit", methods=['GET'])
def edit_artist(id):
    artist = Artist.find(id)
    return render_template('artists/edit.html', artist=artist)

@artists_blueprint.route("/artists/<id>", methods=['POST'])
def update_artist(id):
    name = request.form['name']
    artist = Artist(name, id)
    artist.update()
    return redirect('/artists')

@artists_blueprint.route("/artists/<id>/delete", methods=['POST'])
def delete_artist(id):
    Artist.delete(id)
    return redirect('/artists')
