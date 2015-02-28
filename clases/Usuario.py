#!/usr/bin/python
# -*- coding: utf-8 -*-

from Projecto import Projecto

class Usuario :
	
	#Constructor segun posicion color y tipo
	def __init__ (self, nick, correo, descripcion, localidad) :
		self.nick = nick
		self.correo = correo
		self.descripcion = descripcion
		self.localidad = localidad
		self.userPro = []
		self.otherPro = []
	

	#Funciones de gestion de projectos

	def addUserPro(self, projecto) :
		self.userPro.append(projecto)
	
	def addOtherPro(self, projecto) :
		self.otherPro.append(projecto)

	def removeUserPro(self, projecto) :
		self.userPro.remove(projecto)

	def removeOtherPro(self, projecto) :
		self.otherPro.remove(projecto)
				
	#Getters y setters

	def getUserPro(self) :
		return self.userPro

	def getOtherPro(self) :
		return self.otherPro

	def getNick(self) :
		return self.nick

	def getCorreo(self) :
		return self.correo

	def getDescripcion(self) :
		return self.descripcion
	
	def getLocalidad(self) :
		return self.localidad
