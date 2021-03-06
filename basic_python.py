

#28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. 
def even_num(numbers):
	for i in numbers:
		if i == 237:
			break
		else:
			if i%2 == 0:
				print i	
print "Exercise: 28"
print even_num([    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ])



# only = 44 |17, 26|
#27. Write a Python program to concatenate all elements in a list into a string and return it.
def convert_to_str(some_list):
	result = ""
	for i in some_list:
		result = result + str(i)
	return result
print "Exercise: 27"
print convert_to_str([2, 5, 6, 'b', '#'])
# in case:
s = ""
list1 = [2, 5, 6,'b', '#']
conv = s.join(str(x) for x in list1)
print conv

#26. Write a Python program to create a histogram from a given list of integers.
#pass

#25. Write a Python program to check whether a specified value is contained in a group of values. 
#My version
def in_group(n, group):
	if n in group:
		return True
	return False
print "Exercise: 25"
print in_group(3, [1, 5, 8, 3])
print in_group(-1,[1, 5, 8, 3])
#
def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))


#For me: How to count vowel and consonant letters in some text.
def count_vowel_or_consonant_letter(text):
	count_vowel = 0
	count_consonant = 0
	vowel = ('aeiouAEIOU')
	consonant = ('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
	for i in text:
		if i in vowel:
			count_vowel = count_vowel + 1
		else:
			count_consonant = count_consonant + 1 
	return count_vowel, count_consonant
print "Exercise: without number"
print count_vowel_or_consonant_letter("These five or six letters stand for about 20 vowel sounds in most English accents. This important fact helps to explain why pronunciation can be difficult for both native speakers and learners of English")


#24. Write a Python program to test whether a passed letter is a vowel or not.
def is_vowel(n):
    all_vowels = 'aeiou'
    return n in all_vowels
print "Exercise: 24"
print(is_vowel('c'))
print(is_vowel('e'))	


#23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given sting. Return the n copies of the whole string if the length is less than 2.
# My version:
def take_2_char(str, n):
	result = ""
	if len(str) >= 2:
		for i in range(n):
			result = result + str[:2]
		return result
	else:
		for i in range(n):
			result = result + str[0]
		return result
print "Exercise: 23"
print take_2_char("Happyhour", 2)
print take_2_char("l", 5)
#Version from net:
def substring_copy(str, n):
  flen = 2
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));


# No number, my function=)
def count_letter(text):
	count = 0
	for x in text:
		if x == "a":
			count = count + 1
	return (" In this text we found letter 'a': ", count, "times.")
print count_letter("But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful.")


#22. Write a Python program to count the number 4 in a given list.  / But where i need to take  "given list"?
def list_count_4(nums):
	count = 0
	for x in nums:
		if x == 4:
			count = count + 1
	return count
print "Exercise: 22"
print list_count_4([1, 4, 6, 7, 4])
print list_count_4([1, 4, 6, 4, 7, 4])


#21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
def even_or_odd(n):
	if n%2 == 0:
		print ("This is an even number.")
	if n % 2 == 1:
		print ("This is an odd number.")
	else:
		print ("Ok")
n = int(input("Input number: "))
print "Exercise: 21"
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
print "Exercise: 20"  
print(larger_string('abc', 2))  
print(larger_string('.py', 3))  


#19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. 

def start_is(s):
	if s.startswith("Is"):
		return s
	else:
		return "Is \a" + s
print "Exercise: 19"
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
print "Exercise: 18"
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
print "Exercise: 16"
print difference(24)


#15. Write a Python program to get the volume of a sphere with radius 6
pi = 3.141592
r = 6
V = (4.0/3.0 * r**3 * pi)  # or V = ((float(4)/ float(3)) * r**3 * pi)
print "Exercise: 15"
print "The volume of a sphere with radius 6 is: ", V


#14. Write a Python program to calculate number of days between two dates.
import datetime
first = datetime.date(2014, 7, 2)
second = datetime.date(2014, 7, 11)
print "Exercise: 14"
print second - first


#13. Write a Python program to print the following here document. 
text = ("""Sample string : \n a string that you "don't" have to escape \n This \n is a ....... multi-line \n heredoc string --------> example""")
print "Exercise: 13"
print text


#12. Write a Python program to print the calendar of a given month and year.
import calendar
mm = input("Input month / use numbers, please: ")
yy = input("Input year: ")
print "Exercise: 12"
print (calendar.month(yy, mm))


#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
print "Exercise: 11"
print (abs.__doc__)
print (sum.__doc__)


#10. Write a Python program that accept an integer (n) and computes the value of n+nn+nnn. 
n = int(input("Input number, Mate: "))
n1 = int('%i' %(n))
n2 = int('%i%i' %(n, n))
n3 = int('%i%i%i' %(n, n, n))
print "Exercise: 10"
print (n1 + n2 + n3)


#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print "Exercise: 9"
print ("The examination will start from: %d / %d / %d" %(exam_st_date))


#8. Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]
print "Exercise: 8"
print (color_list[0], color_list[-1])
#or
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))


#7. Write a Python program to accept a filename from the user print the extension of that
#filename = input("Input the Filename: ")    /Sorry, input doesn't work =(
filename = "views.txt"
f_extns = filename.split(".")
print "Exercise: 7"
print ("The  extension of the file is : " + f_extns[-1])


#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
values = input("Input a sequence of comma-separated numbers: ")
x = tuple(values)
y = [values]
print "Exercise: 6"
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
print "Exercise: 4"
print area(r)

 # or:
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


#3. Write a Python program to display the current date and time
# strftime - format date and time
import time
print "Exercise: 3"
print ("* Current data and time now:")
print (time.strftime("%w %A %j %d/%m/%Y %H:%M:%S / %T / %R"))

#2. Write a Python program to get the Python version you are using, V konsoli: python -V
import sys
print "Exercise: 2"
print ("* Python version is:")
print (sys.version)

#1. Write a Python program to print the following string in a specific format
print "Exercise: 1"
print("* Twinkle, twinkle, little star, \n\t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n\t How I wonder what you are")


