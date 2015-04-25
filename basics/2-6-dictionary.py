
### Dictionary ###

person = {"name":"David", "height": 182, "weight": 72 }
print person["name"]
person["name"] = "John"
key = "weight"
print person
person[key] += 10
person["age"] = 28
print person
print person["height"], person["age"]
equipment = {"name":"book", "pages":200}
person["stuff"] = equipment	# nesting
print person
print person.keys()     # list of keys
print person.values()	# list of values
print person.items()	# list of tuples (key, value)
print person["stuff"]["name"]

person.has_key("name")
"name" in person        # not clear, perhaps
"name" in person.keys() # more readable
