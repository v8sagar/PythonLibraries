import csv

with open("CSVfile.csv") as csvFile:
	readCSV = csv.reader(csvFile,delimiter=",")

	for data in readCSV :
		print(data)