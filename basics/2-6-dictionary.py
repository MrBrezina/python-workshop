
### Dictionary ###

person = { "name":"David", "height": 182, "weight": 72 }
person["name"]
person["name"] = "John"
key = "weight"
person
person[key] += 10
person["age"] = 28
person
equipment = {"name":"book", "pages":200}
person["stuff"] = equipment	# nesting
person
person.keys()	# list of keys
person.values()	# list of values
person.items()	# list of tuples (key, value)
person.has_key("name")
"name" in person # better
"name" in person.keys() # more readable
