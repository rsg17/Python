import requests
import html2text
from collections import Counter


if __name__ == "__main__":
	r = requests.get("http://genomics-pubs.princeton.edu/oncology/affydata/names.html");
	print r.status_code
	htmltext = r.content
	plaintext = html2text.html2text(htmltext)
	

#	f = open('workfile', 'w')
#	f.write(plaintext)

	words = plaintext.split()
	counts = Counter(words)
	print counts