# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354776
# Author: Alex Garcia
# Excercise: L1-9
# File name: decimaltoroman.py
# Description: module with function to convert from decimal numbers to roman numbers
# Date created: 02/11/2019
# Date last modified: 02/11/2019
# Python Version:  3.7.2

# Begin code
def decimalToRoman(number):
    decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while number > 0:
    	for _ in range(number // decimal[i]):
    		roman_num += roman[i] 
    		number -= decimal[i] 
    	i += 1
    print("The Roman equivalent to such number is " + str(roman_num))

DecimalNumber = int(input("Enter a number between 1 and 4999: "))
decimalToRoman(DecimalNumber)