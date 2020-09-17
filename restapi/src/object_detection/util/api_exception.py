import time
from flask import Flask, request, abort


class ApiException:

	@staticmethod
	def handle(func):

		def wrapper(*args, **kwargs):

			try:
				#print(">>> API Exception")
				val = func(*args, **kwargs)
				#print("<<< API Exception")
				return val
			except:
				return abort(400)

		wrapper.__name__ = func.__name__
		return wrapper


