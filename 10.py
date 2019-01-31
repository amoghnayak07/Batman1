n = int(input("Enter no of students"))
c = {}
d = {}
for i in range(n):
	name = input("Enter name:")
	usn = input("Enter the reg num")
	c.update({name:usn})
print(c)
	