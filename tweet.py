import os
import time
import tweepy
consumer_key = 'xxxxxx'
consumer_secret = 'xxxxxx'
access_token = 'xxxxxx'
access_token_secret = 'xxxxx'

# these are the key and access secret codes for sending thr tweet
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
b=1
a=0
while a<=2 :
    img="/home/user/Desktop/img"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 -r 800x600 "+img
    os.system(cmd)
    print ("pic taken")
    #read image from location
    api.update_with_media(img, status="Nice one")
    print("wait for 5 seconds for selfiee!!")
    time.sleep(5)
    a+=1
    b+=1
    print("success")
