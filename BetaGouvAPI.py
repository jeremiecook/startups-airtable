import json
import requests


class BetaGouvAPI:

    def __init__(self):
        self.url = "https://beta.gouv.fr/api/v2.1/startups.json"
        self.incubators = {}
        self.startups = {}

    def all(self):
        # Récupérer les données de l'API
        startups = json.loads(requests.get(self.url).text)

        self.incubators = {i.get('id'): i.get("attributes").get("title") for i in startups.get("included")}

        # Load result in a nice dict    
        for se in startups.get('data'):
            incubator_id = "/incubators/{name}".format(name=se.get('relationships').get('incubator').get('data').get('id'))

            self.startups[se.get('id')] = dict(
                name=se.get('attributes').get('name'), 
                phase=se.get('attributes').get('phases')[-1].get('name'), 
                mission=se.get('attributes').get('pitch'),
                incubator=self.incubators.get(incubator_id)
            )

        return self.startups

    def get(self, id):
        return self.startups.get(id)