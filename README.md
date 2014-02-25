twitter_ip_bot
==============

This bot specifically monitors your public ip address every few minutes, and if changed, posts the new ip address on twitter. If like me, you have an ISP which assigns ip addresses, which vary from day to day, and you need to ssh into your home computer from somewhere outside, you know how difficult things can be. This script aims to solve that problem by posting or directly messaging you on twitter your current ip address. And it keeps checking at every 5 minute intervals to see if the ip has changed and notifies you if so.

===============

Dependencies:

*  Python Twitter Tools
        
        pip install twitter
        

===============

Installation:

1. Install python twitter tools as outlined above.
2. Get OAuth tokens from twitter.
3. Replace the dummy tokens in the security tokens file with the actual tokens.
4. Authorize this application to access your account.
5. Run the `main.py` script.

===============

Things to do:

1. Add support for windows.
2. Improve logging to show errors