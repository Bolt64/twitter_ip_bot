#!/usr/bin/env python3

"""
A bot and its various methods to post statuses and get tweets from twitter.
"""


import twitter

def create_bot(tokens):
    """
    Create a twitter object which will authenitcate itself with the given token

    create_bot(((OAUTH_TOKEN,OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET))
    returns a twitter object all autenticated.
    """
    return twitter.Twitter(auth=twitter.OAuth(*tokens))

def post_status(twitter_bot,status):
    """
    Post given status using the twitter_bot object
    """
    twitter_bot.statuses.update(status=status)

def get_last_tweets(twitter_bot, n=10):
    """
    Returns a list containing the last n tweets from the timeline
    """
    tweets=twitter_bot.statuses.home_timeline()
    return tweets[:n]

def message_user(twitter_bot,recipient,text):
    """
    Direct message a user
    """
    twitter_bot.direct_messages.new(user=recipient,text=text)

