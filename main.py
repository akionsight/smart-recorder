import other_functions
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import jsonify
app = Flask(__name__)
app.secret_key = other_functions.get_secret_key()

# functions


@app.route('/home/')
@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/from-yt-link', methods=['POST', 'GET'])
def youtube_link_page():
    if request.method == 'GET':
        return render_template('give_link_page.html')
    elif request.method == 'POST':
        video_url = request.form['url-enter']
        video_id = other_functions.get_video_id(video_url)
        session['video_id'] = video_id
        return redirect(url_for('give_transcript'))


@app.route('/upload_page/')
@app.route('/upload/')
def upload():
    return render_template('upload_page.html')


@app.route('/get-transcript/', methods=['POST', 'GET'])
@app.route('/transcript/', methods=['POST', 'GET'])
def give_transcript():
    if request.method == 'GET':
        try:
            transcript = other_functions.return_transcript(session["video_id"])
            session['transcript'] = transcript
            text_only_transcript = ''
            for i in transcript:
                text_only_transcript = text_only_transcript + i['text'] + ' '
            session['text_only_transcript'] = text_only_transcript
            return render_template('transcript.html', transcript=transcript, raw_text=text_only_transcript)
        except KeyError:
            return '<p>No YT Url Provided</p>'
    elif request.method == 'POST':
        search_query = request.form['search-query']
        print(f"we obtained {search_query} form js with ajax")
        transcript = session['text_only_transcript']
        list_of_words = transcript.split(' ')
        where_is_the_word_present = other_functions.a_small_engine_for_finding_words(
            transcript,  search_query)
        print(f'the word is present in places {where_is_the_word_present}')
        if where_is_the_word_present != []:
            for i in where_is_the_word_present:
                list_of_words.insert(i, '<mark>')
                list_of_words.insert(i+2, '</mark>')
            print(list_of_words)
        else:
            print('lol, word not found')
        return '', 204


if __name__ == "__main__":
    app.run(debug=True)
