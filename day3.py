################################### strings ##############################################
##         "abc",'maria',"india","997899"
## why is handling string data important?
##        Text is everywhere--filenames,user input,web data,logs
##   Text data often has poor quality.Text often holds valuable information.

########## string---->types--->type(),str()

##################  type()---->built-in function    ###

name="Regilin"
print(type(name))   #type(value)-->built-in function,o/p:type,return the data type of a value
#output:<class str>

########### str()

age=24
print(type(age))      #<class 'int'>
#print("Your age is: "+age)    #TypeError-->because we cannot add string and int.so we use str() for converting int to str

age=24
print("Your age is:"+str(age))  #str(value)-->built-in function,o/p:string,converts any value into string value
#output:Your age is 24

age=age+5
age=str(age)
print(type(age))  #<class 'str'>
#age=age+5         #type error-->str +int

############ string---->math---->len(),count()

##############        len()

## use case->check password  quality-->makesure the password meets minimum length requirements
password="1234"
print(len(password))   #len(value)-->built-in function,o/p:int,returns the number of items in a value,returns the number of characters in a string
#output:4

password="1234a34443"
print(len(password))    #10

##use case->validate input length-->prevent values that are too short or too long
password="123455"
if len(password)<8:
    print("Your password is too short")  #Your password is too short

password="   1234   "
print(len(password)) #output:10 ,len() counts everything even spaces

########################    count()

##use case->work frequency check-->counts how many time a specific word appear
text="""
Python is easy to learn$,
Python is powerful.
Many people love python.
"""
print(text.count("Python")) #count(substring)->str method,o/p:int,returns how often a word appears in the string
#output:2-->we have 3 python.why output is 2?->python is case sensitive, means uppercase and lowercase letters are treated as different

##use case->Detect quality issues->count how many unwanted characters in my data
print(text.count("$"))  #1

#############  strings----->Transformations

##########################  replace()

##   "2026/05/10"-->if we want to replace / with - we use replace()--->old value / & new value -

## use case->clean numeric formats-->replace commas with dots in european style decimal numbers

#transformations
price="1234,56"
print(price.replace(",","."))   #replace(old,new)-->str method,0/p:str,swaps part of the text with something new
#output:1234.56

## use case->change phone number format-->replace special characters with something else

phone="176-11233-678"
print(phone.replace("-","/"))    #output:176/11233/678

# replace() not just for changing values.you can also remove unwanted parts by replacing them with an empty strin ""

## use case->clean phone numbers-->remove special characters from phone number
phone="145-567-6778"
print(phone.replace("-",""))   #output:1455676778

# we can also remove something and add space
print(phone.replace("-"," "))  #output:145 567 6778

##use case->clean numeric formats-->remove symbols and commas to prepare for numeric conversion
price="$1,299.99"
print(price.replace("$","").replace(",",""))   #1299.99

############# python challenge #############

###    convert the messy phone number into a clean number format with only digits
###        "+49 (176) 123-4567"
###        output:00491761234567

phone_number="+49 (176) 123-4567"
print(phone_number.replace("+","00").replace(" ","").replace("(","").replace(")","").replace("-",""))
#output:00491761234567

########################## Join strings ##################################
##     'string'+'string'-->operator,o/p:string,joins(concatinates) two strings into one

#Transformations
first_name="Michael"
last_name="Scott"
last_name=first_name+"-"+last_name
print(last_name)
#output:Michael-Scott

##use case->build file paths-->build dynamic paths using folder and file variables

folder="C:\\users\\Regilin\\"
file="report.csv"
full_file=folder+file
print(full_file)
#output:C:\users\Regilin\report.csv

################################### f-string #####################################
##   modern,super easy way to format and build strings
##   f stands for "formatted"
##   lets you easily put variables and expressions directly inside string value

name="sam"
age=34
is_student=False
print("My name is"+name+"Iam"+str(age)+"years old,and student status is"+str(is_student)+".")
#   |->hard to read--->There are lots of plus signs and you have to worry about spaces and types.so we use f-string.
#output:My name issamIam34years old,and student status isFalse.
print(f"My name is {name},Iam {age} years old,and student status is {is_student}.")
#output:My name is sam,Iam 34 years old,and student status is False.

print(f"2+3={2+3}")  #output:2+3=5
##if we want to print with {}
print(f"{{This is me}}")  #output:{This is me}

############################ split() ##########################
##  split one string into multiple string values.one string given,multiple strings in a list comes as output.
##    "Adam-24-USA"----->split("-")---->["Adam","24","USA"]

##Transformations
##use case->separate date from time

stamp="2026-09-20 14:30"
print(stamp.split(" "))   #split(separator)-->str method,o/p:list of strings,breaks a string into smaller parts
#output:['2026-09-20', '14:30']

##use case->break a date into year,month and day parts

stamp="2026-09-20"
print(stamp.split("-"))
#output:['2026', '09', '20']

##use case->break comma separated values into individual items

csv_file="1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))
#output:['1234', 'Max', 'USA', '1970-10-05', 'M']


############################# string repetition #########################
##   'string'*number-->operator,o/p:string,repeat the string multiple times

print("ha"*3)   #output:hahaha

##use case->style your logs->use repeated characters to create clean sections in output
print("="*20)   #output:====================

##################### Data extraction #####################
############### Indexing 
## hello-->sequence of characters,has a position number(index)
##Two types of indexes: positive index and negative index
## positive index->left to right->0,1,2,3....
## negative index->right to left->-1,-2,-3,...


################# slicing
##  group of characters
##  [start,end]-->start included,end not included,example:'hello'[0:3]  output:hel
##  open ended slicing:->start from specific position and include everything after it no need to mention end
##    example:'hello'[1:]  output:ello
##another one:[start:end:step]
##   example:'hello'[0:4:2]   output:hl

##indexes and slicing
#indexing-->'string'[index]-->operator,o/p:string,extracts one character by position

text="Python"
#extract the first character
print(text[0])  #output:P
#extract the last character
print(text[-1])  #output:n
#extract h
print(text[3])  #output:h

##slicing-->'string[start:end:step]->opertor,0/p:string,extract a part of the string

date="2026-09-20"
#extract the year
print(date[0:4])   #output:2026
#in another way we can do->open ended slicing
#open ended slicing-->if you leave the start index empty,python starts from index 0
print(date[:4])    #output:2026
#extract the month
print(date[5:7])   #output:09
#extract the day
print(date[-2:])   #output:20

## when to use positive or negative index?
## positive index-->if you want to extract part from the left side (start) of a string
## negative index-->if you want to extract part from the right side (end) of a string






