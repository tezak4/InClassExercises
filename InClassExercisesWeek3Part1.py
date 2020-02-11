#Review activities
#Ask the user how many days in a leap year
#If they enter the correct answer, then print a success message.
days = int(input("How many days are in a leap year?"))
if(days == 366) :
    print("That is correct!")
else :
    print("That is incorrect!")



#Ask the user if python is an interpreted language.
#If the user answers correctly, then print a message indicating that they answered correctly
#If the user answers incorrectly, then print a message indicating that they answered incorrectly.
#Finally, print a message thanking the user for their participation (regardless of whether they
#answered correctly or incorrectly.
answer = str(input("Is python an interpreted language?")).capitalize()
print(answer)
if(answer == "Yes" or answer == "Y") :
    print("That is correct!")
else:
    print("That is incorrect!")
print("Thank you for participating in this game")




#Ask the user to enter an integer (whole) number.
#Then, print a message indicating whether the number is odd or even.
#For this if/else statement, write it in a single line.
#If the user enters something other than a number, print a message indicating the incorrect input.

try:
    number = int(input("Please input a whole number"))
    if(number%2 == 0): print('This number is odd') else: print("this number is odd")
except:
    print("You must input an integer value")




#Ask the user for three integer (numerical inputs).
#The first input is for the number of machines, which should be either 10 or 20.
# The second input is for units produced per machine per hour.
#The third input is for hours that the machines will be operational.
#if the number of machines equals 10, then print a message indicating that the plant has 10 machines operational.
#For plants with 10 machines working, if the units multiplied by the hours multiplied by the machines is
# is less than or equal to 4000, print
#a message indicating that these 10 machines still have capacity.  Otherwise, print a message indicating that
# these machines are over capacity.
#For the plants with 20 machines working, if the units multiplied by the hours multiplied by the machines is
#less than or equal to 800, print
#a message indicating that these 20 machines still have capacity.  Otherwise, print a message indicating that
# these machines are over capacity.
#For plants that do not have either 10 or 20 machines operational, tell the user that the program
#only works for 10 or 20 machines.
#If the user enters a non-numeric value for one of the three inputs, enter an appropriate error message.
machines= int(input("Do you have 10 or 20 machines?"))
units = int(input("How many units are produced per machine per hour?"))
hours = int(input("How many hours are the machines working for?"))
if(machines == 10):
    print("There are 10 operational machines.")
    if((units*hours) <= 4000):
        print("These machines still have capacity")
    else:
        print("These machines are over capacity")
elif(machines == 20):
    print("There are 20 operational machines")
    if((units*hours) <= 800):
        print("These machines still have capacity")
    else:
        print("These machines are over capacity")
else:
    print("This problem only works for 10 or 20 machines.")


#Define two variables and assign integer values to them
#If a is not greater than b, then
#print a message such as 'The number 10 is less than 20.' or 'The number 10 is equal to 10.'
#If a is greater than b, then print a message such as 'The number 11 is greater than 10.'
a = 15
b = 11
if(a <= b):
    print("The number " + str(a) + " is less than or equal to " + str(b))
else:
    print("The number " + str(a) + " is greater than " + str(b))


###New content about 'collections'
##Lists are collections that are mutable.  They have

food1 = 'Apple'
food2 = 'Orange'
food3 = 'Pear'
#the previous is inefficient...what happens if I have 100 foods to store?
#Having 100 different food variables would not be a good way of
# storing and referencing my food!
#Instead, we can use a list!
foods = ['Apple', 'Orange', 'Pear']
print(type(foods))
#What type of properties and functions are available for a list?
print(dir(foods))
print(foods)
print(foods[0])

#Can have lists containing many different data types
stuff = ['red', 24, 98.6]
print(stuff[0])
#including other lists!
stuff = [1, [5, [77,88]], 7, 'blue', ['apple','pear','orange'], [4, 'bill']]
print(stuff[0])
print(stuff[1])
print(stuff[1][1][0])

#We can loop over the items in a list
my_list = list(range(0,11))
print(my_list)
print(type(my_list))
#for loops have explicit iteration variables that change each time through a loop.
for i in  my_list:
    print(i)

#reverse the order of the elements in the list
my_list.reverse()
for i in  my_list:
    print(i)


my_list = [10,10,10,11,12,13,19,22,22,27,28,29,30,33]
print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sum(my_list)/len(my_list))

import statistics
print(statistics.mean(my_list))
print(statistics.stdev(my_list))
print(statistics.median(my_list))
print(statistics.mode(my_list))

employees = ['joe', 'amy', 'sally']
for employee in employees:
    print(employee.title() + ', you are a great employee!')
    print('I can\'t wait to work with you on a project again, ' + employee.title() + '.\n')
    #Does this blank line impact anything?
    print('Thank you!')

print ('joe' in employees)
print('timewe' in employees)
print ('sally' not in employees)
print(sorted(employees, reverse = True))
new_list = sorted(employees, reverse = True)
print(new_list)

variants = [4, 3.0, '5', 1.5, '2']
variants.sort()
print(variants)

#Generate odd numbers between 1 and 10
odds = list(range(1,11,2))
print(odds)

#Now let's build a list containing the squares of these odd numbers
squares = []
for num in odds:
    square = pow(num,2)
    squares.append(square)
print(squares)

#Another way to do this in a single line
squares = [num**2 for num in list(range(1,11,2))]
print(squares)
#Count the number of instances of a value in the list
employees = ['joe', 'amy', 'sally', 'joe', 'amy', 'amy']
print(employees.count('amy'))

print(employees.index('amy'))
print(employees.index('amy',2))

#insert items in the list
employees.insert(3, 'tim')
print(employees)
employees.insert(5, 'jane')
print(employees)

employees.pop()
print(employees)

employees.pop(3)
print(employees)

employees.clear()
print(employees)

del employees
print(employees)

employees1 = ['joe', 'amy', 'sally']
employees2 = ['jane', 'jim', 'andy']
employees3 = employees1 + employees2
print(employees1)
print(employees2)
print(employees3)
#We can also copy lists
employees4 = employees3[:]
#employees4 = employees3.copy()
print(employees4)
employees3.append('tom')
employees4.append('tony')
#so we started with the copy but now the last element in each of these lists are different
print(employees3)
print(employees4)

employees1 = ['joe', 'amy', 'sally']
employees2 = ['jane', 'jim', 'andy']
employees1.extend(employees2)
print(employees1)
print(employees2)


#notice what happens with this syntax...Here, we are not creating two separate lists
#This equal to sign essentially creates the same memory location so they are not separate lists!
employees1 = ['joe', 'amy', 'sally']
employees2 = employees1
employees1.append('tim')
print(employees1)
print(employees2)

employees1 = ['joe', 'amy', 'sally']
employees2 = ['jane', 'jim', 'andy']
employees3 = employees1 + employees2
print(employees3)
print(employees3[0:3])
print(employees3[2:4])
print(employees3[:4])
print(employees3[2:])

#We can also loop over a slice of the elements in a list
#first x number of employees
x = 3
print('Here are the first {} employees in my list'.format(x))
for emp in employees3[:x]:
    print(emp.title())

line = 'custid|name|address|email'
etc = line.split('|')
print(etc)
print(len(etc))
etc.append('phone')
print(etc)

#tuples...immutable collections
tm_tuple = ()
print(tm_tuple)
print(type(tm_tuple))

# Tuple having integers
tm_tuple = (1, 2, 3, 4, 5, 6)
print(tm_tuple)

# tuple with mixed datatypes
tm_tuple = (99, 'Tom Mattson', 99.7, 14)
print(tm_tuple)

# nested tuple
tm_tuple = ('Bill Jones', [1, 7, 9], (4, 9, 7))
print(tm_tuple)

nums = (900,175,255)
print(nums[0])
print(nums[1])
print(nums[2])

#Note the error when we try to change an item in a tuple
#nums[0]=800

#A tuple can also be created without using parentheses. This is known as tuple packing.
tm_tuple = 313, 'tim', 0.9, 'William Akima'
print(tm_tuple)

# tuple unpacking is also possible
a,b,c,d = tm_tuple

print(a)
print(b)
print(c)
print(d)

#Creating a tuple with one element is a bit tricky.
#Having one element within parentheses is not enough.
#We will need a trailing comma to indicate that it is, in fact, a tuple.

#Is this a tuple or a string
tm_tuple = ('welcome to my class')
print(type(tm_tuple))

# Creating a tuple having one element
tm_tuple = ('welcome to my class',)
print(type(tm_tuple))

# Parentheses are optional but best practice is to include the parentheses
#when defining a tuple
tm_tuple = 'welcome to my class',
print(type(tm_tuple))


#Reference elements in a tuple using an index number
#index numbers start with 0
tm_tuple = ('a', 'c', 't', 'i', 'v', 'i', 't', 'y')
print(tm_tuple[0])
print(tm_tuple[5])
#Note the error when we reference an index using a float
# print(tm_tuple[4.0])
# IndexError: list index out of range
# print(tm_tuple[8])

# nested tuple
tm_tuple = ('pets', [99, 14, 8], (12, 94, 89, 76, 54))

# nested index
#print off the value contained in the first element in the tuple
print(tm_tuple[0])
#print off the second character in the first element of the tuple
print(tm_tuple[0][1])
#print off the last two characters in the first element of the tuple
print(tm_tuple[0][1:])
#now work with the second element of the tuple, which is a list
print(tm_tuple[1])
#print the first two elements of the list that is contained in the second element of the testing_tuple
print(tm_tuple[1][:2])
#The next two lines of code complete the same task
numbers = tm_tuple[1]
print(numbers[:2])

#Now work with the third element in the testing_tuple, which is a tuple object
print(tm_tuple[2])
#print the third element of the nested tuple
print(tm_tuple[2][2])

#The following is functionally equivalent
tuple2 = tm_tuple[2]
print(tuple2[2])

#We can also use negative indexing to reference elements in a tuple
# such that an index of -1 refers to the last item, -2 to the second last item,  and so on.

tm_tuple = ('w', 'i', 'l', 'l', 'y')
print(tm_tuple[-1])
print(tm_tuple[-4])

# We can slice a tuple or access a range of items in a tuple
testing_tuple = ('j', 'o', 'h', 'n', 's', 'o', 'n', '-', 's', 'o', 'n')

#Reminder - zero based!
print(testing_tuple[0:4])
print(testing_tuple[:4])
print(testing_tuple[4:])
#print off fmatt
print(testing_tuple[3:7])

#use negative referencing!
#prof
print(testing_tuple[:-7])
#mattson
print(testing_tuple[-7:])
#print out everything
print(testing_tuple[:])
print(testing_tuple)


#Reminder again: Unlike lists, tuples are immutable.
#However, if the element is itself a mutable datatype like list, its nested items can be changed.
#We can also assign a tuple to different values (reassignment).

testing_tuple = (14, 17, 19, [8, 3, 1, 6])
# TypeError: 'tuple' object does not support item assignment
# testing_tuple[1] = 9

# However, item of mutable element can be changed
testing_tuple[3][0] = 88
print(testing_tuple)
#Now just print the list
print(testing_tuple[3])

tuple1 = (1,2,3)
tuple2 = (4,5,6)
#tuple concatenation
tuple3 = tuple1 + tuple2
print(tuple1)
print(tuple2)
print(tuple3)
#tuple repetition
tuple4 = tuple3*3
print(tuple4)

#We also cannot delete or remove items from a tuple.
# TypeError: 'tuple' object doesn't support item deletion
# del tuple4[2]
#but we can delete an entire tuple
# Can delete an entire tuple
del tuple4
# NameError: name 'my_tuple' is not defined
print(tuple4)

#Tuples have two primary methods that we can use
#count(x) 	Returns the number of items x
#index(x) 	Returns the index of the first item that is equal to x
tuple5 = ('i', 't', 'i', 's', 'f', 'u', 'n', 'n', 'y')
print(tuple5.count('i'))
print(tuple5.count('v'))
print(tuple5.index('s'))
#index of a value not in the index yields an error
print(tuple5.index('t'))

#testing membership similar to lists and other collections
# In operation
print('a' in tuple5)
print('n' in tuple5)
print('g' not in tuple5)

#Using a for loop we can iterate through each item in a tuple.
for name in ('bill', 'joe', 'sally', 'xie'):
    print('Hello ' + name.title() + ' is my favorite student')

for letter in tuple5:
    print(letter)


#In Class Exercises for lists and tuples
#write a program that will accept a user input of a series of
# numbers that are separated by commas.
# Then, generate a list and tuple with the provided input.
#Each value in the comma separated list should be an element in the
#list or the tuple.

numbers = (input("please input a list of numbers seperate by commas"))
tuple_nums = numbers.split(',')
list_nums = numbers.split(',')
print(list(list_nums))
print(tuple(tuple_nums))

print("""\nAt first glance you may notice the list and tuple look the same,
but the list uses brackets and the tuple uses parenthesis.""")

#Given the following tuple (which contains two list objects).
testing_tuple = (1,2,3,4,7,9,14,[8,12,22],5,[2,3,4])
#Modify each element in the two list objects in this tuple
# by doubling the orginal values.
#Finally, print the entire tuple when finished updating the lists.
#For instance, [8,12,22] should become [16,24,44]
#Note that although a tuple is immutable, we can change a list that
#is nested in a tuple because the list is mutable.
for i in range(len(testing_tuple[7])):
    testing_tuple[7][i] = testing_tuple[7][i]*2
for j in range(len(testing_tuple[9])):
    testing_tuple[9][j] = testing_tuple[9][j]*2
print(testing_tuple)



#Given the following tuple,
t = ('a', 'b', 'c', 'd', 'e')
#use concatenation to create the following tuple:
#('A', 'b', 'c', 'd', 'e')
#Note, how the first letter in the concatenated tuple is A and not a.
#Name the new tuple t and print the result as a tuple.
#Then, print each letter on a separate line.
t = ('A',) + t[1:]
for i in t:
    print(i)



#For this question use the following two tuples:
t1 = (0, 1, 2000000)
t2 = (0, 3, 4)
#If tuple one (t1) is less than tuple two (t2),
# print a message indicating that t1 is less than t2.
#Otherwise, print a message indicating that t1 is not less than t2.
if(t1 < t2):
    print('t1 is less than t2')
else:
    print('t1 is not less than t2')


#Create a list of the two two tuple objects (t1 & t2) from the previous question.
#Your new list should only have two elements (not six elements).
#[(0, 1, 2000000), (0, 3, 4)]
#Then, print the list after adding the two tuples.
#Print the entire list together and then print the six numbers on six lines.

list1 = []
list1.append(t1)
list1.append(t2)
print(list1)
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        print(list1[i][j])


#Use the following two lists for this question.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
#Create a new list of the odd-indexed elements/items in the first list.
#Print that list along with a message indicating that these are the
# odd-indexed elements from the first list.
#Create a new list of the even-indexed elements/items in the second list.
# For this question, count 0 as an even indexed number.
#Print that list along with a message indicating that these are the
# even-indexed elements from the second list.
#Next, create a third list by picking the odd-indexed elements from the first list
# and even indexed elements from second.
#Finally, print the elements in the third list.
#Your final (new third list) list should have the following items/elements:
#[6, 12, 18, 4, 12, 20, 28]

oddlist =[]
for i in range(1,len(listOne),2):
    oddlist.append(listOne[i])
print('the odd indexed elements from listOne are:')
print(oddlist)
evenList = []
for j in range(0,len(listTwo), 2):
    evenList.append(listTwo[j])
print('the even indexed elements from listTwo are:')
print(evenList)
listThree  = list()
listThree.extend(oddlist)
listThree.extend(evenList)
print(listThree)

#For this question, use the following list:
sampleList = [34, 54, 67, 89, 11, 43, 94]
#First, print the original list.
#Second, remove the element at index 4
# and add it to the 2nd position and also to the end of the list
#After adding the elements to each position, print a message with
#the new items in the list.
#Your final list should look as follows:
#[34, 54, 11, 67, 89, 43, 94, 11]
print(sampleList)
element = sampleList.pop(4)
print(sampleList)
sampleList.insert(2,element)
sampleList.append(element)
print(sampleList)

# For this question, use the following list:
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]

#First, print the original list.
#Next, slice the list into 3 equal chunks, reverse each chunk,
# and print off each list slice.  Essentially, you are printing three
#separate lists.
#List for slice 1: [8, 45, 11]
#List for slice 2: [12, 14, 23]
#List for slice 3: [89, 45, 78]

print(sampleList)
size = int((len(sampleList)/3))
list1 = sampleList[0:size]
list2 = sampleList[size:size*2]
list3 = sampleList[size*2:size*3]
print(list(reversed(list1)))
print(list(reversed(list2)))
print(list(reversed(list3)))





#For this question, use the following tuple of lists:
portfolio= (['13-Jan-2020', 43.50, 41.50, 43.75],
            ['14-Jan-2020', 42.80, 42.15,42.90],
            ['15-Jan-2020', 42.14, 42.12,42.95],
            ['16-Jan-2020', 42.35, 41.95,42.66],
            ['17-Jan-2020', 42.15, 41.25,42.25]
           )
#The structure of each list is the
# [date, closing price, low price for the day, high price for the day]
#NOTE: These prices are in euros and not USDs,
# so try to use the euro symbol in your print statements.
#HINT: The ger-de locale currency might be helpful here!

#Using the portfolio collection, calculate the following:

#1) the max of the high prices for the week,
#2) the min of the low prices for the week,
#3) the average of the closing prices for the week,
#4) the standard deviation of the closing prices for the week,
#5) the average of the difference between high and low prices for each day in the week,
#6) the standard deviation of the difference between high and low prices for each day in the week,
#7) the percent price decline in closing price from the beginning of the week until the end of the week.

#For each calculation, print a message with the result.
# Please practice formatting the numbers in your print statements.
closing = []
low = []
high =[]
difference =[]
for x in portfolio:
    closing.append((x[1]))
    low.append((x[2]))
    high.append((x[3]))
    difference.append(x[3]-x[2])
import statistics
import locale
locale.setlocale(locale.LC_ALL, 'ger-de')
max = max(high)
print('Max: ' + max)
lowest = min(low)
print('Min: ' + lowest)
averageclose = statistics.mean(closing)
print('Average Closing: ' + averageclose)
avgdif = statistics.mean(difference)
print('The average difference between the high and low price is: ' + avgdif)
stdclose = statistics.stdev(closing)
print('The standard deviation of closing prices is ' + stdclose)
stddif = statistics.stdev(difference)
percentdecline = ((closing[4]-closing[0])/closing[0])* 100
print(percentdecline)