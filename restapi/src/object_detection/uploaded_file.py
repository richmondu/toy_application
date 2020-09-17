import os
import threading
from flask import request, Blueprint, jsonify, abort, send_from_directory
from werkzeug.utils import secure_filename
from object_detection.model.cfg_file import CfgFile
from object_detection.model.img_file import ImgFile
from object_detection.controller.object_detection_haarcascade import HaarCascadeClassifier


IMAGE_FILE_EXT      = ['.jpg']
IMAGE_DIR_UPLOADS   = ".\\object_detection\\user_images\\input\\"
IMAGE_DIR_PROCESSED = ".\\object_detection\\user_images\\output\\"
IMAGE_DIR_CONFIG    = ".\\object_detection\\test_config/"


class UploadedFile:

	def __init__(self, key=None, file_name=None, file_path=None):
		self.key = key
		self.file_name = file_name
		self.file_path = file_path


	def store(self):
		uploaded_file = self._get(self.key)
		if uploaded_file is None:
			print("err1")
			return None
		self.file_name = self._validate(uploaded_file)
		if self.file_name is None:
			return None
		self.file_path = self._save(uploaded_file, self.file_name)
		return self.file_name

	def _get(self, key):
		uploaded_file = request.files.get(key)
		if uploaded_file is None:
			return None
		return uploaded_file

	def _validate(self, uploaded_file):
		file_name = secure_filename(uploaded_file.filename)
		if file_name == '':
			return None
		file_ext = os.path.splitext(file_name)[1]
		if file_ext not in IMAGE_FILE_EXT:
			return None
		return file_name

	def _save(self, uploaded_file, file_name):
		uploaded_file.save(IMAGE_DIR_UPLOADS + file_name)
		return IMAGE_DIR_UPLOADS


	def process(self, asynch=False):
		if asynch:
			x = threading.Thread(target=self._process_image, args=(self.file_name,))
			x.start()
		else:
			self._process_image(self.file_name)

	@staticmethod
	def _process_image(file_name):
		cfg = CfgFile(path="cfg_stop.xml", dir=IMAGE_DIR_CONFIG)
		input = ImgFile(path=file_name, dir=IMAGE_DIR_UPLOADS)
		img_proc = HaarCascadeClassifier(cfg, input, IMAGE_DIR_PROCESSED)
		output = img_proc.process_image()


	def download(self):
		if self.file_name is None:
			return None
		return send_from_directory(directory=IMAGE_DIR_UPLOADS, filename=self.file_name)

	def download_processed(self):
		if self.file_name is None:
			print("1")
			return None
		if not os.path.isfile(IMAGE_DIR_PROCESSED + self.file_name):
			if not os.path.isfile(IMAGE_DIR_UPLOADS + self.file_name):
				print("2")
				return None
			print("3")
			return send_from_directory(directory=IMAGE_DIR_UPLOADS, filename=self.file_name)
		print("4")
		return send_from_directory(directory=IMAGE_DIR_PROCESSED, filename=self.file_name)


	def delete(self):
		if self.file_name is None:
			return
		if not os.path.isfile(IMAGE_DIR_UPLOADS + self.file_name):
			return
		os.remove(IMAGE_DIR_UPLOADS + self.file_name)

	def delete_processed(self):
		if self.file_name is None:
			return
		if not os.path.isfile(IMAGE_DIR_PROCESSED + self.file_name):
			return
		os.remove(IMAGE_DIR_PROCESSED + self.file_name)
