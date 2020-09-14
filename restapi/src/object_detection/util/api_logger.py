import time
from flask import Flask, request


ENABLE_DEBUG = True


class ApiLogger:

	@staticmethod
	def log(func):

		def wrapper(*args, **kwargs):

			if ENABLE_DEBUG:
				starttime = time.time()
				print("\n>>> {}".format(func.__name__))

				try:
					params = "".join([str(arg) for arg in args])
					print("params:  [{}]".format(params))
				except:
					pass
				try:
					headers = dict(request.headers) 
					print("headers: [{}]".format(headers))
				except:
					pass
				try:
					data = request.get_json()
					print("data:    [{}]".format(data))
				except:
					pass

				val = func(*args, **kwargs)
				print("<<< {} {:.2f}\n".format(func.__name__, time.time()-starttime))
				return val

			else:
				return func(*args, **kwargs)

		wrapper.__name__ = func.__name__
		return wrapper


