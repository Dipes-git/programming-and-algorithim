# # 1. Take 3 numbers and print the largest number
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
if num1>num2 and num1>num3:
    print("num1 is greater")
elif num2>num3 and num2>num1:
    print("num2 is greater")
else:
    print("num3 is greater")
# #####################################################################################################################################################################
# #2. Program to print month name based on number (1-12)

number = int(input("Enter a number (1-12): "))

if number == 1:
    print("January")
elif number == 2:
    print("February")
elif number == 3:
    print("March")
elif number == 4:
    print("April")
elif number == 5:
    print("May")
elif number == 6:
    print("June")
elif number == 7:
    print("July")
elif number == 8:
    print("August")
elif number == 9:
    print("September")
elif number == 10:
    print("October")
elif number == 11:
    print("November")
elif number == 12:
    print("December")
else:
    print("Invalid number! Please enter between 1 and 12.")
# ########################################################################################################################################################################

# #3.Write a program to swap two variables.
num_1=int(input("enter a number"))
num_2=int(input("enter another number"))
x=num_1
num_1=num_2
num_2=x
print("num1 "+str(num_1),"num2= "+str(num_2))

# # ##########################################################################################################################################################################
# #4.You are developing a simple ticket booking system for a movie theatre. The ticket
# # price depends on the age of the person and whether they have a membership card. If
# # the person is under 12, the ticket is free. If the person is between 12 and 60: if they
# # have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs 200. If the
# # person is above 60, they get a senior citizen discount, and then ticket costs Rs 100.
# # Write a python program using nested if-else to calculate and print the ticket price
# # based on the users age and membership status.
age=int(input("enter a age"))
if age<12:
    print("ticket is free")
elif age>=12 and age<=60:
    membership=input("have membership card?")
    if membership=="yes":
        price=150
    else:
        price=200
    print(price)
else:
    price=100
    print(price)
# ################################################################################################################################################################################
# #5. A utility company charges different rates based on electricity usage:
# # If usage < 100 units then cost Rs 5 per unit
# # If usage is between 100 to 300 units:
# # First 100 units: Rs 5
# #  Next units: Rs 8
# # If usage is > 300 units:
# #  First 100: Rs 5
# #  Next 200: Rs 8
# #  Remaining: Rs 10

unit=int(input("enter unit used"))
if unit < 100:
    usage=unit*5
elif unit<=300:
    first100=100*5
    next_unit=(unit-100)*8
    usage=first100 + next_unit
else:
    frist_100=100*5
    next_200=200*8
    nextunit=(unit-300)*10
    usage=nextunit+next_200+frist_100
print("the total amount of units is",usage)

################################################################################################################################################################################
#6.Write a complete Python program that:
#  Asks Player 1 to enter their move ( input: rock, paper, or scissors)
#  Asks Player 2 to enter their move ( input: rock, paper, or scissors)
#  Uses only nested if and else statements
#  Prints who wins or if it's a tie
user_1=input("user 1 : Enter rock, paper or scissor: ").lower()
user_2=input("user 2: Enter rock, paper or scissor: ").lower()
if user_1==user_2:
    print("draw")
else:
    if user_1=="rock":
        if user_2=="scissor":
            print("user1 wins")
        else:                                                                          

            print("user2 wins")
    else:
        if user_1=="paper":
            if user_2=="rock":
                print("user1 wins")
            else:
                print("user 2 wins")

        else:
            if user_1=="scissor":
                if user_2=="paper":
                    print("user_1 wins")
                else:
                    print("user_2 wins")
            else:
                print("invalid")
#############################################################################################
#7. A school decided to replace the desks in three classrooms. Each desk sits two
# students. Given the number of students in each class, print the smallest possible
# number of desks that can be purchased. The program should read three integers: the
# number of students in each of the three classes, a, b and c respectively.  

class_a=int(input("enter number of student in class a"))                                            
class_b=int(input("enter number of student in class b"))                                            
class_c=int(input("enter number of student in class c"))                                            

desk_a = (class_a+1)//2
desk_b = (class_b + 1)//2
desk_c= (class_c + 1) //2

total_desk = desk_a + desk_b + desk_c
print("total number of desk is : ",total_desk)
# #8

# ############################################################################################
# #9Write a Python program that takes a number as input, first checks if it is positive
# # if yes then check whether it is even or odd.

num=int(input("enter a number"))
if num>=0:
    if num%2==0:
        print('even')
    else:
        print("odd")

elif num<0:
    print("negative number")
else:
    print("zero")

# #############################################################################################
# #10Take two numbers and find the greater of the two. If they are equal, check if the
# # number is positive, negative, or zero.
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))

if num1==num2:
    print("equal")
    if num1>0:
        print("positive")
    elif num1<0:
        print("negative")
    else:
        print("zero")
elif num1>num2:
    print("num1 is greater")
else:
    print("num2 is grater")
# ############################################################################################
# # 11. Accept input from user If given number is a multiple of both 3 and 5 prints "Fizz
# # Buzz" instead of number If given number is a multiple of 3 but not 5 prints "Fizz"
# # instead of number If given number is a multiple of 5 but not 3 prints "Buzz"instead
# # of number If given number is not multiple of 3 or 5 prints value as usual.
num1=int(input("enter a number"))
if num1%3==0 and num1%5==0:
    print("Fizz Buzz")
elif num1%3==0 and num1%5!=0:
    print("Fizz")
elif num1%3!=0 and num1%5==0:
    print("Buzz")
else:
    print(num1)
# #############################################################################################
# #12

import random 

fact= random.randint(0,5)

if fact ==0:
    print("Flamingos turn pink from eating shrimp")

elif fact == 1:
    print("The only food that doesn't spoil is honey.")
elif fact == 2:
    print("Shrimp can only swim backwards.")
elif fact == 3:
    print("A taste bud's life span is about 10 days.")
elif fact == 4:
    print("It is impossible to sneeze while sleeping.")
else: 
    print("It is illegal to sing off-key in North Carolina.")
# #############################################################################################
# #13

amount = float(input("Enter the total purchase amount: "))
membership = input("Are you a member? (yes/no): ").lower()

if membership == "yes":
    ismember = True
elif membership == "no":
    ismember = False
else:
    print("for member only")
    ismember = False


if amount > 1000:
    if ismember:
        discount = amount * 0.20
        finalamount = amount - discount
        print(f"Member discount applied: 20%  {discount:.2f}")
    else:

        discount = amount * 0.10
        finalamount = amount - discount
        print(f"Non-member discount applied: 10% {discount:.2f}")
else:
    final_amount = amount
    print("No discount applicable (purchase amount ≤  1000)")

print(f"Final amount to pay:  {final_amount:.2f}")
#############################################################################################
# 14
earth_weight = float(input("What is your Earth weight? "))
planet = int(input("Enter planet number from 1-7: "))


if planet == 1:
    relative_gravity = 0.38
    planet_name = "Mercury"
elif planet == 2:
    relative_gravity = 0.91
    planet_name = "Venus"
elif planet == 3:
    relative_gravity = 0.38
    planet_name = "Mars"
elif planet == 4:
    relative_gravity = 2.53
    planet_name = "Jupiter"
elif planet == 5:
    relative_gravity = 1.07
    planet_name = "Saturn"
elif planet == 6:
    relative_gravity = 0.89
    planet_name = "Uranus"
elif planet == 7:
    relative_gravity = 1.14
    planet_name = "Neptune"
else:

    print("Invalid planet number")
    


destination_weight = earth_weight * relative_gravity

print(f"Your weight on {planet_name} would be {destination_weight}")
#############################################################################################