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
              'startups': 'Startups', 'start': 'Arrivée', 'end': 'Fin de mission'}

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

        # Récupération des ID de SE
        airtable_se = Airtable(
            env.get('AIRTABLE_DESIGNERS_BASE_ID'),
            env.get('AIRTABLE_API_KEY'),
            "Startups d'État",
            {'id': 'ID'}
        )

        self.startups = airtable_se.all()

    def add_new_designers(self):
        log.info("\n✅ Designers : Ajout des nouveaux")
        for id, designer in self.beta_designers.items():
            if id not in self.airtable_designers.keys():
                designer = self.__prepare_for_airtable(designer)
                self.airtable.create(id, designer)
                log.info("- 🆕 Nouveau : " + id)

    def update_designers(self):
        log.info("\n✅ Designers : Mise à jour des fiches")

        for id, designer in self.airtable_designers.items():
            record = self.__prepare_for_airtable(self.beta_members[id])
            if not self.__same(designer, record):
                print(designer)
                print(record)
                self.airtable.update(
                    designer['airtable_id'], record)
                log.info("- 🔄 Mise à jour : " + id)

    def __same(self, d1, d2):
        # Compare deux designers
        for key in self.fields.keys():
            if d1[key] != d2[key]:
                return False
        return True

    # TODO Code à refactorer

    def __prepare_for_airtable(self, designer):
        # Startups : add airtable keys
        if (designer['startups']):
            for key, startup in enumerate(designer['startups']):
                if self.startups[startup]:
                    designer['startups'][key] = self.startups[startup]['airtable_id']
                else:
                    del designer['startups'][key]
                    log.warning("La startup " + startup +
                                " n'existe pas en base")

            # Si le tableau est vide, on le définit à None plutôt que [] pour les comparaisons avec Airtable
            if 0 == len(designer['startups']):
                designer['startups'] = None

        else:
            designer['startups'] = None

        return designer
