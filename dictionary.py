students = {}
for  i in range(int(input("Enter no of students"))):
	name = input("Enter name: ")
	usn = input("Enter usn: ")
	students[name] = usn
print(students)