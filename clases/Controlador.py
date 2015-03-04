#!/usr/bin/python
# -*- coding: utf-8 -*-

import clases
import json
#from Usuario import Usuario
#from Projecto import Projecto

class Controlador :
	
	def __init__ (self) :
		self.users = []
		self.projectos = []
		self.tags = []

		fich = open ("datos/usuarios.txt", "r")
		aux = fich.readlines()
		fich.close()

		fich2 = open("datos/projectos.txt", "r")
		aux2 = fich2.readlines()
		fich2.close()

		for usr in aux :
			jobj = json.loads(usr)
			nuevoUser = clases.Usuario(jobj["nick"], 
				jobj["passwd"],	jobj["correo"], jobj["descripcion"], 
				jobj["pais"], jobj["localidad"])

			for tag in jobj["tags"] :
				nuevoUser.addTag(tag["tag"])
				if not tag["tag"] in self.tags :
					self.tags.append(tag["tag"])

			self.users.append(nuevoUser)
				
		for projectJson in aux2 :
			jobj = json.loads(projectJson)
			owner = self.getUserByNick(jobj["owner"])
			project = clases.Projecto(jobj["nombre"],
				jobj["descripcion"], owner)

			for usrName in jobj["users"] :
				usr = self.getUserByNick(usrName["nick"])
				project.addUser(usr)
				usr.addOtherPro(project)

			for tag in jobj["tags"] :
				project.addTag(tag["tag"])
				if not tag["tag"] in self.tags :
					self.tags.append(tag["tag"])

			owner.addUserPro(project)
			self.projectos.append(project)

	#Gestion de usuarios y projectos

	def nuevoUser(self, jobj) :

		if not jobj["nick"] or not jobj["passwd"] \
			or not jobj["correo"] or not jobj["descripcion"] \
			or not jobj["pais"] or not jobj["localidad"] :
			return [False, "empty data"]

		for usr in self.users :
			if usr.getNick() == jobj["nick"] :
				return [False,"nick"]
			if usr.getCorreo() == jobj["correo"] :
				return [False, "correo"]

		aux = clases.Usuario(jobj["nick"], jobj["passwd"],
			jobj["correo"], jobj["descripcion"], 
			jobj["pais"],jobj["localidad"])

		self.users.append(aux)
		self.guardarDatos()
		return [True, aux]

	def login(self, jobj) :
		usr = self.getUserByNick(jobj["nick"])
		if usr.getPasswd() == jobj["passwd"] :
			return True
		else :
			return False

	def nuevoProjecto(self, jobj) :
		if not jobj["nombre"] or not jobj["nick"] \
			or not jobj["descripcion"] :
			return False

		for pro in self.projectos :
			if pro.getNombre() == jobj["nombre"] :
				return False

		user = self.getUserByNick(jobj["nick"])
		aux = clases.Projecto(jobj["nombre"],jobj["descripcion"], user)
		user.addUserPro(aux)
		self.projectos.append(aux)
		self.guardarDatos()
		return True

	def removeProject(self, jobj) :
		project = self.getProjectByNombre(jobj["nombre"])
		user = self.getUserByNick(jobj["nick"])

		if project.getOwner() == user :
			adjuntos = project.getUsers()

			for usr in adjuntos :
				usr.removeOtherPro(project)

			user.removeUserPro(project)
			self.projectos.remove(project)

		else :
			user.removeOtherPro(project)
			project.removeUser(user)

		self.guardarDatos()

	def addUserToProject(self, jobj) :
		project = self.getProjectByNombre(jobj["nombre"])
		user = self.getUserByNick(jobj["nick"])
		project.addUser(user)
		user.addOtherPro(project)
		self.guardarDatos()
		
	#Getters y setters

	def getUserByNick(self, nick) :
		for aux in self.users :
			if nick == aux.getNick() :
				return aux

	def getProjectByNombre(self, nombre) :
		for aux in self.projectos :
			if nombre == aux.getNombre() :
				return aux


	def getUsers(self) :
		return self.users

	def getProjectos(self) :
		return self.projectos

	def getUserInfo (self, jobj) :
		usr = self.getUserByNick(jobj["nick"])
		return usr.getJsonResponse()

	def getProjectInfo (self, jobj) :
		project = self.getProjectByNombre(jobj["nombre"])
		return project.getJsonResponse()

	def guardarDatos(self) :
		fich = open("datos/usuarios.txt","w")

		for usr in self.users :
			jobj = usr.getJsonResponse()
			jobj["passwd"] = usr.getPasswd()
			fich.write(json.dumps(jobj)+"\n")

		fich.close()

		fich2 = open("datos/projectos.txt","w")

		for project in self.projectos :
			jobj = project.getJsonResponse()
			fich2.write(json.dumps(jobj)+"\n")

		fich2.close()

	def getImagenProjecto(self, jobj) :
		return open(imagenes/






