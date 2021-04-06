# coding: utf-8

import os
import csv

import pandas
import requests
from airtable import airtable

from os.path import join, dirname
from dotenv import load_dotenv

#
# Récupérer les variables d'environnement (API Airtable)
#
env = join(dirname(__file__), '.env')
load_dotenv(env)


#
# Récupération des données CSV sur le site Beta Gouv
#
url = "https://beta.gouv.fr/api/v1.7/startups.csv"
startups = pandas.read_csv(url, error_bad_lines=False, engine="python")
# ajouter le paramètre quotechar="'" quand le csv sera réparé
# print(startups)
# for s in startups:
#     print(s)


print(os.getenv('AIRTABLE_BASE_ID'))
print(os.getenv('AIRTABLE_API_KEY'))
print(os.getenv('AIRTABLE_TABLE'))


#
# Récupération des données Airtable
#
at = airtable.Airtable(os.getenv('AIRTABLE_BASE_ID'),
                       os.getenv('AIRTABLE_API_KEY'))
se = at.get(os.getenv('AIRTABLE_TABLE'))
print(se)
