from abc import abstractmethod, ABC


class IObjectDetection(ABC):

	@abstractmethod
	def process_image(self):
		raise NotImplementedError

	@abstractmethod
	def _apply_classification(self):
		raise NotImplementedError

	@abstractmethod
	def _detect_bounds(self, img, classification):
		raise NotImplementedError

	@abstractmethod
	def _apply_bounds(self, img, detection):
		raise NotImplementedError