#!/usr/bin/python
# -*- coding: utf-8 -*-

import clases

#from Usuario import Usuario
#from Projecto import Projecto

class Controlador :
	
	def __init__ (self) :
		self.users = []
		self.projectos = []

	#Gestion de usuarios y projectos

	def nuevoUser(self, jobj) :
		for usr in self.users :
			if usr.getNick() == job["nick"] :
				return [False,"nick"]
			if usr.getCorreo() == job["correo"] :
				return [False, "correo"]

		aux = Usuario(jobj["nick"], jobj["passwd"],
			jobj["correo"], jobj["descripcion"], jobj["localidad"])
		self.users.append(aux)
		return [True, aux]

	def login(self, jobj) :
		usr = getUserByNick(jobj["nick"])
		if usr.getPasswd() == jobj["passwd"] :
			return True
		else :
			return False

	def nuevoProjecto(self, jobj) :
		for pro in self.projectos :
			if pro.getNombre() == jobj["nombre"] :
				return False

		user = self.getUserByNick(jobj["nick"])
		aux = Projecto(jobj["nombre"],jobj["descripcion"], jobj["user"])
		user.addUserPro(aux)
		self.projectos(aux)
		return True

	def removeProject(self, jobj) :
		project = self.getProjectByNombre(jobj["nombre"])
		user = self.getUserByNick(jobj["nick"])

		if project.getOwner() == user :
			adjuntos = project.getUsers()

			for usr in adjuntos :
				urs.removeOtherPro(project)

			user.removeUserPro(project)
			self.projectos.remove(project)

		else :
			user.removeOtherPro(project)
			project.removeUser(user)

	def addUserToProject(self, jobj) :
		project = self.getProjectByNombre(jobj["nombre"])
		user = self.getUserByNick(jobj["nick"])
		project.addUser(user)
		user.addOtherPro(project)

	#Getters y setters

	def getUserByNick(self, nick) :
		for aux in self.users :
			if nick == aux.getNick() :
				return aux

	def getProjectByNombre(self, nombre) :
		for aux in self.projectos :
			if nick == aux.getNombre() :
				return aux


	def getUsers(self) :
		return self.users

	def getProjectos(self) :
		return self.projectos

	def getUserInfo (self, jobj) :
		usr = getUserByNick(jobj["nick"])
		return usr.getJsonResponse()

	def getProjectInfo (self, jobj) :
		project = getProjectByNombre(jobj["nombre"])
		return project.getJsonResponse()
