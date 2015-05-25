from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import tweepy

from biketour.settings import (TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET,
                               TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
                               TWITTER_USER_TIMELINE)


def timeline(request):
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)

    tweets = api.user_timeline(TWITTER_USER_TIMELINE)
    points = [extract_point(t) for t in tweets]

    return JsonResponse({
        'type': 'FeatureCollection',
        'features': points
    }, safe=False)


def extract_point(tweet):
    lat, lon = tweet.geo['coordinates']

    photo_url = None
    for media_item in tweet.entities['media']:
        if media_item['type'] == 'photo':
            photo_url = media_item['media_url']

    icon = 'camera'
    color = '#2c3e50'

    return  {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [lon, lat],
        },
        'properties': {
            'time': tweet.created_at,
            'photo': photo_url,
            'text': tweet.text,
            'marker-symbol': icon,
            'marker-color': color,
            'marker-size': 'large',
        }
    }
