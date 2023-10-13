from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello, {escape(name)}!</p>"

# Collection of records:
@app.route("/songs")
def songs_index():
    # 1. Query all songs in the database
    # 2. Display in HTML template, looping through each song adding it's URL by ID.
    return '''
        <div>
            <h1>All Songs</h1>
            <div>
             <!-- Looping through each song: --->
             <!-- @songs.map(|song|) --->
                <p><a href="/songs/1">Song 1</a></p>
                <p><a href="/songs/2">Song 2</a></p>
                <p><a href="/songs/3">Song 3</a></p>
                <p><a href="/songs/4">Song 4</a></p>
                <p><a href="/songs/5">Song 5</a></p>
             <!-- endmap --->
            </div>
        </div>
    '''

# Individual record:
@app.route("/songs/<id>")
def songs_show(id):
    return f"<p>This is song number, {escape(id)}!</p>"
