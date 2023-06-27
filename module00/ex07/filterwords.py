import sys

def atoi(str):
	res = 0
	for i in range(len(str)):
		res = res * 10 + (ord(str[i]) - ord('0'))
	return res

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("ERROR")
		exit()
	if not sys.argv[2].isdigit():
		print("ERROR")
		exit()
	S = sys.argv[1]
	N = atoi(sys.argv[2])

	lst = S.split()

	punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	i = 0
	while i < len(lst):
		lst[i] = lst[i].strip(punctuations)
		if len(lst[i]) <= N:
			lst.pop(i)
		else:
			i += 1
	
	print(lst)
	