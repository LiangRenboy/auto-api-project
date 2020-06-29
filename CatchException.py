import functools
import time

def catch_except(max_retries=5,validate=None):
	def decorator(func):
		functools.wraps(func)
		def wrappers(*args, **kwargs):
			i = 0
			while i < max_retries:
				try:
					result = func(*args, **kwargs)
					if callable(validate) and validate(result) is False:
						print(i+1)
						continue
					else:
						return result

				except Exception as e:
					print('[%s]: %s' % (func.__name__,e))

				finally:
					i += 1
					print(i)
					time.sleep(i)
		return wrappers
	return decorator


@catch_except()
def testdemo():
	print(123 + "123")

testdemo()
# a = False
# b = testdemo()

# if callable(a) and a(b) is False:
# 	print("111")
# else:
# 	print("222")