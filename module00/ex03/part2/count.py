import sys

def ispuncMark(c):
	if c == ',' or c == '?' or c == ';' or c == '.' or c == ':' or c == '!':
		return True
	else:
		return False 

def text_analyzer(*str):
	upperChar = 0
	lowerChar = 0
	puncChar = 0
	spaceChar = 0
	if len(str) == 0:
		txt = input("What is the text to analyze?\n")
	else:
		txt = str[0]
	for i in range(0, len(txt)):
		if txt[i].isupper():
			upperChar += 1
		if txt[i].islower():
			lowerChar += 1
		if ispuncMark(txt[i]):
			puncChar += 1
		if txt[i] == ' ':
			spaceChar += 1
	if upperChar == 0 and lowerChar == 0 and puncChar == 0 and spaceChar == 0:
		print("AssertionError: argument is not a string")
	else:
		res = """- {} upper letter(s)
- {} lower letter(s)
- {} punctuation mark(s)
- {} space(s)"""
		print(res.format(upperChar, lowerChar, puncChar, spaceChar))

if __name__ == "__main__":
	if len(sys.argv) == 1:
		text_analyzer()
	else:
		if len(sys.argv) == 2:
			text_analyzer(sys.argv[1])
		else:
			print("Too many arg, only 0 or 1 needed")