import sys

def atoi(str):
	res = 0
	for i in range(len(str)):
		res = res * 10 + (ord(str[i]) - ord('0'))
	return res

if len(sys.argv) != 3:
    print("ERROR")
    exit()
if not sys.argv[2].isdigit():
    print("ERROR")
    exit()
