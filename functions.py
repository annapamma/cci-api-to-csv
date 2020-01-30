import json
import urllib.request
import os


def make_request(endpoint, circle_token):
    header = {
        'Circle-Token': circle_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    req = urllib.request.Request(endpoint, headers=header)
    return json.loads(urllib.request.urlopen(req).read())


