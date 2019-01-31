import csv
with open('Amogh.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
          print(', '.join(row))