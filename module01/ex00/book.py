class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		self.name = name#str
		self.last_update = last_update#datetime
		self.creation_date = creation_date#datetime
		self.recipe_list = recipes_list#dict avec 3 key "starter", "lunch", "dessert"

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
