import datetime
from book import Book
from recipe import Recipe

if __name__ == "__main__":
	name = "test"
	cookinglvl = 1
	cookingtime = 1
	ingredients = ["test", "test"]
	descriptions = ""
	recipetype = "lunch"
	test = Recipe(name, cookinglvl, cookingtime, ingredients, descriptions, recipetype)
	# print(str(test))

	nameb = "Test"
	lastupdate = datetime.datetime.now()
	creationdate = datetime.datetime(2023, 6, 28)
	recipelst = {test.recipe_type:test}

	test2 = Book(nameb, lastupdate, creationdate, recipelst)

	# test2.get_recipe_by_name("test")
	# test2.get_recipes_by_types('lunch')
	test3 = Recipe("bouh", 2, 2, ["air","kuuki"], "", 'starter')
	# print(test3)
	test2.add_recipe(test3)
	test2.get_recipes_by_types('starter')