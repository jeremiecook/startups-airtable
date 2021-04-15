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


	def new_startups(self, verbose=True, create=False):
		self.new_startups = {}

		if verbose: 
			print("\n🆕 Nouvelles Startups :")
		for id in self.beta_startups:
			if not self.airtable_startups.get(id):
				se = self.beta_startups.get(id)

				self.new_startups[id] = se
				if verbose:
					print("* {name} ({id}) - {phase} - {mission}".format(
						name=se.get('name'), 
						id=id,
						phase=se.get('phase'), 
						mission=se.get('mission')
					))

		if verbose: 
			print("👉 {count} nouvelles SE".format(count=len(self.new_startups)))

		return self.new_startups

	def load_new_se(self):
		return 1
		# print("\nNouvelles Startups :")
		# for id, se in self.new_startups.items():
		# 	print("* {name} ({id}) - {phase} - {mission}".format(
		# 		name=se.get('name'), 
		# 		id=id,
		# 		phase=se.get('phase'), 
		# 		mission=se.get('mission')
		# 	))
		# print("load_new_se")
		# new_se = find_new_se(startups_source, startups_airtable)
		# for se in new_se:
		# 	id = se.get('id')
		# 	name = se.get('attributes').get('name')
		# 	phase = se.get('attributes').get('phases')[-1].get('name')
		# 	mission = se.get('attributes').get('pitch')
		# 	print("* {name} ({id}) - {phase} - {mission}".format(name=name, id=id, phase=phase, mission=mission))
		# 	api.create(id, name, mission, phase)


sync = SyncStartup()
sync.new_startups()
# sync.print_new_se()


