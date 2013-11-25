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
		self.isartu1 = 0
		self.isartu2 = 0
		self.isartu3 = 0
		logger.debug( "Vamos a comprobar el estatus")
		logger.debug( "Primero probamos internet...")
		nm = nmap.PortScanner()
		nm.scan('google.com','80')
		if nm[ nm.all_hosts()[0]].state() == "up":
			logger.debug( "Hay conexion a inet")
			self.internet = 1
		
		logger.debug( "Ahora sartu prey...")
		nm.scan('alava.sartu.org','80')
		if nm[ nm.all_hosts()[0]].state() == "up":
			logger.debug( "Hay conexion a prey")
			self.prey = 1
		
		logger.debug( "Ahora al server de la  vpn...")
		nm.scan('192.168.160.1','80')
		if len(nm.all_hosts()) != 0:
			if nm[ nm.all_hosts()[0]].state() == "up":
				logger.debug( "Hay conexion a server de la vpn")
				self.vpn = 1
		
		logger.debug( "Ahora probamos cada maquina...")
		host = "192.168.176.10"
		port = "3389"
		nm.scan(host,port)
		if len(nm.all_hosts()) != 0:
			if nm[ nm.all_hosts()[0]].tcp(port)["state"]=="open":
				self.ibsartu1 = 1
		else:
			logger.debug( "No hay conexion a las maquinas")
