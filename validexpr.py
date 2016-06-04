import sys


brackets = dict()
brackets[')'] = '('
brackets['}'] = '{'
brackets[']'] = '['
open_brackets = ['(', '{', '[']

def validate_expr(input_expr):
	comparelist = []
	cnt = 1
	for char in input_expr:
		if char in open_brackets:
			comparelist.append(char)
		elif char in brackets.keys():
			try:
				prevbracket = comparelist.pop()
			except IndexError as e:
				print "Error: Got closing bracket %s without opening bracket at position %s" % (char, cnt)
				raise e

			if brackets[char] != prevbracket:
				print "Error: Got %s; Popped : %s; Position: %s" % (char, prevbracket, cnt)
				sys.exit(1)
		cnt += 1

	if len(comparelist) != 0:
		print "Error: Missing closing brackets for %s opening brackets" % comparelist
		sys.exit(1)

	print "Valid Expression"


def main():
	#expr = "[(2+3) - {5-4}]"
	expr = "}"
	print expr
	validate_expr(expr)




if __name__ == "__main__":
	main()

