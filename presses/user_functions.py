import tweepy as tp
import json
import datetime
import os
import requests
from bs4 import BeautifulSoup

#Tweeter credential
data = {
  "API_key": "",
  "API_secret_key":"",
  "Access_token" :"",
  "Access_token_secret" :""
}

API_key = data['API_key']  
API_secret_key = data['API_secret_key']  
Access_token = data['Access_token']
Access_token_secret = data['Access_token_secret']


#Connection to the twitter
auth = tp.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(Access_token, Access_token_secret)
access_api = tp.API(auth)

def get_user_info(user_id):
    user	=	access_api.get_user(user_id)   
    user_detail ={'location':user.location,
                  'description':user.description,
                  'followers':user.followers_count, 
                  'friend':user.friends_count
                  }
    return user_detail

def get_user_tweets(user_id,startDate = datetime.datetime.now(),endDate =   datetime.timedelta(days=1)):
    tweets = access_api.user_timeline(screen_name=user_id,tweet_mode = 'extended', since=startDate, until=endDate)
    all_tweets = []
    for tweet in tweets:
        tweet_content = {'created_at':tweet.created_at,
                           'full_text':tweet.full_text.split('https')[0],
                           'full_site':'https' +tweet.full_text.split('https')[-1],
                           'retween_count':tweet.retweet_count,
                           'favorite_count':tweet.favorite_count
                           }
        try:                   
        
            if user_id == 'LesEchos':
                 tweet_content['IMG'] = get_img_echo(tweet_content['full_site'])
            elif   user_id == '20Minutes':
                tweet_content['IMG'] = get_img_20min(tweet_content['full_site'])
            else:
                tweet_content['IMG'] = get_img_monde(tweet_content['full_site'])
        except Exception:
            pass
        all_tweets.append(tweet_content)     

    return all_tweets

def get_img_monde(site):
    req = requests.get(site)
    
    if req.status_code == 200:
        soup = BeautifulSoup(req.content, 'html.parser')
        li = soup.find('figure', {'class': 'article__media'})
        children = li.findChildren("img" , recursive=False)
        
    return children['src']

def get_img_echo(site):
    req = requests.get(site)
    if req.status_code == 200:
        soup = BeautifulSoup(req.content, 'html.parser')
        Im = soup.find('img', {'class':'sc-14kwckt-20 jbUOvW'})
    
    return Im['src']

def get_img_20min(site):
    req = requests.get(site)
    if req.status_code == 200:
        soup = BeautifulSoup(req.content, 'html.parser')
        Im = soup.find('img', {'id':'main-illustration'})
    
    return Im['src']
