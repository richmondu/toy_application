import os
from flask import Flask
from flask_cors import CORS
from object_detection.app import ObjectDetectionApp
from rest_api_config import config



app = Flask(__name__)
CORS(app)


def initialize():
	object_detection_app = ObjectDetectionApp(app)


if os.name == 'posix':
	initialize()


if __name__ == '__main__':

	if config.debugging:
		initialize()

	# Initialize HTTP server
	context = None
	port = config.CONFIG_HTTP_PORT
	app.run(ssl_context = context,
		host     = config.CONFIG_HTTP_HOST,
		port     = port,
		threaded = True,
		debug    = (config.debugging==1))

