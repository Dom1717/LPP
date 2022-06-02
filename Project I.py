import math
#Given any non-negative, non-alphabetic number, output next integer divisible by 10:
x = input("Enter a non-negative number to find the next number divisible by 10, increasing: ")  #outputs str
while x.count('-') >= 1:  ##check to make sure input doesn't contain a negative
    x = input("Please enter a non-negative number: ")
##check input to make sure it contains no letters:
while x.isalpha() == True or (x.isalnum() == False and x.count('.') != 1):
    x = input("Please enter a non-negative, non-alphabetic number: ")
z = x  ##retains initial successful input for clarity in output
x = float(x)  ##first convert input to float
x = math.floor(x)  ##reduce input to just integer component
x = int(x)  #change our input to an integer
y = x / 10
while x % 10 != 0:  ##incriment x so long as there is a remainder when divided by 10
    x += 1
print("The next number divisible by 10 for "+str(z)+ " is: "+str(x))