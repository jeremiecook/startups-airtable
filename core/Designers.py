# coding: utf-8
from numpy import False_
from api.Airtable import Airtable
from api.BetaGouv import BetaGouvMembers
from utils.Log import Log
from utils.Env import Env

log = Log()
env = Env()


class Designers:

    table = 'Designers'
    fields = {'fullname': 'Nom', 'role': 'Rôle', 'status': 'Statut',
              'start': 'Arrivée', 'end': 'Fin de mission'}

    def __init__(self):
        self.beta = BetaGouvMembers()
        self.beta_members = self.beta.all()
        self.beta_designers = self.beta.designers()

        self.airtable = Airtable(
            env.get('AIRTABLE_DESIGNERS_BASE_ID'),
            env.get('AIRTABLE_API_KEY'),
            self.table,
            self.fields
        )

        self.airtable_designers = self.airtable.all()

    def add_new_designers(self):
        log.info("\n✅ Designers : Ajout des nouveaux")
        for id, designer in self.beta_designers.items():
            if id not in self.airtable_designers.keys():
                self.airtable.create(id, designer)
                log.info("- 🆕 Nouveau : " + id)

    def update_designers(self):
        log.info("\n✅ Designers : Mise à jour des fiches")
        for id, designer in self.airtable_designers.items():
            if not self.__same(designer, self.beta_members[id]):
                self.airtable.update(
                    designer['airtable_id'], self.beta_members[id])
                log.info("- 🔄 Mise à jour : " + id)

    def __same(self, d1, d2):
        # Compare deux designers
        for key in self.fields.keys():
            if d1[key] != d2[key]:
                return False

        return True
