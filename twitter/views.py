import traceback

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import tweepy

from biketour.settings import (TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET,
                               TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
                               TWITTER_USER_TIMELINE)


MAKI_ICONS = [
    'circle-stroked', 'circle', 'square-stroked', 'square', 'triangle-stroked',
    'triangle', 'star-stroked', 'star', 'cross', 'marker-stroked', 'marker',
    'religious-jewish', 'religious-christian', 'religious-muslim', 'cemetery',
    'rocket', 'airport', 'heliport', 'rail', 'rail-metro', 'rail-light',
    'bus', 'fuel', 'parking', 'parking-garage', 'airfield', 'roadblock',
    'ferry', 'harbor', 'bicycle', 'park', 'park2', 'museum', 'lodging',
    'monument', 'zoo', 'garden', 'campsite', 'theatre', 'art-gallery', 'pitch',
    'soccer', 'america-football', 'tennis', 'basketball', 'baseball', 'golf',
    'swimming', 'cricket', 'skiing', 'school', 'college', 'library', 'post',
    'fire-station', 'town-hall', 'police', 'prison', 'embassy', 'beer',
    'restaurant', 'cafe', 'shop', 'fast-food', 'bar', 'bank', 'grocery',
    'cinema', 'pharmacy', 'hospital', 'danger', 'industrial', 'warehouse',
    'commercial', 'building', 'place-of-worship', 'alcohol-shop', 'logging',
    'oil-well', 'slaughterhouse', 'dam', 'water', 'wetland', 'disability',
    'telephone', 'emergency-telephone', 'toilets', 'waste-basket', 'music',
    'land-use', 'city', 'town', 'village', 'farm', 'bakery', 'dog-park',
    'lighthouse', 'clothing-store', 'polling-place', 'playground', 'entrance',
    'heart', 'london-underground', 'minefield', 'rail-underground','aerialway'
    'rail-above', 'camera', 'laundry', 'car', 'suitcase', 'hairdresser',
    'chemist', 'mobilephone', 'scooter', 'gift', 'ice-cream', 'dentist'
]

def timeline(request):
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)

    tweets = api.user_timeline(TWITTER_USER_TIMELINE)

    points = []
    cursor = tweepy.Cursor(api.user_timeline, id=TWITTER_USER_TIMELINE) \
                   .items(100)

    for tweet in cursor:
        try:
            if tweet.geo:
                point = extract_point(tweet)
                points.append(point) 
        except Exception:
            print(traceback.format_exc())

    return JsonResponse({
        'type': 'FeatureCollection',
        'features': points
    }, safe=False)


def extract_point(tweet):
    lat, lon = tweet.geo['coordinates']

    color = '#63b6e5'
    icon = 'post'
    photo_url = ''
    if 'media' in tweet.entities:
        for media_item in tweet.entities['media']:
            if media_item['type'] == 'photo':
                photo_url = media_item['media_url']
                icon = 'camera'

    if 'hashtags' in tweet.entities:
        for hash_tag in tweet.entities['hashtags']:
            icon_key = hash_tag['text'].lower()
            if icon_key in MAKI_ICONS:
                icon = icon_key

    if icon == 'campsite':
        color = '#fa946e'

    if icon == 'restaurant' or icon == 'cafe':
        color = '#c091e6'


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
