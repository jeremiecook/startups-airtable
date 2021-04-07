# coding: utf-8

import os
import csv

import pandas
import requests
from airtable import airtable

from os.path import join, dirname
from dotenv import load_dotenv


def get_env():
   # Récupérer les variables d'environnement (API Airtable)
    env = join(dirname(__file__), '.env')
    load_dotenv(env)
    # print(os.getenv('AIRTABLE_BASE_ID'))
    # print(os.getenv('AIRTABLE_API_KEY'))
    # print(os.getenv('AIRTABLE_TABLE'))


def get_startups_from_source():
    # Récupérer des données CSV sur le site Beta Gouv
    url = "https://beta.gouv.fr/api/v1.7/startups.csv"
    startups = pandas.read_csv(
        url, error_bad_lines=False, engine="python").to_dict(orient='records')
    # ajouter le paramètre quotechar="'" quand le csv sera réparé
    return startups


def get_startups_from_airtable():
    # Récupérer les données Airtable
    at = airtable.Airtable(
        os.getenv('AIRTABLE_BASE_ID'),
        os.getenv('AIRTABLE_API_KEY')
    )
    startups = at.get(os.getenv('AIRTABLE_TABLE'),
                      fields=['ID', 'Nom', 'Statut'])
    # ,limit=10
    return startups


def find_new_se(beta_base, airtable_base):
    # extraire des colonnes de la base
    # print(beta_base)
    # print(beta_base.loc[:, ["id", "name"]])

    # boucler dans la base
    # for s in beta_base:
    #     print(s)
    # for id in beta_base["id"]:
    # print(id)

    new_startups = []

    # Liste d'ids dans Airtable
    ids = [se['fields'].get('ID') for se in airtable_base['records']]

    for startup in beta_base:
        if (startup['id'] not in ids):
            new_startups.append(startup)

    return new_startups


get_env()
startups_source = get_startups_from_source()
startups_airtable = get_startups_from_airtable()
# print(startups_source[0])
# print(startups_airtable['records'][0]['fields']['ID'])

new_se = find_new_se(startups_source, startups_airtable)
print(new_se)
