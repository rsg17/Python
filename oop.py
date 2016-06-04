class MyClass(object):
	__slots__ = ["a"]
	
	def __init__(self, val):
		self.a = val

	def __str__(self):
		return "This is MyClass"

	def increment_a(self, val):
		self.a += val

	@staticmethod
	def class_level_method(rachana):
		return rachana

if __name__ == "__main__":
	myobject = MyClass(5)
	print myobject
	myobject.increment_a(5)
	print myobject.a
	myobject.b = 5
	print myobject.b

	print "%s" % "="*10
	myobject1 = MyClass(5)
	print myobject1.a
	print myobject1.b