# coding=utf8
"""
The script is used to log in USTB campus network
Modify username and password to yours
Put the script in computer startup items
Then computer will log in campus network automatically when startup
Python version：3.5.1
"""

import httplib2
import urllib
import subprocess
import re

"""
This function will return computer's local temporary ipv6 address if it exists,
otherwise return None.
Every computer has two ipv6 addresses, a ipv6 address and a temporary ipv6 address.
We use the temporary ipv6 address.
"""


def get_local_tmp_v6ip():
    get_ipv6_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
    output = (get_ipv6_process.stdout.read())
    ipv6_pattern = '(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})'
    m = re.findall(ipv6_pattern, str(output))
    if m is not None:
        # m is a list of tuples
        # m[1] is the second tuple
        # m[1][0] is the temporary ipv6 address
        return m[1][0]
    else:
        return None


# modify username and password to yours
username='your username'
password='your password'
savePWD = 'on'

headers = {"Connection": "keep-alive",
           "Cookie": "myusername=%s; username=%s; smartdot=%s; pwd=%s" % (username, username, password, password),
           "Content-Type": "application/x-www-form-urlencoded"}

body = urllib.parse.urlencode({'DDDDD': username,
                               'upass': password,
                               '0MKKey': '123456789',
                               'v6ip': get_local_tmp_v6ip(),
                               'savePWD': savePWD})

http = httplib2.Http()
response, content = http.request("http://202.204.48.66", "POST", body=body, headers=headers)
if response.status == 200:
    print(response)
    print(content)
