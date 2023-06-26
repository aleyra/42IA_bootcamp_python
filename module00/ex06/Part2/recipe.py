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
	#version moche mais easy
	# cookbook_recipe_names = cookbook.keys()
	# print(cookbook_recipe_names)
	#version mieux pour les yeux
	for x in cookbook:
		print(x)
		# for y in cookbook[x]:
		# 	print("\t", y, ':', cookbook[x][y])

# print_recipe_names()

def print_recipe_details(str):
	recipe_details = cookbook.get(str, "oups")
	if recipe_details != "oups":
		for y in recipe_details:
			print(y, ':', recipe_details[y])

# print(cookbook.get("bouh"))
print_recipe_details("Cake")

def delete_recipe(str):
	cookbook.pop(str)
	print_recipe_names()
    
# delete_recipe("Cake")

def	add_recipe():
	name = input(">>> Enter a name:\n")
	ingredients = []
	print(">>> Enter ingredients:")
	one = "start"
	while one != "":
		one = input()
		ingredients.append(one)
	ingredients.pop()
	# print(ingredients)
	meal = input(">>> Enter a meal type:\n")
	time = input(">>> Enter a preparation time in minutes:\n")
	while not time.isdigit():
		time = input(">>> Your times mus be an positive integer\n")
	cookbook.update(
		{name : {
			'ingredients' : ingredients,
			'meal' : meal,
			'prep_time' : time
		}}
	)
	
# add_recipe()
# print_recipe_details("bouh")