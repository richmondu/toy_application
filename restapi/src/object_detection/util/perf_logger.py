import timeit


class PerfLogger:

	@staticmethod
	def log(func):

		def wrapper(*args, **kwargs):
			start_time = timeit.default_timer()
			val = func(*args, **kwargs)
			print("{:.2f} secs".format(timeit.default_timer() - start_time))
			return val

		wrapper.__name__ = func.__name__
		return wrapper
