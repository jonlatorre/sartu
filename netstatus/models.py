from django.db import models

# Create your models here.

def test_port(host,port):
	#port = 3389
	import nmap
	nm = nmap.PortScanner()
	res = nm.scan(host,'%s'%port)
	if res["scan"][host]["tcp"][port]["state"] == "open":
		print "EL pierto esta OPEN"
		return True
	else:
		return False

