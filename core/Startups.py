# coding: utf-8
from numpy import False_
from api.Airtable import Airtable
from api.BetaGouv import BetaGouvStartups
from utils.Log import Log
from utils.Env import Env

log = Log()
env = Env()


class Startups:

    table = "Startups d'État"
    fields = {'name': 'Nom', 'phase': 'Statut', 'incubator': 'Incubateur',
              'statistiques': 'Statistiques', 'start': 'Date de début'}

    def __init__(self):
        self.beta = BetaGouvStartups()
        self.beta_startups = self.beta.all()

        self.airtable = Airtable(
            env.get('AIRTABLE_STARTUPS_BASE_ID'),
            env.get('AIRTABLE_API_KEY'),
            self.table,
            self.fields
        )

        self.airtable_startups = self.airtable.all()

    def add_new_startups(self):
        log.info("\n✅ Startups : Ajout des nouvelles Startups")
        for id, startup in self.beta_startups.items():
            if id not in self.airtable_startups.keys():
                self.airtable.create(id, startup)
                log.info("- 🆕 Nouveau : " + id)

    def update_startups(self):
        log.info("\n✅ Startups : Mise à jour des fiches")
        for id, startup in self.airtable_startups.items():

            if id in self.beta_startups.keys() and not self.__same(startup, self.beta_startups[id]):
                self.airtable.update(
                    startup['airtable_id'], self.beta_startups[id])
                log.info("- 🔄 Mise à jour : " + id)

    def __same(self, s1, s2):
        # Compare deux designers
        for key in self.fields.keys():
            if s1[key] != s2[key]:
                return False
        return True
