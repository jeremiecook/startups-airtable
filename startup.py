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

		self.new_se = {}


	def new_startups(self, verbose=True, create=False):
		if verbose: 
			print("\n🆕 Nouvelles Startups :")

		for id in self.beta_startups:
			if not self.airtable_startups.get(id):
				se = self.beta_startups.get(id)
				self.__new_startup(id, se, verbose, create)

		if verbose: 
			print("👉 {count} nouvelles SE".format(count=len(self.new_se)))

		return self.new_se


	def __new_startup(self, id, se, verbose, create):
		self.new_se[id] = se
		created = ""

		if create:
			self.airtable.create(id, se.get('name'), se.get('mission'), se.get('phase'))
			created = "✅ "

		if verbose:
			print("* {created} {name} ({id}) - {phase} - {mission}".format(
				created= created,
				name=se.get('name'), 
				id=id,
				phase=se.get('phase'), 
				mission=se.get('mission')
			))

sync = SyncStartup()
sync.new_startups(create=True)


