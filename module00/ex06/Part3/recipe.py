Sandwich = {
    'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
	'meal' : 'lunch',
	'prep_time' : 10
}

Cake = {
    'ingredients' : ["flour", "sugar", "eggs"],
	'meal' : "dessert",
	'prep_time' : 60
}

Salad = {
    'ingredients' : ["avocado", "arugula", "tomatoes", "spinach"],
	'meal' : "lunch",
	'prep_time' : 15
}

cookbook = {
    'Sandwich' : Sandwich,
    'Cake' : Cake,
    'Salad' : Salad
}

def print_recipe_names():
	for x in cookbook:
		print(x)

def print_recipe_details(str):
	recipe_details = cookbook.get(str, "oups")
	if recipe_details != "oups":
		# for y in recipe_details:
		# 	print(y, ':', recipe_details[y])
		to_print = """Recipe for {}
	Ingredients list: {}
	To be eaten for {}
	Takes {} minutes of cooking"""
		print(to_print.format(str, recipe_details['ingredients'], recipe_details['meal'], recipe_details['prep_time']))
	else:
		print("This recipe does not exist")

def delete_recipe(str):
	if cookbook.get(str, "oups") == "oups":
		print("This recipe does not exist")
	else:
		cookbook.pop(str)
		print_recipe_names()

def	add_recipe():
	name = input(">>> Enter a name:\n")
	while name == "" or cookbook.get(name, "oups") != "oups":
		name = input(">>> Enter a name:\n")
	ingredients = []
	print(">>> Enter ingredients:")
	one = "start"
	while one != "":
		one = input()
		ingredients.append(one)
	ingredients.pop()
	meal = input(">>> Enter a meal type:\n")
	time = input(">>> Enter a preparation time in minutes:\n")
	while not time.isdigit():
		time = input(">>> Your times must be an positive integer\n")
	cookbook.update(
		{name : {
			'ingredients' : ingredients,
			'meal' : meal,
			'prep_time' : time
		}}
	)

if __name__ == "__main__":
	print("""Welcome to the Python Cookbook !
	List of available option:
		1: Add a recipe
		2: Delete a recipe
		3: Print a recipe
		4: Print the list of recipes
		5: Quit""")

	option = "0"
	while 1:
		option = input("\nPlease select an option:\n>> ")
		if option == "5":
			print("\nCookbook closed. Goodbye !")
			exit()
		if option == "1":
			add_recipe()
		else:
			if option == "2":
				recipe = input("\nEnter a recipe name you wish to delete\n>> ")
				delete_recipe(recipe)
			else:
				if option == "3":
					recipe = input("\nEnter a name of recipe you wish to print\n>> ")
					print_recipe_details(recipe)
				else:
					if option == "4":
						print("\nList of recipe available:")
						print_recipe_names()
					else:
						print("""
	Sorry, this option does not exist.
	List of available option:
		1: Add a recipe
		2: Delete a recipe
		3: Print a recipe
		4: Print the list of recipes
		5: Quit""")