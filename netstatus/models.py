from django.db import models
import nmap
import logging
from fabric.api import *
# Get an instance of a logger
logger = logging.getLogger("sartu")


class SshControl():
	def __init__(self):
		
		self.stdout = ""
		self.stderr = ""
		
	def restart(self,CTID):
		logger.debug( "Vamos a reiniciar el contenedor %s"%CTID)
		client = paramiko.SSHClient()
		client.load_system_host_keys()
		client.connect('alava.sartu.org', username='root', password='trsql266')
		stdin, stdout, stderr = client.exec_command('ls')
		#self.stdout = stdout
		for line in stdout:
			self.stdout = self.stdout + line
		for line in stderr:
			self.sterr = self.stderr + line
		client.close()
		
		

class NetStatus():
	def __init__(self):
		self.internet = 0
		self.prey = 0
		self.vpn = 0
<<<<<<< HEAD
		self.isartu1 = 0
		self.isartu2 = 0
		self.isartu3 = 0
		logger.debug( "Vamos a comprobar el estatus")
		logger.debug( "Primero probamos internet...")
=======
		self.ibsartu1 = 0
		self.ibsartu2 = 0
		self.ibsartu3 = 0
		print "Vamos a comprobar el estatus"
		print "Primero probamos internet..."
>>>>>>> 9d0a7903f447fd887c0b56a4786a2bc7d506dc52
		nm = nmap.PortScanner()
		nm.scan('google.com','80','-T5')
		if nm[ nm.all_hosts()[0]].state() == "up":
			logger.debug( "Hay conexion a inet")
			self.internet = 1
		
<<<<<<< HEAD
		logger.debug( "Ahora sartu prey...")
		nm.scan('alava.sartu.org','80')
=======
		print "Ahora sartu prey..."
		nm.scan('alava.sartu.org','80','-T5')
>>>>>>> 9d0a7903f447fd887c0b56a4786a2bc7d506dc52
		if nm[ nm.all_hosts()[0]].state() == "up":
			logger.debug( "Hay conexion a prey")
			self.prey = 1
		
		logger.debug( "Ahora al server de la  vpn...")
		nm.scan('192.168.160.1','80')
		if len(nm.all_hosts()) != 0:
			if nm[ nm.all_hosts()[0]].state() == "up":
				logger.debug( "Hay conexion a server de la vpn")
				self.vpn = 1
		
<<<<<<< HEAD
		logger.debug( "Ahora probamos cada maquina...")
		host = "192.168.176.10"
		port = "3389"
		nm.scan(host,port)
		if len(nm.all_hosts()) != 0:
			if nm[ nm.all_hosts()[0]].tcp(port)["state"]=="open":
				self.ibsartu1 = 1
		else:
			logger.debug( "No hay conexion a las maquinas")
=======
		print "Ahora probamos cada maquina..."
		host = "192.168.176.10-12"
		port = "3389"
		nm.scan(host,port,'-T5')
		if nm.has_host("192.168.176.10"):
			if nm["192.168.176.10"].tcp(int(port))["state"]=="open":
				self.ibsartu1=1
		if nm.has_host("192.168.176.11"):
			if nm["192.168.176.11"].tcp(int(port))["state"]=="open":
				self.ibsartu2=1
		if nm.has_host("192.168.176.12"):
			if nm["192.168.176.12"].tcp(int(port))["state"]=="open":
				self.ibsartu3=1
>>>>>>> 9d0a7903f447fd887c0b56a4786a2bc7d506dc52
