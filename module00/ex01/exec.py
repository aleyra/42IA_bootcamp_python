import sys

# if __name__ == "__main__":
#     print(f"Arguments count: {len(sys.argv)}")
#     for i, arg in enumerate(sys.argv):
#         print(f"Argument {i:>6}: {arg}")
if len(sys.argv) > 1:
	sys.argv.reverse()
	sys.argv.pop()
	str = ""
	for i, arg in enumerate(sys.argv):
		# changer la case
		# reverse la string
		str = str + sys.argv[i] + " "
	# supprimer le dernier espace
	print(str)
	