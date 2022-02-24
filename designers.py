"""
Show outdated designers from Airtable

Usage:
	designers.py
	designers.py [-w|--write] [-e ENV]
	designers.py -h|--help
	designers.py -v|--version

Options:
	-w --write          Sync outdated designers
	-h --help           Show this screen
	-v --version        Show version
	-e ENV --env=ENV  Use given file for Airtable configuration [default: .env]
"""

# coding: utf-8
from turtle import end_fill
from docopt import docopt
# from AirtableAPI import AirtableAPI
from BetaGouvAPI import BetaGouvMembers


class Designers:

    def __init__(self):
        end

    def update_designers(self):
        end

    def add_new_designers(self):
        end


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    verbose = True
    write = arguments['-w'] or arguments['--write']
    env = arguments['ENV'] or ".env"

    # sync = SyncDesigners(env)
    # sync.new_startups(verbose, write)
    # sync.updated_startups(verbose, write)

    designers = Designers()
    designers.update_designers()
    designers.add_new_designers()

    #designers = members.all()
    print(members.get('jeremie.cook'))
