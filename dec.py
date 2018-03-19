#_*_encoding=utf-8_*_
#
def  dec(func):
	def wrap(*args):
		print("start decorator method...")
		r = func(*args)
		print(r)

		return r+" new value"
	return wrap

@dec
def de_func(val):
	return "this is raw string...{}".format(val)
# def dec(*arg):
# 	def pre_func():
# 		def dec_func(func):
# 			print("this is raw func...")
# 			return  func(*arg)
# 		return  dec_func
# 	return pre_func
#
#
# def def_func(val):
# 	print(val)
#
# @dec('hello world')
de_func()

