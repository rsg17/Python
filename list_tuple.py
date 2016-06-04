import sys

def merge_pair_list(list1,list2):
	l1 = len(list1)
	l2 = len(list2)
	op = []

	if l1 != l2:
		print "Lists not of equal length"
		sys.exit(1)
	
	for i in range(0,l1):
		y = (list1[i],list2[i])
		op.append(y)

	return op



if __name__ == "__main__":
	input1 = ["apple", "banana", ""]
	input2 = ["red", "yellow"]
	
	# print merge_pair_list(input1,input2)
	for x,y in zip(input2, input1):
		print "%s : %s" % (x, y)