#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import time
import socket

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('X-App-Ip', socket.gethostbyname(socket.gethostname()))
		self.end_headers()

print("Initializing...")
time.sleep(int(os.environ['WAIT_SECONDS']))

print("Initialized, starting server...")
server_address = ('', 8000)
httpd = HTTPServer(server_address, RequestHandler)
httpd.serve_forever()
