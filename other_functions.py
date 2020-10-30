from youtube_transcript_api import YouTubeTranscriptApi
import pytube
import secrets
import json
from termcolor import colored, cprint
import sys
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

# def string_to_json(string):
#     return json.loads(string)

def return_raw_or_text_only_transcript(transcript):
    text_only_transcript = ''
    for i in transcript:
        text_only_transcript = text_only_transcript + i['text'] + ' '
    return text_only_transcript

def add_mark_tags_wherever_necessary(where_is_the_word_present, para):
    words = para.split(' ')
    for i in where_is_the_word_present:
        words.insert(i, '<mark>')
        words.insert(i+1 , '</mark>')

    updated_words_in_string = ''
    for i in words:
        updated_words_in_string = updated_words_in_string + i + ' '
    return updated_words_in_string


print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')


            

    