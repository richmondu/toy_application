from flask import Blueprint, jsonify, abort
from object_detection.uploaded_file import UploadedFile
from object_detection.util.api_logger import ApiLogger
from object_detection.util.api_exception import ApiException



blueprint_objectdetection = Blueprint('blueprint_objectdetection', __name__)


# Upload an image
# curl -H "Content-Type: multipart/form-data" -X POST http://127.0.0.1:8000/api/v1/objectdetection/image -F "image=@image.jpg" 
# curl -H "Content-Type: multipart/form-data" -X POST http://127.0.0.1:8000/api/v1/objectdetection/image -F "image=@image__fliph.jpg" 
@blueprint_objectdetection.route("/image", methods=['POST'])
#@ApiException.handle
@ApiLogger.log
def upload_image():
	img = UploadedFile(key='image')
	file_name = img.store()
	if file_name is None:
		return abort(400)
	img.process(asynch=True)
	return jsonify(status='OK', image={"id": file_name} )

# Download the uploaded image
# curl -O http://127.0.0.1:8000/api/v1/objectdetection/image/image.jpg
# curl -O http://127.0.0.1:8000/api/v1/objectdetection/image/image__fliph.jpg
@blueprint_objectdetection.route("/image/<id>", methods=['GET'])
#@ApiException.handle
@ApiLogger.log
def download_image(id):
	img = UploadedFile(file_name=id)
	result = img.download()
	if result is None:
		return abort(400)
	return result

# Delete the uploaded image
# curl -X DELETE http://127.0.0.1:8000/api/v1/objectdetection/image/image.jpg
# curl -X DELETE http://127.0.0.1:8000/api/v1/objectdetection/image/image__fliph.jpg
@blueprint_objectdetection.route("/image/<id>", methods=['DELETE'])
#@ApiException.handle
@ApiLogger.log
def delete_image(id):
	img = UploadedFile(file_name=id)
	img.delete()
	return jsonify(status='OK')



# Download the processed uploaded image
# curl -o image.jpg http://127.0.0.1:8000/api/v1/objectdetection/image/image.jpg/processed
# curl -o image__fliph.jpg http://127.0.0.1:8000/api/v1/objectdetection/image/image__fliph.jpg/processed
@blueprint_objectdetection.route("/image/<id>/processed", methods=['GET'])
#@ApiException.handle
@ApiLogger.log
def download_image_processed(id):
	img = UploadedFile(file_name=id)
	result = img.download_processed()
	if result is None:
		return abort(400)
	return result

# Delete the processed uploaded image
# curl -X DELETE http://127.0.0.1:8000/api/v1/objectdetection/image/image.jpg/processed
# curl -X DELETE http://127.0.0.1:8000/api/v1/objectdetection/image/image__fliph.jpg/processed
@blueprint_objectdetection.route("/image/<id>/processed", methods=['DELETE'])
#@ApiException.handle
@ApiLogger.log
def delete_image_processed(id):
	img = UploadedFile(file_name=id)
	img.delete_processed()
	return jsonify(status='OK')

