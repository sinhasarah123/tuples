print("type yes or no for the following questions in order to recommend hobbies")
creative = input("Do you enjoy being creative:")
colors = input("Do you like working with colors:")
outdoors = input("Do you love spending time outdoors:")
plants = input("Do you enjoy nurturing plants:")
books = input("Do you like escaping into different worlds through books:")
ideas = input("Do you find joy in exploring new ideas through reading:")
if creative == "yes" and colors == "yes":
	print("recommended hobby is Painting")
if outdoors == "yes" and plants == "yes":
	print("recommended hobby is Gardening")
if books == "yes" and ideas == "yes":
	print("recommended hobby is Reading")