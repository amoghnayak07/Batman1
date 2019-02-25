def add_string_to_list(a):
	mylist.append(a)
	return mylist


x = int(input("Emter number of strings to be added: "))
mylist = []


for i in range(x):
	a = input("Enter string: ")
	b = add_string_to_list(a)


print(b)
