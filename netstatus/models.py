from django.db import models
import nmap

class NetStatus():

	
	def __init__(self):
		self.internet = 0
		self.prey = 0
		self.vpn = 0
		self.isartu1 = 0
		self.isartu2 = 0
		self.isartu3 = 0
		print "Vamos a comprobar el estatus"
		print "Primero probamos internet..."
		nm = nmap.PortScanner()
		nm.scan('google.com','80')
		if nm[ nm.all_hosts()[0]].state() == "up":
			print "Hay conexion a inet"
			self.internet = 1
		
		print "Ahora sartu prey..."
		nm.scan('alava.sartu.org','80')
		if nm[ nm.all_hosts()[0]].state() == "up":
			print "Hay conexion a prey"
			self.prey = 1
		
		print "Ahora al server de la  vpn..."
		nm.scan('192.168.160.1','80')
		if len(nm.all_hosts()) != 0:
			if nm[ nm.all_hosts()[0]].state() == "up":
				print "Hay conexion a server de la vpn"
				self.vpn = 1
		
		print "Ahora probamos cada maquina..."
		host = "192.168.176.10"
		port = "3389"
		nm.scan(host,port)
		if len(nm.all_hosts()) != 0:
			if nm[ nm.all_hosts()[0]].tcp(port)["state"]=="open":
				self.ibsartu1 = 1
		else:
			print "No hay conexion a las maquinas"
