"""
Show outdated designers from Airtable

Usage:
	designers.py
	designers.py [--dry] [-e ENV]
	designers.py -h|--help
	designers.py -v|--version

Options:
	--dry               Don't write into Airtable
	-h --help           Show this screen
	-v --version        Show version
	-e ENV --env=ENV    Use given file for Airtable configuration [default: .env]
"""

# coding: utf-8
from docopt import docopt


from api.Mattermost import Mattermost
from core.Designers import Designers
from core.Startups import Startups
from utils.Log import Log
from utils.Env import Env
log = Log()
env = Env()

if __name__ == '__main__':

    arguments = docopt(__doc__, version='1.0')
    dry = arguments['--dry']
    #env = arguments['ENV'] or ".env"

    if(env.exists('AIRTABLE_STARTUPS_BASE_ID')):
        startups = Startups(dry)
        startups.add_new_startups()
        startups.update_startups()

    if(env.exists('AIRTABLE_DESIGNERS_BASE_ID')):
        designers = Designers(dry)
        designers.add_new_designers()
        designers.update_designers()

    if(env.exists('MATTERMOST_URL')):
        # Poster un message sur Mattermost
        m = Mattermost(
            env.get('MATTERMOST_URL'),
            env.get('MATTERMOST_KEY')
        )
        m.post(log.get())
    else:
        print(log.get())
