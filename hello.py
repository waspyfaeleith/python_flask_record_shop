from artist import Artist
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/artists")
def artists():
    artists = Artist.all()
    return render_template('artists.html', artists = artists)

@app.route("/new-artist", methods=['GET'])
def create_artist():
    return render_template('new_artist.html')

@app.route("/new-artist", methods=['POST'])
def new_artist():
    name = request.form['name']
    artist = Artist(name)
    artist.save()
    return redirect('/artists')


if __name__ == '__main__':
    app.run()
