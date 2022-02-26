import requests


class Mattermost:

    def __init__(self, url, key):
        self.hook = hook
        self.url = url
        self.key = key

    def post(self):
        headers = {}
        values = '{"username":"Picasso", "text": "Hello !"}'
        response = requests.post(
            self.url + '/hooks/' + self.key, headers=headers, data=values)
        print(response)
