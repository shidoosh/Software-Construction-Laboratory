#!/usr/bin/python

import sys 
from optparse import OptionParser 

class comm: 
	def __init__(self, file1, file2): 
		if (file1 != '-'):
			f1=open(file1, 'r')
			self.f1lines=f1.readlines()
			f1.close()
		else:
			self.f1lines=sys.stdin.readlines()

		if (file2 != '-'):
			f2=open(file2, 'r')
			self.f2lines=f2.readlines()
			f2.close()
		else:
                        self.f2lines=sys.stdin.readlines()

def compare():
	usage_msg = """comm [OPTION]... FILE1 FILE2
 
	Compare FILE1 and FILE2 line by line"""
	
	parser = OptionParser(usage=usage_msg)
	parser.add_option("-1", action="store_true", dest="col1", default=False)
	parser.add_option("-2", action="store_true", dest="col2", default=False)
	parser.add_option("-3", action="store_true", dest="col3", default=False)
	parser.add_option("-u", action="store_true", dest="unsorted", default=False)

	options, args = parser.parse_args(sys.argv[1:])	

	if (len(args) != 2):
		parser.error("Incorrect number of operands")

	column1=options.col1
	column2=options.col2	
	column3=options.col3
	notSorted=options.unsorted

	input_file1, input_file2 = args[0:2] 

	try: 
		c = comm(input_file1, input_file2)  
	except: 
		parser.error("File {0} and file {1} could not be compared".format(input_file1, input_file2)) 	


	allLines = c.f1lines+c.f2lines
	if (notSorted == False):
		allLines.sort()
	f1=c.f1lines
	f2=c.f2lines

	columns = []
	
	def toColumns():
		for i in allLines: 
			inF1=0
			inF2=0
			for j in f1: #is it in f1?
				if (i == j):
					inF1=1 		
					break
			for k in f2: #is it in f2?
				if (i == k):
					inF2=1
					break
			if (inF1 == 1 and inF2 == 0): # unique to FILE1
				columns.append([i, 1])
				f1.remove(i)	

			if (inF1 == 0 and inF2 == 1): # unique to FILE2
				columns.append([i, 2])
				f2.remove(i)
		
			if (inF1 == 1 and inF2 == 1): # shared element
				columns.append([i, 3])
				f1.remove(i)
				f2.remove(i)

	def toPrint(cols):	
		for each in columns:
			if (column1==False and column2==False and column3==False): 	#no options, print all columns
				if (each[1]==1): 					
					sys.stdout.write(each[0])
				if (each[1]==2): 
					sys.stdout.write('\t'+each[0]) 
				if (each[1]==3): 
					sys.stdout.write('\t\t'+each[0])  
			if (column1==True and column2==False and column3==False): 	# -1
				if (each[1]==2): 					#print column 2
                                        sys.stdout.write(each[0]) 
				if (each[1]==3): 					#print column 3
                                        sys.stdout.write('\t'+each[0])
 
			if (column1==False and column2==True and column3==False): 	# -2 
				if (each[1]==1):					#print column 1
                                        sys.stdout.write(each[0])
				if (each[1]==3):					#print column 3
                                        sys.stdout.write('\t'+each[0])

			if (column1==False and column2==False and column3==True):	# -3
				if (each[1]==1): 					#print column 1
                                        sys.stdout.write(each[0])
				if(each[1]==2):						#print column 2
					sys.stdout.write('\t'+each[0])
	
			if (column1==True and column2==True and column3==False): 	# -1 and -2 
				if (each[1]==3):					#print column 3
					sys.stdout.write(each[0])
			if (column1==True and column2==False and column3==True): 	# -1 and -3
				if (each[1]==2): 					#print column 2
                                        sys.stdout.write(each[0]) 
			if (column1==False and column2==True and column3==True):	#-2 and -3
				if (each[1]==1): 					#print column 1
                                        sys.stdout.write(each[0])

			#all options.. nothing! 

 
	try:
		toColumns()
	except:
		parser.error("Comparsion of file {0} and file {1} could not be completed".format(input_file1, input_file2))

	try:
		toPrint(columns)
	except:
		parser.error("Comparsion of file {0} and file {1} could not be printed".format(input_file1, input_file2))




if __name__ == "__main__":
    compare() 				
