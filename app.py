from artist import Artist
from artists_controller import artists_blueprint
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.register_blueprint(artists_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
