#Family Name: Sy Rajeswaran
#Student number: 300005333
#Course: ITI 1120 [C]
#Assignment 2 part1

import math
import random



def performTest(flag:int,n:int)-> int:
    """ takes in the input of flag either 0 for subtraction or 1 for exponentiation
    and the n value is the number of questions the user wants to practise outputs the
    number of questions gotten right"""
    point= 0
    if flag == 0:
        for i in range(n):
            a= random.randint(0,10)
            b= random.randint(0,10)
            answer = a - b
            x =int (input("What is the result of " + str(a)+ " - " + str(b) + "? "))
            if x == answer:
                point = point+1
    elif flag == 1:
        for i in range (n):
            a= random.randint(0,9)
            b= random.randint(0,9)
            answer = a**b
            x = int(input("What is the result of " + str(a)+ "^" + str(b) + "? "))
            if x == answer:
                point = point +1       
    return (point)


name= str(input( "Hi there! What's your name ? "))
if __name__ == "__main__":

    
    flag=int(input("What woud you like to practise? Enter 0 for subtraction, 1 is exponentiation: "))
    n= int( input ( "How many practise question would you like? "))
    x=(performTest(flag, n)/n)* 100 
    if x >= 90 :
        print ( "Congratulations " + str.strip(name) + "!! You'll probabaly get an A tommorow. Now go eat your dinner and go to sleep. Good bye " + str.strip(name)  + "!")
    elif 90 > x >=70:
        print( "You did well " + str.strip(name)  +", but I know you can do better. Good bye "+str.strip(name) +"!")
    else:
        print("I think you need some more practice "+ str.strip(name) + ". Good bye " + str.strip(name) + "!")

