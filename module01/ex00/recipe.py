class Recipe:#faut gerer les erreurs
	def __init__(self, name, cooking_lvl, cooking_time,
					ingredients, descriptions, recipe_type):
		self.name = name#str()
		self.cooking_lvl = cooking_lvl#int()#[1;5]
		self.cooking_time = cooking_time#int()#in min
		self.ingredients = ingredients#[]
		self.description = descriptions#str()
		self.recipe_type = recipe_type#str()

	def __str__(self):
		"""Return the string to print with the recipe info"""
		to_print = ""
		#comment tu veux print
		return to_print