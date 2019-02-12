# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354776
# Author: Alex Garcia
# Excercise: L3
# File name: statfunctions.py
# Description: module containing different math and statistical functions
# Date created: 02/01/2019
# Date last modified: 02/11/2019
# Python Version:  3.7.2

# Begin code
import random as rn
import numpy as np

randomGen = rn.sample(range(0,100), 9)
print("Your list of random numbers is: " + str(randomGen))

def sampleMean():
	Sum = sum(randomGen)
	sampleMeanValue = Sum / len(randomGen)
	print("- The Sample Mean using the random module and basic arithmetic operations " + str(sampleMeanValue))
	print("- The Sample Mean using the numpy module is " + str(np.mean(randomGen)))

def sampleStandardDeviation():
	standarDeviationValue = np.std(randomGen, ddof=1)
	print("- The Sample Standard Deviation using the numpy module is " + str(standarDeviationValue))
	
def median():
	medianValue = np.median(randomGen)
	print("- The Median using the numpy module is " + str(medianValue))

def nQuartil():
	quartilValue = np.percentile(randomGen,[25,50,75])
	print("- The nQuartil using the numpy module is " + str(quartilValue))

def nPercentil():
	percentilValue = np.percentile(randomGen,50)
	print("- The nPercentil using the numpy module is " + str(percentilValue))


sampleMean()
sampleStandardDeviation()
median()
nQuartil()
nPercentil()
