def generator(text, sep=" ", option=None):
	'''Splits the text according to sep value and yield the substrings.
option precise if a action is performed to the substrings before it is yielded.
'''
	if not sep.isprintable() or not isinstance(text, str):
		print("ERROR")
		return 
	
	split = text.split(sep)

	# match option:
	# 	case "shuffle":
	# 		print("shuffles the list of words")
	# 	case "unique":
	# 		print ("returns a list where each word appears only once")
	# 	case "ordered":
	# 		print ("alphabetically sorts the words")

	for i in range(len(split)):
		yield i

if __name__ == "__main__":
	text = "1.1"
	sep = "."
	for word in generator(text, sep):
		print(word)