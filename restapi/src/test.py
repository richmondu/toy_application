from object_detection.util.perf_logger import PerfLogger
from object_detection.model.cfg_file import CfgFile
from object_detection.model.img_file import ImgFile
from object_detection.controller.object_detection_haarcascade import HaarCascadeClassifier
import os



class TestObjectDetection():

	@staticmethod
	def run():
		input_dir = "object_detection/test_images/input/"
		output_dir = "object_detection/test_images/output/"
		config_dir = "object_detection/test_config/"

		cfg = CfgFile(path="cfg_stop.xml", dir=config_dir)

		for root, dirs, files in os.walk(input_dir):
			pass
		for index, file in enumerate(files):
			output = TestObjectDetection._test_image(cfg, file, input_dir, output_dir)
			if output:
				print("[{}] {} -> {}".format(index, file, output.path))
			else:
				print("[{}] {} -> {}".format(index, file, None))
			print()
		print("See {} for output images".format(output_dir))

	@staticmethod
	@PerfLogger.log
	def _test_image(cfg, file, input_dir, output_dir):
		input = ImgFile(path=file, dir=input_dir)
		img_proc = HaarCascadeClassifier(cfg, input, output_dir)
		output = img_proc.process_image()
		return output


def main():
	TestObjectDetection.run()

if __name__ == "__main__":
	main()

