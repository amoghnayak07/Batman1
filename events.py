import csv
c = []
def add():
	name = input("Enter name: ")
	print("Optios: 1.CS\n2.Google it\n3.Treasure hunt")
	cho = int(input("Enter Choice: "))
	if cho == 1:
		d = [name, 'CS']
		c.extend(d)

		
	elif cho == 2:
		d = [name, 'Google it']
		c.extend(d)		

	elif cho == 3:
		d = [name, 'Treasure hunt']
		c.extend(d)		

	with open ('16.csv','a',newline='\n') as csvfile:
		spamwriter = csv.writer(csvfile)
		spamwriter.writerow(c)

def see():
	with open('16.csv', newline='\n') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			print(','.join(row))

