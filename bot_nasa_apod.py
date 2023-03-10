import tweepy
import requests as req
from PIL import Image
from io import BytesIO

#API_TWITTER

consumer_key = 'fill with your key'
consumer_secret = 'fill with your key'
access_token = 'fill with your key'
access_token_secret = 'fill with your key'

#API_NASA
api_nasa = 'fill with your key' # EXAMPLE = api_nasa = https://api.nasa.gov/planetary/apod?api_key=VJXAfwTXvBXXKCegHuFboXSMc8xVAaht13vfcXXX

#AUTH API TWITTER
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#GET API NASA
request = req.get(api_nasa)
request = request.json()
title = request['title']
image_url = request['url']

# Download the image from the URL

response = req.get(image_url)
image = Image.open(BytesIO(response.content))

# SAVE IMAGE

temp_path = 'temp.jpg'
image.save(temp_path)

# Upload the image to Twitter
media = api.media_upload(temp_path)

tweet = api.update_status(status=title, media_ids=[media.media_id])

import os
os.remove(temp_path)







