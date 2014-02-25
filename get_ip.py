#!/usr/bin/python3

"""
A script to get the public ip address from http://checkip.dyndns.org
"""
import urllib.error
import urllib.request
import re
import time

def contact_server():
    """
    Try to get public ip address
    """
    ipv4_address_pattern=re.compile(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
    ip_addresses=[]
    try:
        try:
            with urllib.request.urlopen("http://checkip.dyndns.org") as urlobject:
                ip_addresses=[addr for addr in ipv4_address_pattern.findall(str(urlobject.read()))]
            return ip_addresses
        except ConnectionResetError:
            return None
    except urllib.error.URLError:
        return None

def get_ip():
    """
    Keep running in a loop until an ip_address is obtained
    """
    result=None
    while not result:
        time.sleep(0.1)
        result=contact_server()
    return result[0]
