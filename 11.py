import csv
c = []
def add():
	name = input("Enter name: ")
	print("Optios: 1.CS\n2.Google it\n3.Treasure hunt")
	choice = int(input("Enter Chice: "))
	if choice == 1:
		c[0:] = [name, 'CS']
	elif choice == 2:
		c[0:] = [name, 'Google it']
	elif choice == 3:
		c[0:] = [name, 'Treasure Hunt']
	with open ('New', 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile)
		spamwriter.writerow(c)
def see():
	with open('New', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			print(','.join(row))

