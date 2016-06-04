

def sort_desc(num_list):
	l = len(num_list)
	for i in range(0, l):
		for j in range(i, l):
			if num_list[i] < num_list[j]:
				k = num_list[j]
				num_list[j] = num_list[i]
				num_list[i] = k			


def main():
	x = [23, 56, 89, 78, 76, 55]
	sort_desc(x)
	print x


if __name__ == "__main__":
	main()