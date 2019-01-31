import csv
with open('Amogh3.csv', 'w', newline='\n') as csvfile:
	spamwriter = csv.writer(csvfile)
	spamwriter.writerow(['spam'] + ['Boo'])
	spamwriter.writerow(['Alloo'])
