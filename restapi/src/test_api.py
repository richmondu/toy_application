import os
import unittest
from rest_api import app
import rest_api


def get_image_data(file_path, file_name):
	data = {
		'image': (open(file_path + file_name, 'rb'), file_name.split("/")[-1])
	}
	return data

def test_upload_image_api(app, test_url, file_path, file_name):
	api = "/api/v1/objectdetection/image"
	data = get_image_data(file_path, file_name)
	res = app.post(f"{test_url}{api}", data=data)
	return res

def test_download_image_api(app, test_url, file_name, processed=""):
	api = "/api/v1/objectdetection/image/{file_name}{processed}"
	res = app.get(f"{test_url}{api}")
	print(res)
	return res


class ToyApplicationApiTests(unittest.TestCase):

	def setUp(self):
		self.test_url = "http://localhost:8000"
		self.test_images = "object_detection/test_images/input/"
		rest_api.initialize()
		self.app = app.test_client()
		self.app.testing = True 
		
	def tearDown(self):
		pass


	def test_upload01(self):
		res = test_upload_image_api(self.app, self.test_url, self.test_images, "image.jpg")
		self.assertEqual(res.status_code, 200)

	def test_upload02(self):
		res = test_upload_image_api(self.app, self.test_url, self.test_images, "image__fliph.jpg")
		self.assertEqual(res.status_code, 200)

	def test_upload03(self):
		res = test_upload_image_api(self.app, self.test_url, self.test_images, "image__rot180.jpg")
		self.assertEqual(res.status_code, 200)

	#def test_download01(self):
	#	res = test_download_image_api(self.app, self.test_url, "image.jpg")
	#	self.assertEqual(res.status_code, 200)

	#def test_download01_processed(self):
	#	res = test_download_image_api(self.app, self.test_url, "image.jpg", "/processed")
	#	self.assertEqual(res.status_code, 200)


def main():
	#unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(ToyApplicationApiTests)
	unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
	main()