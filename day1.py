print("Hi,this is my first python code")

################################## comments ########################################

#This is a single line comment

#store the final exam score
x=10

#This is inline comment
x=9 #final exam score

###################################   print() Function  ###################################

print("Hi")
print("Hi python")
print('hello python')
#print("hi')------->syntax error
print("------------------------------------")
print("...........Learn python.............")
print("------------------------------------")

##############   Escape sequence  #############

####     \" -------->Double quote
####     \' -------->single quote
####     \\ -------->backslash
####     \n -------->new line
####     \t -------->tab
####     \b -------->backspace

#print("Hi,"Python"")--------->invalid syntax error
## for this we use escape sequence \"
print("Hi,\"Python\"")      # Hi,"Python"

#same like this we use \'
print('Hi,\'Python\'')      # Hi,'Python'

#print("Path:C:\users\Regilin")---------->syntax error beacuse backslash is special
# so solve this error by using the \\
print("Path:C:\\users\\Regilin")         #Path:C:\users\Regilin

print("Message1")
print("Message2")
#if we want blank line between two messages we can use print()
print("Message1")
print()
print("Message2") # this works but we have better option

#another way we use \n
print("Message1\n")
print("Message2")

#we can also make as much blank line as we need
print("Message1\n\n\n")
print("Message2")

#we can also give it in single line
print("Message1\n\nMessage2")

#for making a tab space in between we use \t
print("message1\tmessage2")

####print() challenge
###    use print() to recreate this exact output
###    you are allowed to use only one print()
###    
###    Your Learning path:
###           -Python Basics
###           -Data Engineering
###           -AI

print("Your Learning path:\n\t-python basics\n\t-Data Engineering\n\t-AI") #this prints correctly but we can use another way """ """

print("""Your learning Path:
    \t-python basics
    \t-Data Engineering
    \t-AI""")    #here no need for \n 

##########################################    variables #######################################
x=1
print(x)   #1
x=2
print(x)   #2
y=x+3
print(y)   #5

print("My name is regilin")
print("Regilin is learning python")
print("Regilin wants to become python expert") #if we want to change the name regilin to rejichia then its difficult we have to change in each line so we use variables to make it easy

#using variable to make it easy to update
name="Rejichia"
language="python"
print("My name is",name)
print(name,"is learning",language)
print(name,"wants to become", language, "expert") # now we only change in variable then it automatically update in all lines


####### python challenge
##    Print the following three lines
##    Add a variable to make it dynamic
##
##    info@datawithregilin.com
##    support@datawithregilin.com
##    www.datawithregilin.com

name="datawithregilin.com"
print("info@",name)
print("support@",name)
print("www.",name)