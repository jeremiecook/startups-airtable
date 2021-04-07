# coding: utf-8

import os
import csv

import pandas
import requests
from AirtableAPI import AirtableAPI

from os.path import join, dirname
from dotenv import load_dotenv


def get_env():
   # Récupérer les variables d'environnement (API Airtable)
    env = join(dirname(__file__), '.env')
    load_dotenv(env)
    # print(os.getenv('AIRTABLE_BASE_ID'))


def get_startups_from_source():
    # Récupérer des données CSV sur le site Beta Gouv
    url = "https://beta.gouv.fr/api/v1.7/startups.csv"
    startups = pandas.read_csv(
        url, error_bad_lines=False, engine="python").to_dict(orient='records')
    # ajouter le paramètre quotechar="'" quand le csv sera réparé
    return startups


def find_new_se(beta_base, airtable_base):
    # extraire des colonnes de la base
    # print(beta_base)
    # print(beta_base.loc[:, ["id", "name"]])

    new_startups = []

    # Liste d'ids dans Airtable
    ids = [se['fields'].get('ID') for se in airtable_base]
    # print(ids)

    for startup in beta_base:
        if (startup['id'] not in ids):
            new_startups.append(startup)

    return new_startups


get_env()

api = AirtableAPI(
    base=os.getenv('AIRTABLE_BASE_ID'),
    key=os.getenv('AIRTABLE_API_KEY'),
    table=os.getenv('AIRTABLE_TABLE')
)

#api.create("hello", "Hello", "Dire bonjour")


startups_source = get_startups_from_source()
startups_airtable = api.all()

# print(startups_source[0])
# print(startups_airtable['records'][0]['fields']['ID'])

new_se = find_new_se(startups_source, startups_airtable)


print("\nNouvelles Startups :\n")

for se in new_se:
    print("* " + se['name'] + " (" + se['id'] + ")")
#print([se['fields'].get('ID') for se in startups_source['records']])
#print([se['id'] for se in new_se])
