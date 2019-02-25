n = int(input("Enter number of members needed in the list: "))
a = []
for i in range(n):
	a.append(int(input("Enter members of list: ")))



string = input("Enter any string value: ")



b = []
for j in a:
	c = string + str(j)
	b.append(c)
print(b)