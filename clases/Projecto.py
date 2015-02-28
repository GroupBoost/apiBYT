#!/usr/bin/python
# -*- coding: utf-8 -*-

from Usuario import Usuario

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

