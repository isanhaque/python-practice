#This is a note/comment
print("Hello I am learning Python")
#print("these are my examples when I am coding")
print("item cost")
#give a 20% discount
print( (25*4) * 0.8 )

print("funds to send:", 225/5 + 600*8 + 144/12)
#the module (%) gives you the remainder of the division presented in the syntax
print("you get:", 53%4)
print("you now get:", 51%3)

print(30/4)
#see how you can use // to round down instead of getting a remainder
print(30//4)


#learn symbols (logical operators, conditionals), data types, data structures (arrays, sets, tuples, dictionaries),
# for loops, while loops, scope, functions, object-oriented programming
#Turn off the ai/autocomplete
#for html/css and javascript use vscode
#copy-paste the code here into practice.py to see how it works individually
#use web3schools as a resource https://www.w3schools.com/python/default.asp
#make a github account and linkedin account

letter = "string" # this is a string
number = 3 #this is a number
boolean = True #this is a boolean
decimal = 3.22452 #this is a float
print(letter)
print(number)
print(boolean)
print(decimal)


print("conditionals")
number = 4
decimal = 3.22453 #this is a float
decimal2 = 3.00
print(1>2)
print(number == decimal)
print(number == decimal2) #why does this return true

if number > 2:
    print("number is greater than 2")
else:
    print("number is less than 2")
#try changing the number to see if you can get to the else condition

string = "Hello world"
if string == "Hello world":
    print("this string says hello world")
elif string == "foo bar":
    print("this string says foo bar")
else:
    print("I don't know what the string says")
#change string to foo bar and see what happens

print("data structures")

print("list")
nums = [1,2,3,4,5] #data type: list
print(nums[1])

print("set")
nums2 = {1,2,3,4,5} #data type:set
print(nums2)
nums2.add(3)
print(nums2)

print("dictionary")
nums3 = { # data type: dictionary
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
}
print(nums3)
print(nums3.keys())
print(nums3.values())
print(nums3["first"])
print(nums3["second"])
print(nums3["third"])


print("tuple")
nums4 = (1,2,3,4,5) #data type: Tuple
print(nums4)
print(nums4[0])
#nums4.add(2) uncomment this. Research why there is an error


print("for loop")
for i in range(len(nums)): #for key word for starting for loops, i is an iterator (search up what this means),
    # range is how much the for loop will go through, len calculates the length of the thing inside
    print(nums[i])
    #this is the body of the function, whatever you do in here will happen for each thing you iterate over.
    #make a for loop that adds all the numbers

print("while loop")
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
#learn about linked lists, stacks, queues, binary trees, heaps, hashmap



print("functions")
#functions
def add(num): #def key word to start function, add is the name of the function
    #inside the parenthesis are parameters, research what that means
    return num+1
    #function body, whatever you do in here is what the function does
    #make a function that returns the sum of all numbers in an array that is passed in as the parameter

print(add(1))

#first project
#make a todo list app
#must use 3 functions
#displays menu to let user add delete complete tasks
#clear option



#move onto learning javascript





