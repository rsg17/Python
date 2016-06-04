class Shape(object):
	def perimeter(self):
		raise NotImplementedError()

	def area(self):
		raise NotImplementedError()


class Triangle(Shape):
	def __init__(self, base, height):
		self.base = base
		self.height = height

	def area(self):
		return self.base*self.height/2

	@staticmethod
	def static_area(base, height):
		return base*height/2

class Square(Shape):
	def __init__(self, side):
		self.side = side

	def area(self):
		return self.side*self.side

	def perimeter(self):
		return 4*self.side


def main():
	t = Triangle(5, 10)
	print t.area()
	print "%s Static Method" % t.static_area(10,20)

	s = Square(20)
	print s.area()
	print s.perimeter()


if __name__ == "__main__":
	main()
