#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import web
import json
import clases

controladora = clases.Controlador()

urls = (
	'/registro/' 'Registro',
	'/login/', 'Login',
	'/nuevoPro/', 'NuevoPro'
)

app = web.application(urls, globals())

class Registro :
	def POST (self) :
		jobj = json.loads(web.data())
		dicc = {}
		aux = controladora.nuevoUser(jobj)
		if aux[0]  == True:
			dicc["resultado"] = True
		else :
			dicc["resultado"] = False
			dicc["error"] = aux[1]

		return json.dumps(dicc)

class Login :
	def POST (self) :
		jobj = json.loads(web.data())
		dicc = {}

		if controladora.login(jobj) == True :
			dicc["resultado"] = True
		else :
			dicc["resultado"] = False

		return json.dumps(dicc)

class NuevoPro :
	def POST (self) :
		jobj = json.loads(web.data())
		dicc = {}

		if controladora.nuevoProjecto(jobj) == True :
			dicc["resultado"] = True
		else :
			dicc["resultado"] = False

		return json.dumps(dicc)
		

if __name__ == "__main__":
	app.run()
