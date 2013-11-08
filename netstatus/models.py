from django.db import models

# Create your models here.
class NetStatus():

	
	def __init__(self):
		self.internet = 0
		self.prey = 0
		self.vpn = 0
		self.isartu1 = 0
		self.isartu2 = 0
		self.isartu3 = 0
		print "Vamos a comprobar el estatus"
		
		
		import nmap
		nm = nmap.PortScanner()
		nm.scan('google.com','80')
		if nm[ nm.all_hosts()[0]].state() == "up":
			self.internet = 1
		
		nm.scan('alava.sartu.org','80')
		nm.scan('google.com','80')
		if nm[ nm.all_hosts()[0]].state() == "up":
			self.prey = 1

		
		host = "192.168.176.10"
		port = "3389"
		nm.scan(host,port)
		if nm[ nm.all_hosts()[0]].tcp(port)["state"]=="open":
			self.ibsartu1 = 1
