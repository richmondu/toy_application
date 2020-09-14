from object_detection.blueprint_objectdetection import blueprint_objectdetection


class ObjectDetectionApp:

	def __init__(self, app):
		app.register_blueprint(blueprint_objectdetection, url_prefix="/api/v1/objectdetection")
