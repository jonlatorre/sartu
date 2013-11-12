from django.core.management.base import BaseCommand, CommandError
from netstatus.models import *

class Command(BaseCommand):
	 def handle(self, *args, **options):
		import json
		status = NetStatus()
		data = json.dumps(vars(status))
		print data
