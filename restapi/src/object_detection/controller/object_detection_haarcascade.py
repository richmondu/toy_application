import cv2
from object_detection.model.cfg_file import CfgFile
from object_detection.model.img_file import ImgFile
from object_detection.controller.object_detection_interface import IObjectDetection


class HaarCascadeClassifier(IObjectDetection):

	def __init__(self, cfg: CfgFile, img: ImgFile, output_dir: str):
		self.img = img
		self.cfg = cfg
		self.output_dir = output_dir
		self.min_size = (20, 20)

	def process_image(self):
		try:
			img = cv2.imread(self.img.dir + self.img.path)
			classification = self._apply_classification()
			detection = self._detect_bounds(img, classification)
			return self._apply_bounds(img, detection)
		except Exception as e:
			print(e)
			return None


	def _apply_classification(self):
		return cv2.CascadeClassifier(self.cfg.dir + self.cfg.path) 

	def _detect_bounds(self, img, classification):
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
		return classification.detectMultiScale(img_gray, minSize=self.min_size) 

	def _apply_bounds(self, img, detection):
		amount_found = len(detection) 
		if amount_found != 0: 
			for (x, y, width, height) in detection: 
				new_img = cv2.rectangle(img, (x, y), (x + height, y + width), (0, 255, 0), 5) 
			output = self.output_dir + self.img.path
			cv2.imwrite(output, new_img)
			return ImgFile(path=self.img.path, dir=self.output_dir)
		return None
