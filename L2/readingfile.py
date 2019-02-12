# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354776
# Author: Alex Garcia
# Excercise: L2-13-14
# File name: readingfile.py
# Description: class to read values for a list from a textfile
# Date created: 02/11/2019
# Date last modified: 02/11/2019
# Python Version:  3.7.2

# Begin code
import time as tm

class myPoweList():
	def createListOfNumbers(self):
		values = input("Input some comma seprated numbers: ")
		global valueList
		valueList = values.split(",")
		print('Python List: ',valueList)

	def saveToTextFile(self,filename):
		with open(filename, 'w') as filehandle:  
			for listitem in valueList:
				filehandle.write('%s\n' % listitem)

	def readFromTextFile(self,filename):
		emptyNumbers = []
		with open(filename, 'r') as filehandle:  
			for line in filehandle:
				placeHolder = line[:-1]
				emptyNumbers.append(placeHolder)
				print(placeHolder)

def main():
	mpl = myPoweList()
	mpl.createListOfNumbers()
	fileName = input("How would you like to name yout file? ")
	fileNameWithExtension = fileName + ".txt"
	mpl.saveToTextFile(fileNameWithExtension)
	tm.sleep(2)
	print("Here's the list of numbers you just created: ")
	mpl.readFromTextFile(fileNameWithExtension)

if __name__ == "__main__":
	main()