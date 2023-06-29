import datetime
from recipe import Recipe
class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		#checks
		isNameStr = isinstance(name, str)
		assert isNameStr, "The name must be a string"
		isLastUpdateDatetime = isinstance(last_update, datetime.datetime)
		assert isLastUpdateDatetime, "The last update is not a datetime"
		isCreationDateDatetime = isinstance(creation_date, datetime.datetime)
		assert isCreationDateDatetime, "The creation date is not a datetime"
		isRecipeListDict = isinstance(recipes_list, dict)
		assert isRecipeListDict, "This is not a dict"
		for key, value in recipes_list.items():
			assert isinstance(value, Recipe), "This is not a Recipe"
			assert isinstance(key, str), "This is not a string"
			isRecipeTypeOk = False
			if (key == "lunch" or key == "starter"
				or key == "dessert"):
				isRecipeTypeOk = True
			assert isRecipeTypeOk, 'This is not a "lunch", a "starter" or a "dessert"'

		#init
		self.name = name#str
		self.last_update = last_update#datetime
		self.creation_date = creation_date#datetime
		self.recipe_list = recipes_list#dict avec 3 key "starter", "lunch", "dessert"

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		assert isinstance(name, str), "the name must be a string"
		for key in self.recipe_list.keys():
			if (self.recipe_list[key].name == name):
				print(self.recipe_list[key])
				break

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		assert isinstance(recipe_type, str), "the recipe type must be a string"
		isRecipeTypeOk = False
		if (recipe_type == "lunch" or recipe_type == "starter"
			or recipe_type == "dessert"):
			isRecipeTypeOk = True
		assert isRecipeTypeOk, 'The recipe type must be "lunch", "starter" or "dessert"'
		for key in self.recipe_list.keys():
			if key == recipe_type:
				print(self.recipe_list[key].name)

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		self.recipe_list.update({recipe.recipe_type:recipe})
		self.last_update = datetime.datetime.now()
