#These tasks represents tasks that you should probably be able to do without looking
#up how to do them on the Internet.

#1. Ask the user to enter their name and print a message that says 'Hello, {name}!
name = input("Please enter your name")
print('Hello, {}'.format(name))

#2. Modify the previous program/statement to convert the users name to title case.
name = input("Please enter your name").title()
print('Hello, {}'.format(name))
#3 Create a variable and assign the value of 6 to it.
#  Multiply that value by 22 and print out the result with a user-friendly message such as
#  The value of 6 multiplied by 22 is 132.
num = 6
newnum = 6*22
print("The value of {} multiplied by 22 is {}".format(num,newnum))


#4. Ask the user to enter two integer values.
#   Perform a floor division of the first number (numerator) and the second number (denominator)
#   Then, print out the result
num1 = int(input('Please enter an integer value'))
num2 = int(input("Please enter an integer value"))
divided = (num1 // num2)
print(str(divided))



#5. Ask the user for two integer values.
#   Divide the first number by the second number.
#   Then, print off a message that reads something like the following:
#   19 divided by 10 equals 1 with a remainder of 9.
num_1 = int(input('Please enter an integer value'))
num_2 = int(input('Please enter an integer value'))
remainder = num_1 % num_2
divided = (num_1 // num_2)
print('{} divided by {} equals {} with a remainder of {}'.format(num_1,num_2,divided,remainder))



#6. In the previous program, if the user enters a string (text) instead of integers,
#   print a message (instead of the traceback message) such as the following:
#   Please enter integers instead of text.
try:
    number1 = int(input('Please enter an integer value'))
    number2 = int(input('Please enter an integer value'))
    remainder = number1 % number2
    divided = number1 // number2
    print('{} divided by {} equals {} with a remainder  of {}'.format(number1,number2,divided,remainder))
except:
    print('You must enter an integer value')




#7. Ask the user to enter a sentence.
#   Print the sentence with just the first word in the sentence capitalized.
#   'Hello my name is tom.'
#   Then, print the sentence with each word capitalized.
#   'Hello My Name Is Tom.'
#   Then, print the sentence with each word in lower case and again with each word in all capital letters.
sentence = input("Please enter a sentence")
print(sentence.capitalize())
print(sentence.title())
print(sentence.lower())
print(sentence.upper())



#8.  Ask the user to enter a word.
#   Print a message indicating the length of the word.  For instance, enter the following message:
#   You entered 'Hello', which is 5 characters long.
word = input("please enter a word")
length = len(word)
print('You entered \'{}\', which is {} characters long'.format(word,length))




#9.  Set a variable equal to the following string: 'We are learning python to eventually learn machine learning.'
#    Then, print off just the word Python with a capital P.
#    Then, print off the words machine learning with a capital M and capital L.
sentence = "We are learning python to eventually learn machine learning"
print(sentence[16:22].capitalize())
print(sentence[43:].title())

#10. Create a variable with the following string:
#    I told my friend, "Python is my favorite language!" with the quotation marks
#    Then, print out that variable.
#    Next, reassign the value of your variable to:
#    The language of 'Python' is named after Monty Python, not the snake with Python in single quotations.
#    Then, print out that variable.
#    Next, reassign the value of your variable to:
#    One of Python's strengths is its diverse and supportive community with the apostrophe.
#    Then, print out that variable.

sentence = "I told my friend, \"Python is my favorite language!\""
print(sentence)
sentence = "The language of \'Python\' is name after Monty Python, not the snake"
print(sentence)
sentence = "One of Python\'s strengths is its diverse and supportive community"
print(sentence)




#11. Create a variable to store my first name ('Tom') and a second variable to store my last name ('Mattson')
#    Then, create a third variable that concatenates the two names together with a space between the names.
#    Then, print the third variable
first = 'Tom'
last = 'Mattson'
full = first + " " + last
print(full)




#12. In the previous program, instead of creating a third variable, combine the first two variables in a print
#    statement.  Try to do this multiple ways!
print(first + ' ' + last)
print('{} {}'.format(first,last))
print(f'{first} {last}')
print('%s %s' %(first,last))




#13. Print the following with the tabs and the returns:
#Courses:
#   MGMT325
#   INFO201
#   INFO303
print("Courses: \n \tMGMT325 \n \tINFO201 \n \tINFO303")

#14.  Using the following variable:
fav_course = '          INFO 303           '
#   First, print the variable with the leading spaces stripped
#   Second, print the variable with the trailing spaces stripped
#   Thirs, print the variable with both the leading and trailing spaces stripped
print(fav_course.strip())
print(fav_course.rstrip())
print(fav_course.lstrip())

#15. Ask the user to enter two numbers.
#    Use a try/except block to handle the possibility that the user enters text instead of numbers in their response.
#    Then, add the two numbers together and print the result.
#    Then, multiply the two numbers together and print the result.
#    Then, subtract the two numbers (first - second) and multiply that difference by 7 and print out the result.
#    Then, divide the two numbers (first number is the numerator), raise that result to the fourth power
#    and print out the result.
#    For the last calculation, print out the data type.
#    Finally, add a docstring comment at the start of your answer
"""This does various calculations with user inputs numbers"""
try:
    int1 = int(input("Please enter an integer"))
    int2 = int(input("Please enter an integer"))
except:
    print('You must enter an integer value')
add = int1+int2
print(add)
multiply = int1*int2
print(multiply)
dif7  = (int1-int2) * 7
print(dif7)
fourth = (int1/int2)**4
print(fourth)
print(type(fourth))




#16. Ask the user to enter a number.
#    If the number is greater than or equal to 25, print an appropriate message.
num = int(input("Please input a number that is greater than or equal to 25"))
if num >= 25:
    print('Thank you')
else:
    print('You must enter a number greater than or equal to 25')


#17. Ask the user to enter a number.
#    If the number is between 15 (inclusive) and 40 (inclusive), print an appropriate message.
num = int(input("Please input a number between 15 and 40 (inclusive)"))
if(num >= 15) and (num <= 40):
    print("Good job")
else:
    print("You must enter a number between 15 and 40")



#18. Ask the user to enter either tom, bill, joe, or sally.
#    If they enter, bill (in any case), then print an appropriate message.
name = input("Please enter Tom, Bill, Joe, or Sally").lower()
if(name == 'bill'):
    print("Good job you input Bill")
else:
    print("You should have input Bill")




#19. Ask the user to enter either tom, bill, joe, or sally.
#    If they enter, bill (in any case) or tom (in any case), then print an appropriate message.
name = input("Please enter Tom, Bill, Joe, or Sally").lower()
if(name == 'bill') or (name == 'tom'):
    print("Good job you chose {}".format(name.capitalize()))
else:
    print("You should have chosen Tom or Bill")


#20. Ask the user to enter two numbers.  Divide the first number by the second number.
#   If the result is greater than 4, print an appropriate message.  For instance:
#   16.0 divided by 3.0 is 5.33, which is greater than 4
#   Otherwise, print an appropriate message.  For instance,
#   16.0 divided by 4.0 is 4.0, which is not greater than 4
#   Make sure the result of the division in your message is formatted with a reasonable number of decimal places.

num = int(input("Please enter a number"))
num1 = int(input("Pleae enter another number"))
divided =(num/num1).__round__(4)
if(divided > 4):
    print('{} divided by {} is {}, which is greater than 4'.format(num,num1,divided))
else:
    print("{} divided by {} is {}, which is not greater than 4".format((num,num1,divided)))






#21. Ask the user to enter two numbers.  Raise the first number to the second number.
#    Using a single if conditional, check for the following:
#    If the result is between 0 and 500 (inclusive of both numbers), print an appropriate message.
#    If the result is greater than 500, print an appropriate message.
#    For all other values (i.e., negative numbers), print an appropriate message.
#A sample message for one of the conditions would be the following:
#-7.0 raised to the power of 3.0 is -343.0, which is negative (less than zero)

num = int(input("Please enter an integer"))
num1 = int(input("Please enter an integer"))
raised = num**num1
if(raised >= 0) and (raised <= 500):
    print('{} is between 0 and 500'.format(raised))
elif(raised > 500):
    print(f'{raised} is greater than 500')
else:
    print(f'{raised} is a negative number')



#22. Ask the user to enter two words.
#    If the length of the first word is longer than the second word, print an appropriate message.
#    Otherwise, print an appropriate message.
# A sample message would be the following:
#The first word of 'doggy' is 5 characters long, which is longer than the second word of 'cat' that is 3 characters long.
word = input("Please enter a word")
word2 = input("Pleae enter another word")
if(len(word) > len(word2)):
    print(f'The first word is {word}, which is longer than {word2}')
else:
    print(f'The first word is {word}, which is not longer than {word2}')



#23. Ask the user to enter two words.
#    If the two words are equal (do not change the case that the user enters), enter an appropriate message.
#    Otherwise, print an appropriate message.
# A sample message would be the following:
#The first word of 'doggy' is equal to the second word of 'doggy'.
word = input("Please enter a word")
word2 = input("Please enter another word")
if(word == word2):
    print(f'The first word of {word} is equal to the second word of {word2}')
else:
    print(f'The first word of {word} is not equal to the second word of {word2}')



#24. Modify the previous question to compare the two words, regardless of case.  Therefore,
#    dog should equal 'Dog' for this question.
word = input("Please enter a word").lower()
word2 = input("Please enter a word").lower()
if(word == word2):
    print(f'The first word of {word} is equal to the second word of {word2}')
else:
    print(f'The first word of {word} is not equal to the second word of {word2}')


#25. Ask the user to enter a word.
#    If the word contains the letter r and the letter a, then print an appropriate message.
#    Otherwise, print an appropriate message.
word = input("Please enter a word").lower()
if(word.__contains__('r')) and (word.__contains__('a')):
    print("The word {} contains both \'a\' and \'r\'".format(word))
else:
    print("The word {} does not contain both \'a\' and \'r\'".format(word))



#26. Check whether two strings are equal even if the order of words or
#    the characters are different.  To do this comparison, ignore the case of the words.
#    For instance, consider this string:
#    Str1 = “Hello and Welcome”
#    Str2 = “welcome and Hello”
#    These two should be the same!
#    If the two strings are the same, then print an appropriate message.
#    Otherwise, print an appropriate message.
#    For this question, use the following two variables!
#    After testing your code with these two strings, modify them so they are not equal.
word = "Hello and Welcome"
word2 = "Welcome and Hello"
if(sorted(word.lower()) == sorted(word2.lower())):
    print(f'Both strings are the same')
else:
    print(f'Both strings are NOT the same')



#For the next series of problems, use the random module.
#27  Print the help for random.random.
#    Generate a random real number number between 0 (inclusive) and 1 (not inclusive)
#    If the number is less than 0.5, print an appropriate message.
#    Otherwise, print a different message.



#28   Print the help for random.randint.
#     Generate a random integer between -15 and 15.
#     If the number is zero, print an appropriate and user-friendly message with the percent chance
#     that the number would be exactly equal to zero.
#     If the number is negative, print an appropriate and user-friendly message with the percent chance
#     that the number would be negative.
#     If the number is positive, print and appropriate and user-friendly message with the percent chance
#     that the number would be positive.  Within this positive condition, do the following:
#           Pick another random integer between 5 and 10.
#           Then, raise the first random number to the power of the second random integer.
#           Then, print the result with an appropriate and user-friendly message.





#29  Create a list containing four names.
#    Have the computer randomly choose one of those names.
#    Then, print an appropriate and user-friendly message.




#30. Modify the previous example.  If the computer automatically selected the first or third item
#    in the list, print an appropriate and user-friendly message such as 'I was hoping for one of
#    these values was'.  Otherwise, print a different
#    user-appropriate message such as 'I was hoping for one of the other options.'



#31.  Generate a random sample (n=5) from the following list.
#    Then, print out the random sample with an appropriate and user-friendly message.!
my_list = [20,40,80,100,120,33,45,65,85, 97,109,123]



#32.  Modify the previous example, to ask the user to enter the sample size.
#    Check to make sure the sample size is less than the size of the list!
#    If less than the size of the list, generate the random sample.
#    Otherwise, print a message that indicates that your sample size is too big.
my_list = [20,40,80,100,120,33,45,65,85, 97,109,123]



#33.  Have the user enter three numbers.
#     Check whether the first number is greater than the second number
#     and whether the second number is greater than the number.
#     If so, print an appropriate user-friendly message.
#     If not, print an appropriate user-friendly message.




#34.  Ask the user to enter a number.
#     Check whether that number is not equal to zero.
#     If so, check if the number is positive and print an appropriate user-friendly message.
#     If not, print an appropriate user-friendly message.
#     If user enters a zero, then print an appropriate user-friendly message.




#35.  Ask the user to enter a year and a month.
#     Enter the year: 2020
#     Enter the month: 4
#     Then, print a message determining how many days in the month.  For instance,
#     There are 30 days in this month
#     First, check whether we are in a leap year by checking the following:
#     Year MOD 4 equals zero and year MOD 100 not equal to zero and year MOD 400 equals zero.
#           Then, within the leap year, perform a conditional test on the month that the user entered
#           to determine the number of days in the month.
#           Also account for a user entering an invalid month (i.e., a 13 or 14).
#     If we are not in a leap year, perform a conditional test on the month that the user entered
#           to determine the number of days in the month.
#           Also account for a user entering an invalid month (i.e., a 13 or 14).
#     If the user enters an invalid year, print a message indicating that the user entered an invalid year.



#36. Build a list of at least four car manufacturers.
#    Print the third element in the list.
#    Print the last item in the list.  For this task, do this in multiple ways.


#37. Using the previous list, print out the second element in the list in all capital letters.


#38. Using the previous list, modify the fourth item to a different manufacturer.
#    Then, print off the new fourth item in title case.
#    Then, print off the entire list.


#39. Using the previous list, delete the fourth item.


#40. Using the previous list, add a manufacturer to the last position and print the list after you add the item.


#41. Using the previous list, add a manufacturer to the second position and print the list after you add the item.


#42. Using the previous list, delete the last item in your list and print the list after you remove that item.



#43. Using the below list, delete the item with the value of 'tom' without referencing the indexed position.
#    When finished, print the list
names = ['bill','joe','sally','sue','tom', 'tim', 'violet']


#44. Using the below list, reverse the order of the list and then print the list.
#    Next, permanently sort the items in ascending order and then print the list.
#    Next, permanently sort the items in descending order and then print the list.
cars = ['ford', 'honda', 'gm', 'nissan', 'toyota', 'bmw', 'tesla']

#45.  Using the below list, create a variable to store the length of the list.
#     Then, try to use that variable to reference the last item in the list.  Notice how you get an error!
#     Handle that error by printing a user-friendly and appropriate message.  Then, print the last
#     element/item in the list using two different methods.
cars = ['ford', 'honda', 'gm', 'nissan', 'toyota', 'bmw', 'tesla']


#46. Using the below list and variable, check if the value stored in the variable is
#    contained in the list.  If so, print an appropriate message.  If not, print an appropriate message.
#    After you find that the value is not contained in the list, build another if statement to handle the
#    difference in case (i.e., capital F instead of lower case f)
cars = ['ford', 'honda', 'gm', 'nissan', 'toyota', 'bmw', 'tesla']


#47. Check if the following list is empty!  If so, print an appropriate and user-friendly message.
#    If not, print an appropriate and user-friendly message.
cars = ['ford', 'honda', 'gm', 'nissan', 'toyota', 'bmw', 'tesla']


#48.  Clear the list from the previous question and perform the is empty check again.


#49.  Create a list of numbers from 1 to 1000 and print the values


#50.  Create a list of odd numbers from 500 to 600.  Then, print the values.
#     Create a list of even numbers from 500 to 600.  Then, print the values.
