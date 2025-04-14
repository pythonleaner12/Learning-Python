### Let's assign 10 to my_number ###
my_number = 10
print(my_number)

### Whole Numbers and Decimals ###

age = 11
print("Age:", age )
print('Type of Class:', type(age),)

 # Decimals (Float) #

pi = 3.1415926535
print('Value of pi:', pi)
print('Type of Class:', type(pi))

### Text (String) ###

# Example 1: Connect Strings #

name = "Bryan"
last_name = "Robledo"
message = "Hello, " + name + ' ' + last_name + "!"
print(message)
# Example 1.5: What a Difference F-Strings Truly Make #

something = f"Hello, {name} + {last_name} + !"
print(something)

# Example 2: Connect Strings With Numeric Values

name_2 = "Jazmine"
age = 3
message_2 = "Hello, " + name_2 + ", you are " + str(age) + " years old!"
print(message_2)

# Example 2.5: What a Difference F-Strings Truly Make #

somethingelse = f"Hello, {name_2}, you are {age} years old!"

# Example 3: Basic F-String Usage #

name_3 = "Melanie"
last_name_2 = "Chavez"
messsage_3 = f"Hello, {name_3} {last_name_2}!"
print(messsage_3)

# Example 3.5: What a Difference F-Strings Truly Make #
message_plus = "Hello, " + name_3 + " " + last_name_2 + "!"
messsage_3 = f"Hello, {name_3} {last_name_2}!"

print(messsage_3)
print(message_plus)

# Example 4: F-Strings With Numeric Values #

name_4 = "Jimmy"
age = 39
message_4 = f"Hello, {name_4} you are {age} years old!"
print(message_4)

# Example 4.5: What a Difference F-Strings Truly Make #

message_plus_again = "Hello, " + str(name_4) + " you are " + str(age) + " years old!"
message_4 = f"Hello, {name_4} you are {age} years old!"

print(message_4)
print(message_plus_again)

# Example 5: F-String With Expressions and Calculations #

a = 5
b = 3
math_message = f"The sum of {a} and {b} is {a + b}."
print(math_message)

# Example 5.5: What a Difference F-Strings Truly Make #

math_plus = 'The sum of ' + str(a) + " and " + str(b) + " is " + str(a + b) + "."
math_message = f"The sum of {a} and {b} is {a + b}."

print(math_message)
print(math_plus)

### Booleans (Bools) ###

# Example 1: (Basic) Represent Values of True and False in a Variable #

is_student = True
print(is_student)
print(type(is_student))

# Example 2: Comparisons #
a = 10
b = 5

print(a > b)  # True, because 10 is greater than 5
print(a == b) # False, because 10 is not equal to 5
print(a < b)  # False, because 10 is not less than 5

# Example 3: Using Logical Operators #

x = True 
y = False

# 'and' operator (returns True only if both are True)
print(x and y) # Output: False

# 'or' operator (returns True if at least one is True)
print(x or y) # Output: True

# 'not' operator (inverts the Boolean value)

print(not x) # Output: False
print(not y) # Output: True

# Example 4: Bools With Conditions #

bool_age = 38
if bool_age >= 18:
    print(("You are an adult!"))    
else: 
    print("You are not an adult yet!")    

# Example 4: Can I Go Outside and Play? #

homework_done = True
weather_is_sunny = False

if homework_done and weather_is_sunny:
    print("You can go outside and play!")
else:
    print("You cannnot go outside and play.") 

# Example 5: Access to Python #

permmision = False
is_of_older_age = True

if is_of_older_age or permmision:
    print("Access Allowed!")
else:
    print('Access Denied.')    

# Example 6: Time for Bed #

night_time = True 

if not night_time:
    print("You can still play outside!")
else:
    print("Time for bed!")

# Example 7: Traffic Light #

red_light = True
cars_present = True

if red_light and cars_present:
    print("Don't cross the street!")
else:
    print("You can cross, just be careful!")    

# Example 8: Exam Results #

grade = 100

if grade >= 90:
    print("Exelllent Work! You get an A+!")
elif grade >= 80: 
    print("Good job! You got a B.")
elif grade >= 70:
    print("Ok, you passed. You get a C.")
else:
    print("Make sure to study next time!")

# Example 9: The Door #

closed_door = True

if closed_door:
    print("You can't enter")
else:
    print("You may pass")

# Example 10: Do You Have Permission to Play Outside? #

outside_permmision = False

if outside_permmision:
    print('You may go outside and play!')
else:
    print("You don't have permmision to go outside and play!")

# Example 11: Are You of Age?

new_bool_age = 11

if bool_age >= 18:
    print(("You are an adult!"))    
else: 
    print("You are not an adult yet!")  

# Example 11: Secret Password

correct_password = input("Type Password: ")

if correct_password == "python123":
    print("Access Granted")
    print("You have access to Python.org.")
else:
    print("Access Denied")    
