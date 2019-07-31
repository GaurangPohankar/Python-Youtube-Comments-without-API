'''
import pafy

url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
video = pafy.new(url)

print(video.title)
print(video.rating)
print(video.viewcount)
print(video.author)
print(video.length)
print(video.duration)
print(video.likes)
print(video.dislikes)
print(video.description)
'''

from urllib.request import urlopen
import json

channel_id = 'UC8w4I8t2OpqoOpzzNT1c2dg'

def get_all_video_in_channel(channel_id):
    api_key = 'AIzaSyCbFsgQGzi7rdEyun9-cz7dsBJWDIOjtM4'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    print(video_links)
    return video_links
