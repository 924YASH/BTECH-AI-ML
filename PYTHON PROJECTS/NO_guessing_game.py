# NO GUESSING GAME WITH COMPUTER VS USER 
import random
ans = "y"
rand = random.randint(0,10)
attempt = 0


print ("WELCOME TO THE RANDOM NO GUESSING GAME !")


while ans == "y" :
    user = int(input("enter your between 0 to 10 :"))
    attempt += 1

    if user == rand :
        print ("\ncongratuation u won")
        print ("total time u played :"  , attempt )
        ans = input("enter y to continue , y/n")

    elif user != rand :
        print ("OOPS you guess the wrong number , try again ")
        ans = input ("\nenter y to continue , y/n ")
        