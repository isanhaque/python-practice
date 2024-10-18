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