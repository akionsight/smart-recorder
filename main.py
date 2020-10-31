import other_functions
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

## Imports ##

app = Flask(__name__)
app.secret_key = other_functions.get_secret_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SESSION_TYPE'] = 'sqlalchemy'
db = SQLAlchemy(app)
app.config['SESSION_SQLALCHEMY'] = db
sess = Session(app)

db.create_all()
## app config  ##

# functions


@app.route('/home/')
@app.route('/')
def main_page():
    return render_template('index.html')
@app.route('/upload_page/')
@app.route('/upload/')
def upload():
    return render_template('upload_page.html')

@app.route('/from-yt-link', methods=['POST', 'GET'])
def youtube_link_page():
    if request.method == 'GET':
        return render_template('give_link_page.html')
    elif request.method == 'POST':
        video_url = request.form['url-enter'] ## get video url

        # other_functions.print_red_on_cyan(video_url)

        video_id = other_functions.get_video_id(video_url) ## get video id from url

        # other_functions.print_red_on_cyan(video_id)

        transcript = other_functions.return_transcript(video_id) ## get transcript 

        text_only_transcript = other_functions.return_raw_or_text_only_transcript(transcript) ## get text only transcript 

        # other_functions.print_red_on_cyan(text_only_transcript)

        ### ONLOAD DATA TO SESSION
        session['transcript'] = transcript
        session['TextOnlyTranscript'] = text_only_transcript
        return redirect(url_for('give_transcript'))




@app.route('/transcript/', methods=['POST', 'GET'])
def give_transcript():
    ### GET SESSION ###
    transcript = session['transcript']
    raw_transcript = session['TextOnlyTranscript']
    if request.method == 'GET':

        return render_template('transcript.html', text_only_transcript=raw_transcript) #transcript=transcript, raw_text=raw_transcript)

    elif request.method == 'POST':
        search_query = request.form['search-query'] ## get search query

        places_where_the_word_is_present = other_functions.a_small_engine_for_finding_words(raw_transcript, search_query)
        return render_template('transcript.html', text_only_transcript=raw_transcript)
        


if __name__ == "__main__":
    app.run(debug=True)
