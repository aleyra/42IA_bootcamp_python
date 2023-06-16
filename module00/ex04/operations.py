import sys

def atoi(str):
	res = 0
	for i in range(len(str)):
		res = res * 10 + (ord(str[i]) - ord('0'))
	return res

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("""Usage: python operations.py <number1> <number2>
Example:
python operations.py 10 3""")
		exit()
	if len(sys.argv) > 3:
		print("AssertionError: too many arguments")
		exit()
	if sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
		print("AssertionError: only integers")
		exit()
	a = atoi(sys.argv[1])
	b = atoi(sys.argv[2])
	sum = a + b
	diff = a - b
	prod = a * b
	res1 = """Sum:		{}
Difference:	{}
Product:	{}"""
	print(res1.format(sum, diff, prod))
	if b != 0:
		div = a / b
		rem = a % b
		res2 = """Quotient:	{}
Remainder:	{}"""
		print(res2.format(div, rem))
	else:
		print("""Quotient:	ERROR (division by zero)
Remainder:	ERROR (modulo by zero)""")