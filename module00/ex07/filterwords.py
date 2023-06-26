import sys

def atoi(str):
	res = 0
	for i in range(len(str)):
		res = res * 10 + (ord(str[i]) - ord('0'))
	return res

def haspuncMark(str):
	for i in [0, len(str) - 1]:
		if str[i] == ',' or str[i] == '?' or str[i] == ';' or str[i] == '.' or str[i] == ':' or str[i] == '!':
			return True
	return False 

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("ERROR")
		exit()
	if not sys.argv[2].isdigit():
		print("ERROR")
		exit()
	S = sys.argv[1]
	N = atoi(sys.argv[2])

	list = S.split()

	for x in list:
		if haspuncMark(x):
			list.remove(x)

	print(list)
	print(len(list))

	# for x in list:
	# 	print(len(x))
	# 	if len(x) < N:
	# 		list.remove(x)
	
	print(list)
	to_print = """S = {}
N = {}"""
	print(to_print.format(S, N))