class Recipe:#faut gerer les erreurs
	def __init__(self, name, cooking_lvl, cooking_time,
					ingredients, descriptions, recipe_type):
		#checks
		isNameStr = isinstance(name, str)
		assert isNameStr, "The name must be a string"
		assert name != "", "The name must not be empty"
		isCookingLvlInt = isinstance(cooking_lvl, int)
		assert isCookingLvlInt, "The lvl of cooking must be an int between 1 and 5"
		assert 0 < cooking_lvl < 6, "The lvl of cooking must be an int between 1 and 5"
		isCookingTimeInt = isinstance(cooking_time, int)
		assert isCookingTimeInt, "The time of cooking must be a positive integer"
		assert cooking_time > 0, "The time of cooking must be a positive integer representing the time in minutes"
		isIngredientsLstStr = isinstance(ingredients, list)
		assert isIngredientsLstStr, "The list of ingredients must be a list of string"
		for i in range(len(ingredients)):
			assert isinstance(ingredients[i], str), "The list of ingredients must contained only strings"
		isDescriptionStr = isinstance(descriptions, str)
		assert isDescriptionStr, "The descriptions must be a string"
		isRecipeTypeStr = isinstance(recipe_type, str)
		assert isRecipeTypeStr, 'The type of the recipe must be "starter", "lunch" or "dessert"'
		# assert recipe_type == "lunch" or recipe_type == "starter" or recipe_type == "lunch", 'The type of the recipe must be "starter", "lunch" or "dessert"
		isRecipeTypeOk = False
		if (recipe_type == "lunch" or recipe_type == "starter"
			or recipe_type == "dessert"):
			isRecipeTypeOk = True
		assert isRecipeTypeOk, 'The type of the recipe must be "starter", "lunch" or "dessert"'

		#init
		self.name = name#str()
		self.cooking_lvl = cooking_lvl#int()#[1;5]
		self.cooking_time = cooking_time#int()#in min
		self.ingredients = ingredients#[]
		self.description = descriptions#str()
		self.recipe_type = recipe_type#str()

	def __str__(self):
		"""Return the string to print with the recipe info"""
		to_print = f"""{self.name}
	cooking's lvl: {self.cooking_lvl}
	type of recipe: {self.recipe_type}
	time of cooking: {self.cooking_time}
	ingredients: {self.ingredients}
	description: {self.description}"""
		return to_print