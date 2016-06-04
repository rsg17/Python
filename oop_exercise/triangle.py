from shape import Shape as Shape


class Triangle(Shape):
	def __init__(self, base, height):
		self.base = base
		self.height = height

	def area(self):
		return self.base * self.height / 2

	@staticmethod
	def static_area(base, height):
		return base * height / 2
