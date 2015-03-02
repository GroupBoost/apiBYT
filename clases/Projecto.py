#!/usr/bin/python
# -*- coding: utf-8 -*-

import clases

#from Usuario import Usuario
#from Usuario import Usuario

class Projecto :
	
	#Constructor segun posicion color y tipo
	def __init__ (self, nombre, descripcion, owner) :
		self.nombre = nombre
		self.descripcion = descripcion
		self.owner = user
		self.users = []


	#Gestion de usuarios
	
	def addUser(self, user) :
		self.users.append(user)

	def removeUser(self, user) :
		self.users.remove(user)

	#Getters y setters

	def getOwner(self) :
		return self.owner

	def getUsers(self) :
		return self.users

	def getNombre(self) :
		return self.nombre

	def getDescripcion(self) :
		return self.descripcion

	def getJsonResponse(self) :
		dicc = {}
		dicc["nombre"] = self.nombre
		dicc["descripcion"] = self.descripcion
		dicc["owner"] = self.owner
		
		aux = []

		for usr in self.users :
			aux2 = {}
			aux2["nick"] = usr.getNick()
			aux.append(aux2)

		dicc["users"] = aux

		return dicc
