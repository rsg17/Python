import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--foo', help='foo help', dest='val')
	args = parser.parse_args()
	print args.val