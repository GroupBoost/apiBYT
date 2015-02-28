#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import web
import json
import clases

controlador = clases.Controlador()

urls = (
	'/(.*)', 'basura'
)

app = web.application(urls, globals())

class basura:
	def GET(self, basura):
		return "<h1>Nop</h1>"

if __name__ == "__main__":
	app.run()
