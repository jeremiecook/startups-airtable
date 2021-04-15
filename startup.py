# coding: utf-8
from AirtableAPI import AirtableAPI
from BetaGouvAPI import BetaGouvAPI

class SyncStartup:

	def __init__(self):
		# Load BetaGouv data
		self.beta = BetaGouvAPI()
		self.beta_startups = self.beta.all()

		# Load Airtable data
		self.airtable = AirtableAPI()
		self.airtable_startups = self.airtable.all()


	def find_new_se(self):
		print("hello")
		# Liste d'ids dans Airtable
		# ids = [se['fields'].get('ID') for se in airtable_base]

		# new_startups = []
		# for startup in beta_base:
		# 	if (startup.get('id') not in ids):
		# 		new_startups.append(startup)

		# return new_startups

	def print_new_se(self):
		print("print_new_se")
		# new_se = find_new_se(startups_source, startups_airtable)
		# print("\nNouvelles Startups :")
		# for se in new_se:
		# 	print("* {name} ({id}) - {phase} - {mission}".format(
		# 		name=se.get('attributes').get('name'), 
		# 		id=se.get('id'),
		# 		phase=se.get('attributes').get('phases')[-1].get('name'), 
		# 		mission=se.get('attributes').get('pitch')
		# 	))

	def load_new_se(self):
		print("load_new_se")
		# new_se = find_new_se(startups_source, startups_airtable)
		# for se in new_se:
		# 	id = se.get('id')
		# 	name = se.get('attributes').get('name')
		# 	phase = se.get('attributes').get('phases')[-1].get('name')
		# 	mission = se.get('attributes').get('pitch')
		# 	print("* {name} ({id}) - {phase} - {mission}".format(name=name, id=id, phase=phase, mission=mission))
		# 	api.create(id, name, mission, phase)


sync = SyncStartup()
sync.find_new_se()



