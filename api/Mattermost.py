# coding: utf-8
import requests


class Mattermost:

    def __init__(self, url, key):
        self.url = url
        self.key = key

    def post(self, text):
        headers = {}
        values = '{"username":"Beta Airtble", "text":"' + text + '"}'
        #values = '{"username":"Beta Airtble", "text":"hello", "props": {"card": "' + "hello" + '"} }'
        response = requests.post(
            self.url + '/hooks/' + self.key, headers=headers, data=values.encode('utf-8'))
        print(response)
