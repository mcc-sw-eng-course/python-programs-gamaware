# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A01223463, A00354776 
# Author: Bruno Vergaray, Alex Garcia
# Excercise: L6
# File name: SortData.py
# Description: Sorting Data using different algorithms
# Date created: 02/26/2019
# Date last modified: 03/07/2019
# Python Version:  3.7.2

# Begin code
from pathlib import Path
import csv
from datetime import datetime

# Magic strings for the performance data map
NUM_OF_RECORDS = "num_of_records"
TIME_CONSUMED = "time_consumed"
START_TIME = "start_time"
END_TIME = "end_time"
ALGORITHM = "algorithm used"

# Algorithm Identifiers
MERGE_SORT = "Merge Sort"
HEAP_SORT = "Heap Sort"
QUICK_SORT = "Quick Sort"

class Sorter:
    def __init__(self):
        self.readfile = ""
        self.writefile = ""
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.algorithm_used = ""

    def set_input_data(self, file_location):
        file = Path(file_location)
        if not file.is_file():
            raise ValueError("file not found")
        try:
            with open(file_location, newline='') as f:
                reader = csv.reader(f, delimiter=',',lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
                self.readfile = list(reader)
                for row in reader:
                    print(', '.join(row))


        except:
            raise ValueError("could not open file")
        return self.readfile



    def set_output_data(self, file_location):

            with open(file_location, 'x') as f:
                writer = csv.writer(f, quoting = csv.QUOTE_ALL)
                self.writefile = writer.writerow(self.readfile)


    def mergeSort(self,list):

        self.algorithm_used = MERGE_SORT
        self.start_time = datetime.now()
        if len(list) > 1:
            mid = len(list) // 2  # Finding the mid of the array
            L = list[:mid]  # Dividing the array elements
            R = list[mid:]  # into 2 halves

            self.mergeSort(L)  # Sorting the first half
            self.mergeSort(R)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    list[k] = L[i]
                    i += 1
                else:
                    list[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                list[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                list[k] = R[j]
                j += 1
                k += 1

        self.end_time = datetime.now()

    #For Heap Sort
    def heapify(self,list, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and list[i] < list[l]:
            largest = l

            # See if right child of root exists and is
        # greater than root
        if r < n and list[largest] < list[r]:
            largest = r

            # Change root, if needed
        if largest != i:
            list[i], list[largest] = list[largest], list[i]  # swap

            # Heapify the root.
            self.heapify(list, n, largest)

    def heapSort(self, list):
        self.algorithm_used = HEAP_SORT
        n = len(list)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(list, n, i)

            # One by one extract elements
        for i in range(n - 1, 0, -1):
            list[i], list[0] = list[0], list[i]  # swap
            self.heapify(list, i, 0)

    #For Quick Sort
    def partition(self, list, low, high):
        i = (low - 1)  # index of smaller element
        pivot = list[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if list[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                list[i], list[j] = list[j], list[i]

        list[i + 1], list[high] = list[high], list[i + 1]
        return (i + 1)

    def quickSort(self, list, low, high):
        self.algorithm_used = QUICK_SORT
        if low < high:
            # pi is partitioning index, list[p] is now
            # at right place
            pi = self.partition(list, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(list, low, pi - 1)
            self.quickSort(list, pi + 1, high)

    def get_performance_data(self)-> dict:
        stats = [NUM_OF_RECORDS + ": " + str(len(self.readfile[0])),
        TIME_CONSUMED + ": " + str(self.end_time - self.start_time),
        START_TIME + ": " + str(self.start_time),
        END_TIME + ": " + str(self.end_time),
        ALGORITHM + ": " + str(self.algorithm_used)
        ]
        print("\n".join( repr(e) for e in stats))

    def defineAlgorithm(self):
        fCallToMainClass = Sorter()
        extractData = fCallToMainClass.set_input_data("convertData.csv")
        fAlgorithm = int(input("Which alogorithm would you like to use to perform the sort? \n1. For Merge Sort\n2. For Heap Sort\n3. For Quick Sort\n"))
        if fAlgorithm == 1:
            print("\nYou have selected Merge Sort")
            fAlgorithm = 1
            fCallToMainClass.mergeSort(extractData[0])
        elif fAlgorithm == 2:
            print("\nYou have selected Heap Sort")
            fAlgorithm = 2
            fCallToMainClass.heapSort(extractData[0])
        elif fAlgorithm == 3:
            print("\nYou have selected Quick Sort")
            fAlgorithm = 3
            fCallToMainClass.quickSort(extractData[0],0,1048575)
        else:
            print("You didn't select a valid option") 
        try:
            fCallToMainClass.set_output_data("output.csv")
        except:
            raise ValueError("File already exists!")
        fCallToMainClass.get_performance_data()    
       
def main():
    callToMainClass = Sorter()
    callToMainClass.defineAlgorithm()
    #selectedAgorithm = callToMainClass.defineAlgorithm()
    #callToMainClass.selectedAgorithm(extractData[0])

if __name__ == "__main__":
	main()