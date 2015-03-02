#!/usr/bin/python
# -*- coding: utf-8 -*-

import clases

#from Usuario import Usuario
#from Projecto import Projecto

class Controlador :
	
	def __init__ (self) :
		self.users = []
		self.projectos = []

		fich = open ("usuarios.txt", "r")
		aux = fich.readlines()

		fich2 = open("projectos.txt", "r")
		aux2 = fich2.readlines()

		fich.close()
		fich2.close()

		for usr in aux :
			jobj = json.loads(usr)
			self.users.append(Usuario(jobj["nick"], jobj["passwd"],
				jobj["correo"], jobj["descripcion"], jobj["localidad"]))

		for projectJson in aux2 :
			jobj = json.loads(projectJson)
			owner = getUserByNick(jobj["owner"])
			project = Projecto(jobj["nombre"],
				jobj["descripcion"], owner))

			for usrName in jobj["users"] :
				usr = getUserByNick(usrName)
				project.addUser(usr)
				usr.addOtherPro(project)

			owner.addUserPro(project)

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
		guardarDatos()
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
		aux = Projecto(jobj["nombre"],jobj["descripcion"], user)
		user.addUserPro(aux)
		self.projectos(aux)
		guardarDatos()
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

		guardarDatos()

	def addUserToProject(self, jobj) :
		project = self.getProjectByNombre(jobj["nombre"])
		user = self.getUserByNick(jobj["nick"])
		project.addUser(user)
		user.addOtherPro(project)
		guardarDatos()
		

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

	def guardarDatos(self) :
		fich = open("usuarios.txt","w")

		for usr in self.users :
			fich.write(json.dumps(usr.getJsonResponse()))

		fich.close()
		fich = open("projectos.txt","w")

		for project in self.projectos :
			fich.write(json.dumps(project.getJsonResponse()))

		fich.close()






