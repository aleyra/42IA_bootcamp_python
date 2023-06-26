kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

to_print = """Python was created by {}
Ruby was created by {}
PHP was created by {}"""

print(to_print.format(kata['Python'], kata['Ruby'], kata['PHP']))