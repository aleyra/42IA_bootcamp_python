def what_are_the_vars(*args, **kwargs):
	lst = []
	for i in range(len(args)):
		lst.append(args[i])
	d = dict()
	for key, value in kwargs.items():
		d.update({key : value})
	return ObjectC(lst, d)

class ObjectC(object):
	def __init__(self, lst, d):
		dico = dict()
		isOk = True
		for i in range(len(lst)):
			attr_name = "var_" + str(i)
			dico.update({attr_name : lst[i]})
		for key, value in d.items():
			if key in dico.keys():
				isOk = False
			else:
				dico.update({key : value})
		if isOk == True:
			self.__dict__ = dico
		else:
			return None#echec.... Comment faire pour que obj is None renvoie true ?

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	# obj = what_are_the_vars(7)
	# doom_printer(obj)
	# obj = what_are_the_vars(None, [])
	# doom_printer(obj)
	# obj = what_are_the_vars("ft_lol", "Hi")
	# doom_printer(obj)
	# obj = what_are_the_vars()
	# doom_printer(obj)
	# obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	# doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
	# obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	# doom_printer(obj)