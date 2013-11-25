from django.db import models
import nmap
import logging
from fabric.api import *
# Get an instance of a logger
logger = logging.getLogger("sartu")

#Para fabric:
def reset_kvm(CTID):
	run("qm reset %s"%CTID)

class SshControl():
	def __init__(self):
		self.message = ""
		self.status = 1
	
	@hosts('root@192.168.176.254')	
	def restart(self,CTID):
		
		logger.debug( "Vamos a reiniciar el contenedor %s"%CTID)
		try:
			self.message = execute(reset_kvm,CTID,host='root@192.168.176.254')
			self.status = 1
		except:
			self.message = "Error en la conexion ssh"
			self.status = 0
	
		
class NetStatus():
	def __init__(self):
		self.internet = 0
		self.prey = 0
		self.vpn = 0
		self.ibsartu1 = 0
		self.ibsartu2 = 0
		self.ibsartu3 = 0
		logger.debug( "Vamos a comprobar el estatus")
		logger.debug( "Primero probamos internet...")
		nm = nmap.PortScanner()
		nm.scan('google.com','80','-T5')
		if nm[ nm.all_hosts()[0]].state() == "up":
			logger.debug( "Hay conexion a inet")
			self.internet = 1
		logger.debug( "Ahora sartu prey...")
		nm.scan('alava.sartu.org','80','-T5')
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

