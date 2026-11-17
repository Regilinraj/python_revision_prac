#######################################    input() function #######################
####              print()------->display something to user
####              input()------->get something from user

#ask the user to input there name
input("Enter your name:")      #input() alone reads the users response and immediately discards it.
                               #to keep the value assign it to a variable
name=input("Enter your name: ")
print("Hello,",name)

#### static hard coded values vs dynamic values
name=input("Enter your Name:")   #dynamic value--->change each time
country="Germany"                #static value---->fixed data not change 
print("You are",name)
print(name,"comes from",country)

#how everything we learned work together

x="A"
print(x)    #A
#ask for a value
y=input("Enter value:")
print(y)    #what we give in input is the output

############################# Python Data Types ################################
###      Python needs to understand how to treat your values
###      Python automatically detect data types
###      Dynamic:Data types can change any time in python

a=10         #int
b="hello"    #str
c=True       #bool

#why data types in python

a=2  #int
b=2  #int
print(a+b)  #int + int makes addition and gives output as 4

a="2"   #str
b="2"   #str
print(a+b)     #str + str makes concatination and gives output as 22
#so to know what operation to perform, python need data types

### data types categories
###    no value--->None
###    single value(primitive data types)---->int,float,str,bool
###    multiple values---->list,set,tuple,dict

##datatypes
a=10   #int
b=3.15  #float
c="Hello"  #str
e="1234"   #str
f=True     #bool---->can be either true or false,used to handle logic and decision making
g=False    #bool
h=None     #NoneType---->means no value,used to show absense of any data
i=""       #str-->blank "" is a string value with no characters inside,it is not same as None
j=" "      #str-->white space " " is a string value with 1 or more spaces,it is not same as none

####functions---->independent block of codes
##     syntax: function_name(value)
#example:
print("hello")
type(50)

####methods----->function belonging to objects/classes
##      syntax: value.method_name()
#example:
"hello".upper()

text="hi"
number=10
print(type(text))  #type()--->built in function,return the data type of a value here output:<class str>
print(type(number))  #<class int>
print(len(text))    #len()--->built in function gives total count of items insides a value here output:2
print(len(number))   #len not work for int
print(text.upper())  #upper()--> method of <class str> convert all letter to uppercase here output:HI
print(number.upper())   #attribute error because int has no method upper()
print(number.bit_length())  #bit_length()-->method of <class int> returns length of number in binary o/p.4
print(text.bit_length())    #attribute error because its not for str

############  python challenge #############
##    create 5 variable-each with a different datatype
##      1.your age
##      2.your height with decimal
##      3.your name
##      4.are you a student
##      5.something with no value yet
##    Then print the values,data types,length of all variables

age=24
height=5.5
name="Regilin"
is_student=True
qualification=None
print("name:",name,"type:",type(name),"length:",len(name))
print("age:",age,"type:",type(age),"length:",age.bit_length())
print("height:",height,"type:",type(height))
print("is student?:",is_student,"type:",type(is_student))
print("qualification:",qualification,"type:",type(qualification))


