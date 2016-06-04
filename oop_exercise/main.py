from triangle import Triangle as Triangle
from square import Square as Square
from shape import Shape as Shape

def main():
	sh = Shape()
	print sh
	t = Triangle(5, 10)
	print t.area()
	print "%s Static Method" % t.static_area(10, 20)

	s = Square(20)
	print s.area()
	print s.perimeter()


if __name__ == "__main__":
	main()
