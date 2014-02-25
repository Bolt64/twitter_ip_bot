#!/usr/bin/env python3

"""
Main function of the program. Regularly checks the ip address. If changed, posts the new ip on twitter.
"""

import twitter_bot_methods as twitter_bot
import load_tokens as lt
import get_ip, scrambler
import time
import logging

INTERVAL=300                              # Interval after which the program checks its ip address
SECURITY_TOKEN_FILE="security_tokens"     # File containing the security tokens
RECIPIENT="sayantan_khan"                 # The default recipient of the bot's direct messages
LOGFILE="/home/bolt/.twitter-bot.log"

def main(security_token_file=SECURITY_TOKEN_FILE, interval=INTERVAL):

# Creating logger
    logger = logging.getLogger('twitter-bot-logger')
    logger.setLevel(logging.DEBUG)

# Creating file handler
    filehandler = logging.FileHandler(LOGFILE)
    filehandler.setLevel(logging.DEBUG)

# Create a formatter (ToDo: Add new style formatter)
    formatted=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(formatted)

# Add handler to logger
    logger.addHandler(filehandler)

#   Main Code

    tokens=lt.load_tokens(security_token_file)
    logger.debug('Tokens loaded')

    bot=twitter_bot.create_bot(
                               (
                               tokens['OAUTH_TOKEN'],
                               tokens['OAUTH_SECRET'],
                               tokens['CONSUMER_KEY'],
                               tokens['CONSUMER_SECRET']
                               )
                              )

    logger.debug('Bot created')

    last_ip=''
    while True:
        current_ip=get_ip.get_ip()
        logger.debug('Current ip obtained. IP is {0}'.format(current_ip))
        if not current_ip==last_ip:
            logger.debug('Posting ip to twitter.')
            last_ip=current_ip
            scrambled=scrambler.scramble(current_ip)
#            twitter_bot.post_status(bot,scrambled)
            logger.debug('Sending dm to {}'.format(RECIPIENT))
            logger.debug(scrambled)
            twitter_bot.message_user(bot,RECIPIENT, scrambled)

        else:
            logger.debug('IP not changed.')
            logger.debug('Current ip is {}'.format(current_ip))
            logger.debug('Last ip was {}'.format(last_ip))

        logger.debug('Sleeping for {} seconds'.format(INTERVAL))
        time.sleep(INTERVAL)


if __name__=="__main__":
    main()
