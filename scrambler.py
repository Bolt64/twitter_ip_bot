#!/usr/bin/python3

"""
Scrambles the ip address in a suitable manner and adds a timestamp as well.

If you are worried about directly tweeting your public ip address
on twitter, the scramble function takes in an ip address if given, else
it determines the ip on its own and scrambles it so it's still readable
although it doesn't look like an ip address. Change the scrambled text to suit 
your needs.

For example, the ip address 12.127.3.45 is scrambled to
12 years a slave. 127 hours. 3 days of misery. Core temperature 45 degree celsius
"""

import get_ip as ip
import datetime

def scramble(ip_address=None, only_timestamp=True):
    """
    Scrambles the ip address. If no argument is given the ip_address is determined on its own.
    """

    if not ip_address:
        ip_address=ip.get_ip()

    now=datetime.datetime.now()
    timestamp=", {3}:{4}:{5}, {0}/{1}/{2}.".format(now.day, now.month, now.year, str(now.hour).zfill(2), str(now.minute).zfill(2), str(now.second).zfill(2))
    scrambled_text="{0} years a slave. {1} hours. {2} days of misery. Core temperature {3} degree celsius.".format(*ip_address.split('.'))
    if not only_timestamp:
        return scrambled_text+timestamp
    else:
        return ip_address+timestamp
