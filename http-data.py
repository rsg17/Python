import requests
import html2text
from collections import Counter
import argparse
import re


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--url', help='Enter URL', dest='u')
	args = parser.parse_args()
	print args.u
	r = requests.get(args.u);
	print r.status_code
	htmltext = r.content
	plaintext = html2text.html2text(htmltext)
	words = plaintext.split()
	counts = Counter(words)
#	print counts
	f = open('workfile', 'w')
	f.write(str(counts))

	lines = plaintext.splitlines()

	k = []
	v = []

#	a, b = re.split('\W+',lines[1],1)
#	print a
#	print b
	
	for i in range(0,len(lines)):
		test = 1
		try:
			s = lines[i].lstrip()
			a, b = re.split(r'\t+',s,1)
		except ValueError:
			test = 0

		if test == 1:
			k.append(a)
			v.append(b)
	


		
		
			


