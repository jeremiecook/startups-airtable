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
		self.changed_se = {}


	def new_startups(self, verbose=True, create=False):
		if verbose: 
			print("\n🆕 Nouvelles Startups :")

		for id, se in self.beta_startups.items():
			if not self.airtable_startups.get(id):
				self.__new_startup(id, se, verbose, create)

		if verbose: 
			print("👉 {count} nouvelles SE".format(count=len(self.new_se)))

		return self.new_se

	def updated_startups(self, verbose=True, update=False):
		if verbose: 
			print("\n🆕 Startups ayant évolué :")

		for id, se in self.beta_startups.items():
			if self.airtable_startups.get(id) and se.get("phase") != self.airtable_startups.get(id).get("phase"):
				self.__updated_startup(id, se, verbose, update)

		if verbose: 
			print("👉 {count} SE ayant évolué".format(count=len(self.changed_se)))

		return self.changed_se

	def __new_startup(self, id, se, verbose, create):
		self.new_se[id] = se

		if create:
			self.airtable.create(id, se.get('name'), se.get('mission'), se.get('phase'))

		if verbose:
			print("* {emoji}{name} ({id}) - {phase} - {mission}".format(
				emoji= "✅ " if create else "",
				name=se.get('name'), 
				id=id,
				phase=se.get('phase'), 
				mission=se.get('mission')
			))

	def __updated_startup(self, id, se, verbose, update):
		self.changed_se[id] = se

		if update:
			# TODO : récupérer la date, et charger dans airtable
			self.airtable.update(id, se.get('name'), se.get('mission'), se.get('phase'))

		if verbose:
			print("* {emoji}{name} ({id}) - {phase} to {new_phase}".format(
				emoji= "✅ " if update else "",
				name=se.get('name'), 
				id=id,
				phase=self.airtable_startups.get(id).get('phase'), 
				new_phase=se.get('phase'), 
			))


verbose = True
write = False

sync = SyncStartup()
sync.new_startups(verbose, write)
sync.updated_startups(verbose, write)

