# coding: utf-8

import os
import csv
import json

import requests
from AirtableAPI import AirtableAPI

from os.path import join, dirname
from dotenv import load_dotenv


def get_env():
   # Récupérer les variables d'environnement (API Airtable)
	env = join(dirname(__file__), '.env')
	load_dotenv(env)

def get_startups_from_source():
	# Récupérer des données CSV sur le site Beta Gouv
	url = "https://beta.gouv.fr/api/v2.1/startups.json"
	startups = json.loads(requests.get(url).text)
	return startups.get('data')


def find_new_se(beta_base, airtable_base):
	# extraire des colonnes de la base
	new_startups = []

	# Liste d'ids dans Airtable
	ids = [se['fields'].get('ID') for se in airtable_base]

	for startup in beta_base:

		if (startup.get('id') not in ids):
			new_startups.append(startup)

	return new_startups

def print_new_se(new_se):
	print("\nNouvelles Startups :")
	for se in new_se:
		print("* {name} ({id}) - {phase} - {mission}".format(
			name=se.get('attributes').get('name'), 
			id=se.get('id'),
			phase=se.get('attributes').get('phases')[-1].get('name'), 
			mission=se.get('attributes').get('pitch')
		))

def load_new_se(new_se):
	new_se = find_new_se(startups_source, startups_airtable)


get_env()

api = AirtableAPI(
    base=os.getenv('AIRTABLE_BASE_ID'),
    key=os.getenv('AIRTABLE_API_KEY'),
    table=os.getenv('AIRTABLE_TABLE')
)

startups_source = get_startups_from_source()
startups_airtable = api.all()

new_se = find_new_se(startups_source, startups_airtable)


print("\nNouvelles Startups :\n")

for se in new_se:
    print("* " + se.get('attributes').get('name') + " (" + se.get('id') + ")")
#print([se['fields'].get('ID') for se in startups_source['records']])
#print([se['id'] for se in new_se])
