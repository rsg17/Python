import sys

vowel = ['a','e', 'i', 'o', 'u']

def reverse_sentence(input_sentence):
	output_sentence = ''
	length = len(input_sentence)
	for i in range(0,length):
		output_sentence += input_sentence[length - i - 1]
	return output_sentence


def reverse_word(input_sentence):
	output_sentence = []
	words = input_sentence.split()
	for i in words:
		output_sentence.append(reverse_sentence(i))
	return " ".join(output_sentence)

def reverse_wo_word(input_sentence):
	output_sentence = []
	words = input_sentence.split(" ")
	l = len(words)
	for i in range(0,l):
		output_sentence.append(words[l-i-1])
	return " ".join(output_sentence)	

	
def square(x):
	return x * x

def eliminate_odds(x):
	return x % 2 == 0

def add(x, y):
	return x + y

def get_vowels(x):
	return x in vowel


def vowel_count(x):
	pass


if __name__ == "__main__":
	"""
	# print "%sfoo" % reverse_wo_word(sys.argv[1])
	print map(square, range(0, 9))
	print filter(eliminate_odds, range(0,9))
	print reduce(add, range(0,9))


	sentence = 'These are not vowels'
	print sentence
	print filter(eliminate_vowels, sentence)

	boolval = eliminate_vowels('a')
	print not boolval
	"""
	sentence = 'These are not vowels'
	print sentence
	vowel_dict = dict()
	for i in vowel:
		vowel_dict[i] = 0
#	print vowel_dict

	vowels_sentence = filter(get_vowels, sentence)

	for i in vowels_sentence:
		vowel_dict[i] += 1

	print(vowel_dict)

	del vowel_dict['o']
	print vowel_dict.keys()


