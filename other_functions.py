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

print(a_small_engine_for_finding_words("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", 'Ipsum'))



            

    