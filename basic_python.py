

#22. Write a Python program to count the number 4 in a given list.





# only = 50 |17, 20|
#21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
def even_or_odd(n):
	if n%2 == 0:
		print ("This is an even number.")
	if n % 2 == 1:
		print ("This is an odd number.")
	else:
		print ("Ok")
n = int(input("Input number: "))
print even_or_odd(n)

# or:
n = int(input("Input number: "))
mod = n % 2
if mod > 0:
	print ("This is an odd number.")
else:
	print ("This is an even number.")


#20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# I don't understand solution.
def larger_string(str, n):  
   result = ""  
   for i in range(n):  
      result = result + str  
   return result  
  
print(larger_string('abc', 2))  
print(larger_string('.py', 3))  


#19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. 

def start_is(s):
	if s.startswith("Is"):
		return s
	else:
		return "Is \a" + s
print start_is("Lorem ipsum dolor sit amet. ")
print start_is("Is voluptate velit esse cillum dolore. ")


#18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def sum_trize(n1, n2, n3):
	summ = n1 + n2 + n3
	if n1 == n2 == n3:
		return (summ * 3)
	else:
		return (summ)
n1 = float(input("Input number1: "))
n2 = float(input("Input number2: "))
n3 = float(input("Input number3: "))
print sum_trize(n1, n2, n3)


#17. Write a Python program to test whether a number is within 100 of 1000 or 2000
# I really don't understand task


#16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
f_num = float(input("Input any number: "))
s_num = 17
if f_num <= 17:
	print (s_num - f_num)
else:
	print ((f_num - s_num) * 2)
# or
def difference(n):
	if n <= 17:
		print (17 - n)
	else:
 		return ((n-17)*2)
print difference(24)


# Write a Python program to get the volume of a sphere with radius 6
pi = 3.141592
r = 6
V = (4.0/3.0 * r**3 * pi)  # or V = ((float(4)/ float(3)) * r**3 * pi)
print "The volume of a sphere with radius 6 is: ", V


#14. Write a Python program to calculate number of days between two dates.
import datetime
first = datetime.date(2014, 7, 2)
second = datetime.date(2014, 7, 11)
print second - first


#13. Write a Python program to print the following here document. 
text = ("""Sample string : \n a string that you "don't" have to escape \n This \n is a ....... multi-line \n heredoc string --------> example""")
print text


#12. Write a Python program to print the calendar of a given month and year.
import calendar
mm = input("Input month / use numbers, please: ")
yy = input("Input year: ")
print (calendar.month(yy, mm))


#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
print (abs.__doc__)
print (sum.__doc__)


#10. Write a Python program that accept an integer (n) and computes the value of n+nn+nnn. 
n = int(input("Input number, Mate: "))
n1 = int('%i' %(n))
n2 = int('%i%i' %(n, n))
n3 = int('%i%i%i' %(n, n, n))
print (n1 + n2 + n3)


#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print ("The examination will start from: %d / %d / %d" %(exam_st_date))


#8. Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]
print (color_list[0], color_list[-1])
#or
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))


#7. Write a Python program to accept a filename from the user print the extension of that
#filename = input("Input the Filename: ")    /Sorry, input doesn't work =(
filename = "views.txt"
f_extns = filename.split(".")
print ("The  extension of the file is : " + f_extns[-1])


#5. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
values = input("Input a sequence of comma-separated numbers: ")
x = tuple(values)
y = [values]
print('tuple:', x)	
print('list:', y)


#5. Write a Python program which accept the user's first and last name and print them in reverse order with a space between them
#person = input('Enter your name: ')
#print 'Hello', person

#fname = input("Enter you First name: ")
#lname = input("Enter you Last name:")
#print (fname, lname)

#fname = input("Input your First Name : ")  
#lname = input("Input your Last Name : ")  
#print ("Hello  " + lname + " " + fname)    


#4. Write a Python program which accept the radius of a circle from the user and compute the area. S=p*r2
def area(r):
	if r<=0:
		return ("Try again, Input error for radius")
	else:
		 s = 3.14 * (r**2)
		 return (s)

print ("Input value of radius: ")
r = float(input("r = "))
print area(r)

 # or:
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


#3. Write a Python program to display the current date and time
# strftime - format date and time
import time
print ("* Current data and time now:")
print (time.strftime("%w %A %j %d/%m/%Y %H:%M:%S / %T / %R"))

#2. Write a Python program to get the Python version you are using, V konsoli: python -V
import sys
print ("* Python version is:")
print (sys.version)

#1. Write a Python program to print the following string in a specific format
print("* Twinkle, twinkle, little star, \n\t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n\t How I wonder what you are")


