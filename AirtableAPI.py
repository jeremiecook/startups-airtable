from airtable import airtable
import os
from os.path import join, dirname
from dotenv import load_dotenv


class AirtableAPI:

    def __init__(self):
        self.__get_env()
        self.api = airtable.Airtable(self.base, self.key)
        self.startups = {}

    def __get_env(self):
        # Récupérer les variables d'environnement (API Airtable)
        env = join(dirname(__file__), '.env')
        load_dotenv(env)

        self.base=os.getenv('AIRTABLE_BASE_ID')
        self.key=os.getenv('AIRTABLE_API_KEY')
        self.table=os.getenv('AIRTABLE_TABLE')

    def all(self):
        # Récupérer les données Airtable
        records = self.api.get(self.table, fields=['ID', 'Nom', 'Statut'])
        startups = records['records']

        while records.get('offset'):
            records = self.api.get(
                self.table,
                fields=['ID', 'Nom', 'Statut'],
                offset=records.get('offset')
            )
            startups += records['records']

        # Load result in a nice dict
        for se in startups:
            self.startups[se.get("fields").get("ID")] = dict(
                name=se.get("fields").get("Nom"), 
                phase=se.get("fields").get("Statut"), 
                airtable_id=se.get("id"), 
            )

        return self.startups

    def get(self, id):
        return self.startups.get(id)

    def create(self, id, name, mission, phase):
        try:
            self.api.create(self.table,
                        {'ID': id,
                         'Nom': name,
                         'Mission': mission, 
                         'Statut': phase})
        except airtable.AirtableError as err:
            print("❌ Error: cannot create startup {name} ({id}):".format(name=name, id=id))
            print(err)

    def update(self, airtable_id, id, name, mission, phase):
        try:
            self.api.update(self.table, airtable_id,
                        {'ID': id,
                         'Nom': name,
                         'Mission': mission, 
                         'Statut': phase})
        except airtable.AirtableError as err:
            print("❌ Error: cannot update startup {name} ({id}):".format(name=name, id=id))
            print(err)
