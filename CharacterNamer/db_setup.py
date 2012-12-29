from CharacterNamer import settings
from django.core.management import setup_environ
import os
setup_environ(settings)

from Namer.models import Name, NameUsage
import json
files = [path+'/'+f for (path, dirs, files) in os.walk('./name_data') for f in files]

for f in files:
	with open(f) as fh:
	 	data = json.loads(fh.read())
	 	for d in data:
	 		n = Name()
	 		n.name = d['name']
	 		n.gender = d['gender']
	 		n.origin = d['origin']
	 		n.meaning = d['meaning']
	 		n.save()