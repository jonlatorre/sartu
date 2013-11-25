from django.http import HttpResponse
from django.conf import settings
from django.core.servers.basehttp import FileWrapper
import json
import os

from models import *

def get_status(request):
    status = NetStatus()
    data = json.dumps(vars(status))
    return HttpResponse(data, mimetype='application/json')

def send_ibsartu_file(request,ibsartu_id):
    """                                                                         
    Send a file through Django without loading the whole file into              
    memory at once. The FileWrapper will turn the file object into an           
    iterator for chunks of 8KB.                                                 
    """
    print "Nos piden el fichero para el id ",ibsartu_id
    filename = "%s/ibsartu%s.RDP"%(settings.MEDIA_ROOT,ibsartu_id)
    print "Vamos a servir el fichero ",filename
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    return response
    
def reset_ibsartu_file(request,ibsartu_id):
    ssh = SshControl()
    ssh.restart(101)
    data = json.dumps(vars(ssh))
    return HttpResponse(data, mimetype='application/json')
