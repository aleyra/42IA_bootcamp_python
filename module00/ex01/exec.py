import sys

if len(sys.argv) > 1:
	sys.argv.reverse()
	str = ""
	for i in range(0, len(sys.argv) - 1):
		t = sys.argv[i] [::-1]
		str = str + t.swapcase()
		if i != len(sys.argv) - 2:
			str = str + " "
	print(str)