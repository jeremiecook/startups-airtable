import json
import requests


class BetaGouvAPI:

    def __init__(self):
        self.url = "https://beta.gouv.fr/api/v2.1/startups.json"
        self.startups = {}

    def all(self):
        # Récupérer les données de l'API
        startups = json.loads(requests.get(self.url).text)

        # Load result in a nice dict    
        for se in startups.get('data'):
            self.startups[se.get('id')] = dict(
                name=se.get('attributes').get('name'), 
                phase=se.get('attributes').get('phases')[-1].get('name'), 
                mission=se.get('attributes').get('pitch')
            )

        return self.startups

    def get(self, id):
        return self.startups.get(id)