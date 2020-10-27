from youtube_transcript_api import YouTubeTranscriptApi
import pytube
import secrets
import json
def get_video_id(url):
    return pytube.extract.video_id(url)

def return_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id=video_id)

def get_secret_key():
    return secrets.token_urlsafe(64)

def a_small_engine_for_finding_words(para: str, word_to_find: str):
    list_of_words = para.split()
    yup = []
    word_num = 0
    for i in list_of_words:
        if i == word_to_find:
            yup.append(word_num)
        word_num = word_num + 1
    return yup

def string_to_json(string):
    return json.loads(string)



            

    