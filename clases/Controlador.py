#!/usr/bin/python
# -*- coding: utf-8 -*-

from Usuario import Usuario
from Projecto import Projecto

class Controlador :
	
	#Constructor segun posicion color y tipo
	def __init__ (self) :
		self.users = []
		self.projectos = []


	#Gestion de usuarios y projectos

	def nuevoUser(self, nick, passwd, correo, descripcion, localidad)
		self.users.append(Usuario(nick, passwd, corre, descripcion, localidad)	

	def nuevoProjecto(self, nick, nombre, descripcion) :

		user = self.getUserByNick(nick)
		aux = Projecto(nombre,descripcion, user)
		user.addUserPro(aux)
		self.projectos(aux)

	
	#Getters y setters

	def getUserByNick(self, nick) :
		for aux in self.users :
			if nick == aux.getNick()
				return aux

	def getProjectByNombre(self, nombre) :
		for aux in self.projectos :
			if nick == aux.getNombre()
				return aux


	def getUsers(self) :
		return self.users

	def getProjectos(self) :
		return self.projectos

