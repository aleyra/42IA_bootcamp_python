import sys

def atoi(str):
	res = 0
	for i in range(len(str)):
		res = res * 10 + (ord(str[i]) - ord('0'))
	return res

if len(sys.argv) > 2:
	print("Error: give only 1 argument which must be an integer")
	exit()
if len(sys.argv) == 2:
	if sys.argv[1].isdigit() != True:
		print("Error: you're argument is not an integer")
		exit()
	i = atoi(sys.argv[1])
	if i == 0:
		print("I'm Zero")
	else:
		if i % 2 == 0:
			print("I'm Even")
		else:
			print("I'm Odd")