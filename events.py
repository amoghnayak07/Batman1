import csv
c = {}
def add():
	name = input("Enter name: ")
	print("Optios: 1.CS\n2.Google it\n3.Treasure hunt")
	choice = int(input("Enter Choice: "))
	if choice == 1:
		d = {name:'CS'}
		c.update(d)
	elif choice == 2:
		d = {name:'Google'}
		c.update(d)

	elif choice == 3:
		d = {name:'Treasure'}
		c.update(d)

	with open ('9.csv', 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile)
		spamwriter.writerow(c)
def see():
	with open('9', newline='\n') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			print(','.join(row))

