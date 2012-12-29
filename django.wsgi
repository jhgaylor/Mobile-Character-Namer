import os
import sys

sys.path.append('/var/www/name.codegur.us/CharacterNamer')

#os.environ['PYTHON_EGG_CACHE'] = '/var/www/name.codegur.us/CharacterNamer/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'CharacterNamer.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

my_venv = os.apth.join('/var/www/name.codegur.us/nameenv', "bin/activate")
execfile(my_venv, dict(__file__=my_venv)) 
