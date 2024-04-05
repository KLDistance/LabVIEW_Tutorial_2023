class OBJ:
	num = 0
	def __init__(self):
		pass
	def increment(self, input_var):
		self.num += input_var
		return self.num

def init_obj():
	obj = OBJ()
	return obj

def incr_obj(obj, incr_num):
	obj.increment(incr_num)
	return obj.num

if __name__ == '__main__':
	obj = OBJ()
	ret = obj.increment(4)
	print(ret)
	ret2 = obj.increment(8)
	print(ret2)