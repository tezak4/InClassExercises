#What is a variable?
#Memory location
#variable names must start with an underscore or a letter
#Good:    spam    eggs   spam23    _speed
#Bad:     23spam     #sign  var.12
#Different:    spam   Spam   SPAM

#Primary data types are integers, floats, booleans, and strings
#We don't have the specify the data type before assigning a value to a variable
x = 2
print ('The current value of x is {}.'.format(x))
#Just because we used x as integer previously, does not mean that we have to use
#x as an integer in future lines of code.
x='tom is great!'
print(x.capitalize())
print(x.title())
print(type(x))
print(dir(x))

#Let's go back to assigning the integer value of 2 to x
x = 2
#Assignment with expression
x = x*7
print ('The current value of x is {} and x is a {} data type.'.format(x, type(x)))
#With numbers, we have to be careful with our order of operations
x = 1 + 2 * 3 - 4 / 5 ** 6
print(x)
x = 1 + 2 ** 3 / 4 * 5
print(x)

x = 2.7
print ('The current value of x is {} and x is a {} data type.'.format(x, type(x)))
print('The current value of x is ' + str(x) + ' and x is a ' + str(type(x)))
x = 4
x = 4/2
print ('The current value of x is {} and x is a {} data type.'.format(x, type(x)))
#All divison results in a float data type

x = True
print ('The current value of x is {} and x is a {} data type.'.format(x, type(x)))
x=False
print ('The current value of x is {} and x is a {} data type.'.format(x, type(x)))
print(type(x))
print(dir(x))
#The data types matter
a = 'Hello' + ' Bob'
print(a)
a = a + str(5)
print(a)
a = str(5)
a = a * 5
print(a)
a = '12345'
a = int(a) * 5
a = float(a) * 5
print(a)
print(type(a))
print(dir(a))
a = 14
a = srt(14) * 5
print(a)
print(type(a))
print(dir(a))
a = 14
a = str(14) * 5
print(a)

a = (input('Please enter a number'))
a = a*2
print (a)
#The output of every input statement is a String
a = int(input('Please enter a number'))
a = (a)*2
print (a)
#Why does the following line of code throw an error?
print('The value of a is ' + str(a))

name = '        bill jones         '
print (name)
print(name.title())
print(name.upper())
print (name.lstrip())
print (name.rstrip())
print(name.strip())
# print *************BILL JONES************
print (name.strip().upper().center(35,'|'))

#Let's display strings as fractions
from fractions import *
s = '0.07'
#s = None
#del s
f = fractions.Fraction(s)
print('{0} = {1}'.format(s, f))

import datetime
hiredate = datetime.date(2002, 11, 19)
print(type(hiredate))
name = 'bill jones'
print(f'My name is {name!r} and I was hired on {hiredate:%A, %B, %d, %Y}.')


#Conditional execution
x = 4
if x <= 4:
	print('This is a small number!')
	print('line 2 of this if clause')
	print('line 3 of this if clause')
else:
	print('else clause')
#You must indent to have a statement included in the if block
if x > 20:
	print('This is a large number')

x = 3
if x == 5:
	print('Equals 5')
if x > 4:
   print('Greater than 4')
if  x >= 5:
	print('Greater than or Equals 5')
if x < 6:
	print('Less than 6')
if x <= 5:
	print('Less than or Equals 5')
if x != 6:
	print('Not equal 6')

x = 5
print('Before if statement for x == 5')
if  x == 5:
	print('Is 5')
	print('Is Still 5')
	print('Third 5')
print('After the first if statement for x == 5')
print('Before if statement for x == 6')
if x == 6:
	print('Is 6')
	print('Is Still 6')
	print('Third 6')
print('After the second if statement for x == 6')

x = 42
if x > 1:
	print('More than one')
	if x < 100:
		print('Less than 100')
print('All done')

x = 4

if x > 2:
	print('Bigger')
else:
	print('Smaller')

print('All done')

if x < 2:
	print('small')
elif x < 10:
	print('Medium')
else:
	print('LARGE')
print('All done')

x = 5
if x < 2:
	print('Small')
elif x < 10:
	print('Medium')

print('All done')

if x < 2:
	print('Below 2')
elif x < 20:
	print('Below 20')
elif x < 10:
	print('Below 10')
else:
	print('Something else')

name = 'Hello Prof-Mattson'
try:
	istr = int(name)
except:
	print('There was an error in the try block!!!!')

age = 47
if age >= 18:
	print('You are old enough to enlist in the army!')
	print('Is a military career the correct path for you?')
else:
	if age < 13:
		print('I hope you are enjoying your childhood')
	else:
		print('You are at the age where you should start thinking about your career')

#Single line if/statements
age = 12
print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')


#Ask the user to enter the state that they live in (fully spelled out)?
#Store that state in a variable
State = (input("Please enter the entire name of the state that you live in"))
#Then, display (print) the first two characters of that state in upper case letters
print(State[0:2].upper())
#For example, the print out should be 'You reside in VI, which stands for Virginia in this analysis!' for Virginia.
#Obviously, these are not the correct state abbreaviations (just working on concatenation)!!!!
print('You reside in ' + State[0:2].upper() + ' which stands for ' + State + " in this analysis")


#Ask the user to input the number of consultants assigned to a project
#and store that as a variable.
num = int(input("How many consultants are assigned to a project?"))
#Then, ask the user to input the average number of hours per consultant
#and store that as a variable.
hours = int(input('How many average hours do they spend on the project?'))
#Then, ask the user to input the average hourly wage of the consultants
#and store that as a variable.
wage = float(input("What is the hourly wage of the consultants?"))
#Then, calculate the cost, which is a product of those three inputs.
cost = num*hours*wage
#Finally, display the cost in a user friendly sentence.
print("For this project the total cost will be {}".format(cost))



#In the previous program, try to format the numbers that are currencies as currency
# and floats with two decimal points!
#hint: The locale module might be helpful here
import locale
locale.setlocale(locale.LC_ALL, 'en_US')
print('This project had {a} consultants assigned to it who owrks and average o f \n'
      '{b} hours (per consultant) \n as an average rate per hour of {c}, '
      'which is an average cost of {d}.'.format(a='{:,.2f}'.format(num),
                                                b ='{:,2f}'.format(hours),
                                                c =locale.currency(wage,grouping=True),
                                                d= locale.))

#Ask the user to input an integer value under 20
num = int(input('Please input an integer value under 20'))
#Calculate the factorial of that number
output = 1
for i in range(1,num+1):
	output = output*i
print(str(output))
#Print a user-friendly message containing that factorial.
#Try to format the factorial in a readable manner (i.e., with commas)

num = int(input("Please input an integer value under 20"))
output = 1
for i in range(1,num+1):
	print(str(output) + '*' + str(i))
	output = output*i


#Write a program to ask the user to enter two integer numbers. Then, calculate the whole number
# division with the first number as the numerator and the second number as the denominator.
# Then, display the answer as something like “The floor division of {num1} divided by {num2} is {answer}”.
num = int(input("Please enter an integer"))
num2 = int(input("Please enter an integer"))
divided = num/num2
print("The floor division of {} divided by {} is {}".format(num,num2,divided))


#Create a variable that stores the following:
#'     hello this is some random text     '
#strip away the leading and trailing spaces in this string
#print off the word with the leading and trailing spaces removed with each word capitalized
statement = '     hello this is some random text     '
print(statement.strip().title())

#Notice the difference between title() and capitalize(), which one is correct for this question?
print(statement.strip().capitalize())

#Ask the user to enter the number of days in the month of March.
#If the user enters the correct number, print a message that displays
#'You passed the test.'  If the user enters incorrectly, print a message that displays
#'You failed the test.

days = int(input("How many days are in the month of March"))
if days == 31:
	print("you have passed the test")
else:
	print("you have failed the test")

#Ask the user to enter a two letter state abbreviation for a state that starts with the letter c
#Based on the state abbreviation that the user enters, print the name of the state.
#If the user enters a state abbreviation that does not start with C, print an invalid data entry message
state = input("Please input the two letter state abbreviation for a state that starts with C").upper()
if state[0] != 'C':
	print('Invalid data entry')
else:
	if state == 'CA':
		print("California")
	elif state == 'CT':
		print('Connecticut')
	elif state =='CO':
		print("Colorado")
	else:
		print("This is not a valid state abbreviation")


#Surround the previous set of statements with a try/except block
#Will the except block ever execute?  Why or why not?
try:
	state = input("Please input the two letter state abbreviation for a state that starts with C").upper()
	if state[0] != 'C':
		print('Invalid data entry')
	else:
		if state == 'CA':
			print("California")
		elif state == 'CT':
			print('Connecticut')
		elif state == 'CO':
			print("Colorado")
		else:
			print("This is not a valid state abbreviation")
except:
	print("Invalid data entry!")
#The except block will never execute because you can enter any value as a string and the program will run with it


#Ask the user to enter three numbers
#if the third number is greater than the second number and the second number is greater than the first number
#print a message such as 'Success. num1 < num2 < num3'
num1 = int(input("Please enter an integer"))
num2 = int(input("Please enter an integer"))
num3 = int(input("Please enter an integer"))
if(num1 < num2) and (num2 < num3):
	print('Success! num1<num2<num3')
#Add a else clause to the previous example that prints a message such as 'Failure. num1 < num2 < num3 is not true'
else:
	print("failure. num<num2<num3 is not true")

#Ask the user to enter a number between 10 and 20 (non-inclusive)
#If the user properly follows instructions, print a success message.
#If not, print a failure message.
num = int(input("Please enter a number between 10 and 20 (non-inclusive"))
if(num > 10) and (num < 20):
	print("Good job")
else:
	print("Failure")



#Compare the values contained in a and b
#if a is less than b, print an appropriate message.  If that is true, then check if c is less than b.
#if that is true, print an appropriate message.  Otherwise, print an appropriate message.
#if a is not less than b, print an appropriate message.
a = 4
b = 2
c = 1
if(a < b):
	print('a is less than b')
	if(c<b):
		print('c is less than b')
	else:
		print('c is greater than or equal to b')
else:
	print('a is greater than or equal to b')


#Write several clauses checking the value of a.
#If a is less than zero, print an appropriate message.
#else if a is zero, print an appropriate message.
#else if a is between 0 and 5 (not inclusive), print an appropriate message.
#otherwise, print a message indicating that a is greater than or equal to 5.
if(a<0):
	print("a is a negative number")
elif(a ==0):
	print('a is 0')
elif(a<5) and (a > 0):
	print('a is between 0 and 5')
else:
	print('a is greater than or equal to 5')