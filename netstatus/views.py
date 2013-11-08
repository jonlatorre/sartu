from django.http import HttpResponse

from models import *

def get_status(request):
	import json
	status = NetStatus()
	data = json.dumps(vars(status))
	return HttpResponse(data, mimetype='application/json')
