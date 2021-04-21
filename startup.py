"""Show outdated SE from Airtable

Usage:
	startup.py
	startup.py [-w|--write] [-e ENV] 
	startup.py -h|--help
	startup.py -v|--version

Options:
	-w --write          Sync outdated SE
	-h --help           Show this screen
	-v --version        Show version
	-e ENV --env=ENV  Use given file for Airtable configuration [default: .env]
"""

# coding: utf-8
from docopt import docopt
from AirtableAPI import AirtableAPI
from BetaGouvAPI import BetaGouvAPI

class SyncStartup:

	def __init__(self, airtable_env):
		# Load Airtable data
		self.airtable = AirtableAPI(airtable_env)
		self.airtable_startups = self.airtable.all()

		# Load BetaGouv data
		self.beta = BetaGouvAPI()
		self.beta_startups = self.beta.all()

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
			airtable_se = self.airtable_startups.get(id)
			if airtable_se and se.get("phase") != airtable_se.get("phase"):
				self.__updated_startup(id, se, airtable_se, verbose, update)

		if verbose: 
			print("👉 {count} SE ayant évolué".format(count=len(self.changed_se)))

		return self.changed_se

	def __new_startup(self, id, se, verbose, create):
		self.new_se[id] = se

		if create:
			self.airtable.create(id, se.get('name'), se.get('mission'), se.get('phase'))

		if verbose:
			print("* {emoji}{name} ({id}) de {incubator} - {phase} - {mission}".format(
				emoji= "✅ " if create else "",
				name=se.get('name'), 
				id=id,
				incubator=se.get('incubator'),
				phase=se.get('phase'), 
				mission=se.get('mission')
			))

	def __updated_startup(self, id, se, airtable_se, verbose, update):
		self.changed_se[id] = se

		if update:
			self.airtable.update(airtable_id=airtable_se.get('airtable_id'), id=id, name=se.get('name'), mission=se.get('mission'), phase=se.get('phase'))

		if verbose:
			print("* {emoji}{name} ({id}) - {phase} to {new_phase}".format(
				emoji= "✅ " if update else "",
				name=se.get('name'), 
				id=id,
				phase=self.airtable_startups.get(id).get('phase'), 
				new_phase=se.get('phase'), 
			))


if __name__ == '__main__':
	arguments = docopt(__doc__, version='1.0')
	verbose = True
	write = arguments['-w'] or arguments['--write']
	env = arguments['ENV'] or ".env"

	sync = SyncStartup(env)
	sync.new_startups(verbose, write)
	sync.updated_startups(verbose, write)
	




