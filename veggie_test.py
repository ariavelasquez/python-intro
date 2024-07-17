# Create an empty list named favorite_vegetables.
favorite_vegetables = []

# Create an empty list named gross_vegetables.
gross_vegetables = []

# Create a third list named vegetables and fill it with 8 vegetables.
vegetables = ["corn", "potatoes", "beets", "lima beans", "spinach", "green beans", "zucchini", "vidalia onions"]

# Now iterate through the list called vegetables.
for x in vegetables:

	# Add the vegetable to the favroites list IF it is a potato.
	if x == "potatoes":
		favorite_vegetables.append(x)
	# If the vegetable is NOT a potato, add it to the gross_vegetables list.
	else:
		gross_vegetables.append(x)

# At the end, print out the list favorite_vegetables.
print(favorite_vegetables)

# Then print out the list gross_vegetables.
print(gross_vegetables)

# ANOTHER SOLUTION:
# 		favorite_vegetables = favorite_vegetables + [x]
# 	else:
# 		gross_vegetables = gross_vegetables + [x]

# print("Favorite Vegetables:",favorite_vegetables)
# print("Gross Vegetables:",gross_vegetables)