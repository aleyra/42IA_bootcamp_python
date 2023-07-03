import random
def generator(text, sep=" ", option=None):
	'''Splits the text according to sep value and yield the substrings.
option precise if a action is performed to the substrings before it is yielded.
'''
	if not sep.isprintable() or not isinstance(text, str):
		print("ERROR")
		return 
	
	split = text.split(sep)

	if option == "shuffle":
		split = random.sample(split, len(split))
	elif option == "unique":
		# split = list(set(split)) #bizarre ça met dans un ordre aleatoire
		res = []
		for i in split:
			if i not in res:
				res.append(i)
		split = res
	elif option == "ordered":
		split.sort()

	for i in range(len(split)):
		yield split[i]

if __name__ == "__main__":
	txt = "Le Lorem Ipsum est simplement du faux texte."
	s = " "
	for word in generator(txt, sep=s, option="ordered"):
		print(word)