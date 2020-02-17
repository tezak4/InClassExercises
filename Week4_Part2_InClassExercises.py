#Find all of the locale currency options that are available
#I will use en-GB for the formatting in this example.
import locale
print(type(locale.windows_locale.values()))
for x in locale.windows_locale.values():
    print(x)
    #Our argument that we pass to the function uses dashes and not underscores
    print(x.replace('_','-'))
#Let's use the 'en-GB' locale for all currency values in these examples

#kwargs is a keyword parameter that is a dictionary type
#*args gives us a tuple with positional arguments packaged/grouped in a tuple object
#kwargs will package keyword or named parameters as a dictionary object
def process_customers (rep, cust_name, *args, **kwargs):
    """ function to practice with args and kwargs"""
    import locale
    locale.setlocale(locale.LC_ALL, 'en-GB')

    prompt = f'{rep.title} is responsible for {cust_name.title()}.  They had the following orders:\n'
    i = 0
    sum = 0
    for sale in args:
        i += 1
        sum += sale
        prompt += 'Sale #{a} was for {b}.\n'.format(a=i,
                                                    b=locale.currency(sale, grouping=True))

    prompt += 'The market characteristics are the following:\n'
    for key, value in kwargs.items():
        prompt += key.title() + ' is ' + str(value) + '\n'

    print(prompt)

process_customers ('Sally Johnson', 'wawa', 7500, 2000, 500, 1500, city='Richmond', cust_potential='high', comp_score=8)

#Notice the difference with this example here.
#We are using standard parameters and not args.
#These standard parameters can be of any data type, including a collection.
def empsales2 (a,b,c):
    import locale
    locale.setlocale(locale.LC_ALL, 'en-GB')

    prompt = f'{a.title()} had the following sales last month:\n'
    i = 0
    for x in range(0,3):
        i += 1
        prompt += 'Sale #{x} was for {y} units worth {z}.\n'.format(x=i,
                                                                    y=str(b[x]),
                                                                    z=locale.currency(c[x], grouping=True))
    print (prompt)


my_list = ['Tom Mattson']
vol = [10, 15, 20]
amt = [500.56, 1500.75, 2175.99]

my_list.append(vol)
my_list.append(amt)
print(my_list)

#unpack my_list into its three components
(a,b,c) = my_list
print(a)
print(b)
print(c)

#Now when we call empsales2 with the * unpacking operator, we will get something similar
#to the above unpacking of my_list into three variables.
empsales2(*my_list)


#Notice the differnce between the following example and our kwargs example.
def process_customers2 (chars):
    """ function to demonstarte a dictionary parameter"""
    prompt = 'The market characteristics are the following:\n'
    for key, value in chars.items():
        prompt += key.title() + ' is ' + str(value) + '\n'
    print(prompt)

my_dict = {}
my_dict['city'] = 'Richmond'
my_dict['cust_potential'] = 'high'
my_dict['comp_score'] = 8
process_customers2 (my_dict)

#Last type of function that I will discuss is a generator function.
#A Python generator is a function that produces a sequence of results by maintaining its results.
# This means that the function can resume again exactly where it
# left off if/when the function is called again.
# Therefore, you can conceptualize a generator function as a powerful iterator.

#Notice the yield instead of the typical return statement.
#Conceptualize the yield function as a "pause" button where you can continue from the
#same spot later!  This is how Python remembers the state!

import random

#First function will perform this operation without a generator function
def get_random_ints(count, begin, end):
    """let's generate a random list of integers
    param#1 = How many random numbers to create
    param#2 = Lowest possible value for our randint function
    param#3 = Highest possible value for our randint function"""
    list_numbers = []
    for x in range(0, count):
        list_numbers.append(random.randint(begin, end))
    return list_numbers

print(type(get_random_ints))
nums = get_random_ints(10, 0, 100)
for x in nums:
    print(x)

#Now let's try to do this with a generator function and a yield statement
def get_random_ints2 (count, begin, end):
    print('Starting my generator function')
    for x in range(0, count):
        yield random.randint(begin, end)
    print('Notice when this statement gets executed! Why only once instead of ten times?')

nums_generator = get_random_ints2 (10, 0, 100)
print(type(nums_generator))
for i in nums_generator:
    print(i)

#Let's work with creating files, reading data from files, and appending data to a file
file_name = 'randomfilename.txt'
handle = open(file_name, 'w')
handle.write('CustID|CustName|Gender')
handle.write('1000|Bill Jones|Male')
handle.close()

file_name = 'randomfilename.txt'
handle = open(file_name, 'w')
handle.write('CustID|CustName|Gender')
handle.write('\n')
handle.write('1000|Bill Jones|Male')
handle.close()

file_name = 'randomfilename.txt'
handle = open(file_name, 'x')
handle.write('CustID|CustName|Gender')
handle.write('1000|Bill Jones|Male')
handle.close()

file_name = 'randomfilename.txt'
handle = open(file_name, 'a')
handle.write('\n\t Appending a new indented line to the file')
handle.close()

file_name = 'randomfilename.txt'
handle = open(file_name, 'r')
for line in handle:
    print(line)
    #new_line = line.strip().replace('\n','')
    #print(new_line)
handle.close()

import csv
file_name = 'randomfilename.txt'
handle = open(file=file_name, mode='w', newline='') #keyword arguments
#use without the newline argument and then with the newline argument
#Change to mode x and notice how it errors out if the file already exists
with handle as file:
    #Change the delimiter and change the quoting option
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #quoting = csv.QUOTE_MINIMAL
    #way to write to csv file
    writer.writerow(['EmpId', 'FirstName', 'LastName', 'Email', 'Amount'])
    writer.writerow([1, 'Bill', 'Jones', 'bjones@gmail.com', 200])
    writer.writerow([2, 'Sally', 'Johnson', 'sjohnson@gmail.com', 400])
    writer.writerow([3, 'Tim', 'Smith', 'tsmith@gmail.com', 600])

handle.close()

#We can append text to the bottom of the file quite easily
file_name = 'randomfilename.txt'
handle = open(mode='a', file=file_name, newline='')
writer = csv.writer(handle, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['9999', 'Bill', 'Jones', 'email@gmail.com', 100])
handle.close()

#Now that we have a csv file, we can easily read in the data using the reader function!
file_name = 'randomfilename.txt'
handle = open(file_name, 'r')
reader = csv.reader(handle, delimiter=',')
print(type(reader))
rows = list(reader)
print(type(rows))
print(rows[0])
print(rows[1])
handle.close()

file_name = 'randomfilename.txt'
handle = open(file_name, 'r')
with handle as f:
    data = csv.reader(f)
    for row in data:
        print(row)
handle.close()

file_name = 'randomfilename.txt'
handle = open(file_name, 'r')
my_list = []
with handle as f:
  data = csv.reader(f)
  for row in data:
        my_list.append(tuple(row))
print(my_list)
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])
handle.close()

file_name = 'randomfilename.txt'
handle = open(file_name, 'r') #r should be the default
#This should put everything EXCEPT the header into a dictionary object
reader = csv.DictReader(handle)
my_list = []
for raw in reader:
    my_list.append(raw)
print(my_list)
my_dict = my_list[1]
print(my_dict)
print(f'Employee number {my_dict["EmpId"]} is {my_dict["FirstName"]} {my_dict["LastName"]}')
handle.close()

#Activities/Exercises
#Build a function to accept an args argument as well as a kwargs argument as two parameters.
#The args should be the sales for the month
#The kwargs should contain two sales goals (goal1 and goal2).
#Your function should return how far over or under the goal (sum of goal1 plus goal2 in the **kwargs)
#Finally, print off an appropriate message depending on whether the salesperson
# achieved their sales goals, did not achieve their sales goals or exactly hit their sales goals.
#The sales are in British Pounds and not USDs so make sure you print the appropriate currency symbol
#in your printed out message.

def function(*args, **kwargs):
    goal = kwargs['goal1'] + kwargs['goal2']
    sales = 0
    for x in args:
        sales += x
    dif = sales-goal
    if dif == 0:
        print(f"Congratulations you sold exactly {goal}, which was your goal")
    elif dif > 0:
        print(f'Congratulations you beat your goal of {goal} by {dif}')
    else:
        print("Unfortunately you did not reach your goal!")
function(45,78,90,100,40, goal1=200, goal2=45)


#Create a function to generate a text file containing 100 random rows.
#The file should have three columns (with the header row as the first row in your file)
#SaleId, which should be a sequence starting with 1.
#Units, which should be a random integer between 10 and 25
#Amount, which should be a random integer between 1000 and 10000
#Your function should accept two paramters. The first should be the filetype, which contains the delimiter
#and the second should be the file name.
#Finally, call the function to generate the file!

def filegenerator(ftype, file_name,):
    import csv
    import random
    handle = open(file=file_name, mode = 'w', newline='')
    with handle as file:
        writer = csv.writer(file,delimiter = ftype,quotechar ='"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(['SaleId','Units','Amount'])
        for x in range(1,101):
            writer.writerow([x,random.randint(10,15),random.randint(1000,10000)])
    handle.close()
filegenerator('|','sales.txt')

#Build a function to read in the text file that you created in the previous function.
#The function should determine the per unit amount for each sale
#and then display the average and standard deviation of the per unit amount for all of the transactions.
#Your function should take in the delimiter type and the file_name as parameters (same as the previous function).
#Finally, call your function!

def perunit(ftype, file_name):
    import csv
    import statistics
    import locale
    handle = open(file_name,'r')
    with handle as f:
        my_list =[]
        data=csv.reader(f,delimiter=ftype)
        for row in data:
            if row[0] != 'SaleId':
                my_list.append(float(row[2])/float(row[1]))
        avg = statistics.mean(my_list)
        stdev = statistics.stdev(my_list)
        print(f'The average per unit amount across the 100 transactions was {avg} with a standard deviation of {stdev}')
perunit('|', 'sales.txt')
#Build a function to add (append) a user specified number of rows to the text file that you previously made.
#This function should have the same two parameters as the previous two functions plus a parameter to accept
# an argument for the number of rows to add to the file.
# The units for the new rows should be a random integer between 10 and 25.
# The Amount should be a random integer between 1000 and 10000.
# The SaleId should continue with the sequence of numbers.
#After you define the function, call it!
#Finally, recall the previous function to recalculate the averages.

def addrows(ftype,file_name,numrows):
    import csv
    import random
    handle = open(file_name,'r')
    data = csv.reader(handle,delimiter = ftype)
    my_list=list(data)
    seq = len(my_list)
    handle.close()
    handle = open(file_name,'a',newline='')
    writer = csv.writer(handle,delimiter =ftype,quotechar = '"',quoting = csv.QUOTE_MINIMAL)
    for x in range(numrows + 1):
        writer.writerow([seq,random.randint(10,25),random.randint(1000,10000)])
        seq += 1
        handle.close()
addrows('|','sales.txt',5)
perunit('|','sales.txt')




#Use a generator function to create a Fibonacci series of numbers.
#This is a series of numbers in which each number (Fibonacci number)
# is the sum of the two preceding numbers.
# The simplest is the series 1, 1, 2, 3, 5, 8, etc.
#After you build the generator function, call the function a few times
# to see if the function is working!
def fibonacciGenerator():
    a=0
    b=1
    while True:
        yield b
        a,b =b,a+b
obj = fibonacciGenerator()
print(type(obj))
print(next(obj))
print(next(obj))
print(next(obj))
