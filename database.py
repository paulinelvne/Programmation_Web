import json

def get_cocktails():
	""" Reads the database file data.json containing the list of our cocktails with their corresponding recipes.
	 	Returns the list of the cocktails. Each cocktail is a python dictionary.
	"""
	jsonFile = open("./data.json")
	jsonString = jsonFile.read()
	cocktails = json.loads(jsonString)
	return cocktails



def get_cocktail_id(c, requested_id):
	""" Selects a cocktail using its id.

		Parameters :
			- 'c' is a list of dictionnaries. Each dictionnary corresponding to a cocktail.
			- 'requested_id' : integer. The id of the coktail we want.

	 	Returns the cocktail dictionary with the requested id.
			"cocktail" parameter is a dictionary with the following values:
	        'name', 'cout', 'difficulte', 'type', 'image' are strings.
			'ingredients', 'quantities', 'preparation' are lists of strings.
	        'id' is an integer.
	"""

	cocktails = c

	for cocktail in cocktails:
		if cocktail["id"] == int(requested_id):
			return cocktail



def get_cocktail_name(c, requested_name):
	""" Get cocktails which names match with at least sequence of the requested name.

		Parameters :
			- 'c' is a list of dictionnaries. Each dictionnary corresponding to a cocktail.
			- 'requested_name' : string. The pattern that we look for in the cocktails' name.

	 	Returns a list with the cocktails containing the pattern in their names.
	"""
	cocktails = c
	c =[]

	for cocktail in cocktails:
		if requested_name.casefold() in cocktail["name"].casefold():
			c.append(cocktail)
	return c



def get_cocktail_ingredient(c, requested_ingredient):
	""" Get cocktails which ingredients match with at least sequence of the requested ingredient.

		Parameters :
			- 'c' is a list of dictionnaries. Each dictionnary corresponding to a cocktail.
			- 'requested_ingredient' : string. The pattern that we look for in the cocktails' ingredients.

	 	Returns a list with the cocktails containing the pattern in their ingredients.
	"""
	cocktails = c
	c = []

	for cocktail in cocktails:
		for ing in cocktail["ingredients"]:
			if requested_ingredient.casefold() in ing.casefold():
				c.append(cocktail)

	return c



def write_json(new_data, filename='data.json'):
	""" Add content to json file.

		Parameters :
			- 'new_data' is a dictionnary that corresponds to a cocktail.
			- 'file_name' : string. The json file where the new information is written.

		Returns None
	"""
	with open(filename,'r+') as file:
		file_data = json.load(file)
		file_data.append(new_data)
		file.seek(0)
		json.dump(file_data, file, indent=2)



def delete_cocktail(cocktail_id):
	""" Deletes cocktail from json file 'data.json'.

		Parameters :
			- 'cocktail_id': integer. The id of the cocktail to be deleted.

	 	Returns None
	"""
	obj = json.load(open("data.json"))

	for i in range(len(obj)):
		if obj[i]["id"]==int(cocktail_id):
			obj.pop(i)
			break
	# Output the updated file with pretty JSON
	open("data.json", "w").write(json.dumps(obj, sort_keys=True, indent=2, separators=(',', ': ')))


def reset_data():
	""" Resets the 'data.json' file to match the 'reset_data.json' so as to not loose certain cocktails.

		Returns None
	"""
	with open("reset_data.json", "r") as original:
		with open("data.json", "w") as to_be_reseted:
			original_file = original.read()
			to_be_reseted.write(original_file)
