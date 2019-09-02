
 # ============================================================================
 # Name        : ferry_delays.py
 # Author      : Nicholas Roethel
 # Description : A program which takes the bc ferries .csv departure time files
 # from 2017 and calculates the average delay over the month
 # ============================================================================



import csv
import sys
import math
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument("dataset.csv",nargs="+") #adds optional arguments
args = parser.parse_args()

def check_for_months(monthlist, flatargs):	 #Checks which month is in each file
	for file in flatargs:
		with open(file, newline='') as csvfile:
			reader = csv.reader(csvfile)
			next(reader)
			data = tuple(reader)
			tup = (file, int(data[0][4])) #checks in month colum
			monthlist.append(tup)


def csv_reader (csvfile,mon,destination): #reads file, does the math and prints
	reader = csv.reader(csvfile)
	next(reader)
	data = [tuple(line) for line in reader]
	count = 0
	delay = []
	for element in data:
		if element[0] == destination:
			if element[5] == element[10]:
				delay.append( (int(element[11])+(int(element[12])/60))-(int(element[6])+(int(element[7])/60)))
	size = len(delay)
	total = sum(delay)
	final = (total/size)*60
	destination = destination + ":"
	print(":RESULTS")
	print(destination)
	print("    Average delay for {}: {:.2f}".format(mon,final))
	print("END")

def main(): #main function 
	csv_path = None
	mon = None
	month = None
	destination = None
	month  = 15
	arglist = []
	arglist = vars(args)
	arglist = list(arglist.values())
	flatlist = []
	flatargs = [item for sublist in arglist for item in sublist] #puts arguments in a list
	monthlist = []
	check_for_months(monthlist,flatargs)

	while(month != "q" and destination != "q"): #loop looking for q

		month = None
		destination = None
		month = 15
		mon = None

		while(str('t')!= str(destination) and str('s')!= str(destination) and str('q')!= str(destination)): #runs until q s or t
			destination = input("Would you like the average delay from Tsawwassen or Swartz Bay? Enter t for Tsawwassen, s for Swartz Bay, or q to quit\n")
		
		if(destination == "q"):
			sys.exit(0)

		while(str(month)!= str('1') and str(month)!= str('2') and str(month)!= str('3') and str(month)!= str('4') and str(month)!= str('5') and str(month)!= str('6') and 
		str(month)!= str('7') and str(month)!= str('8') and str(month)!= str('9') and str(month)!= str('10') and str(month)!= str('11') and str(month)!= str('12') and str(month)!= str('q')): #while its not between 1 and 12
			month = input("Which month would you like the data for? Enter a number between 1 and 12 for the month, or q to quit \n")

		if(destination == "s"):
			destination = "Swartz Bay"

		elif(destination == "t"):
			destination = "Tsawwassen"

		elif(month == "q"):
			sys.exit(0)

		if(str(month) == str('q')):
				sys.exit(0)

		months_and_numbers = [] #list of tupples to associate the number to the month
		tup = (1,"Jan")
		months_and_numbers.append(tup)
		tup = (2,"Feb")
		months_and_numbers.append(tup)
		tup = (3,"Mar")
		months_and_numbers.append(tup)
		tup = (4,"Apr")
		months_and_numbers.append(tup)
		tup = (5,"May")
		months_and_numbers.append(tup)
		tup = (6,"Jun")
		months_and_numbers.append(tup)
		tup = (7,"Jul")
		months_and_numbers.append(tup)
		tup = (8,"Aug")
		months_and_numbers.append(tup)
		tup = (9,"Sep")
		months_and_numbers.append(tup)
		tup = (10,"Oct")
		months_and_numbers.append(tup)
		tup = (11,"Nov")
		months_and_numbers.append(tup)
		tup = (12,"Dec")
		months_and_numbers.append(tup)
		tup = (12,"Dec")


		for el in months_and_numbers: #assigns a month to the number
			if(int(el[0]) == int(month)):
				mon = el[1]
		
		monthnotfound = 0
		for item in monthlist:  #looks for match
			if(int(item[1]) == int(month)):
				monthnotfound = 1
				with open(item[0], newline='') as csvfile:
					csv_reader(csvfile,mon,destination)

		if(monthnotfound == 0): #if month not found
			destination = destination + ":"
			print(":RESULTS")
			print(destination)
			print("    No delay data for",mon)
			print("END")


if __name__ == "__main__":
	main()
	
