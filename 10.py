import csv
n = int(input("Enter no of students"))
c = []
d = []
for i in range(n):
	name = input("Enter name:")
	usn = input("Enter the reg num")
	d = [name, usn]
	c.extend(d)
print(c)
with open('register5.csv', 'a', newline='\n') as csvfile:
	spamwriter = csv.writer(csvfile)

	spamwriter.writerow(c)
	