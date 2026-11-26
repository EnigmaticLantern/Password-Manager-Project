import math
import random
import string

# This project should be able to create, store, generate, and manage passwords. 
# All this while being purely python based, have it's own encryption system and have security of it's own when it comes to logging into the eventual application.

password = []

def generate_password(password):
    print("\n")
    print("---------- Amount ----------")
    amount = input(
        """How many passwords would you like to generate? \nIf you'd like to exit the program please enter "e"\n--------------
        \nAnswer: """
        )
    print("--------------------")
    l = amount
    print(amount)
    
    for l in amount:

        if amount != "e" or amount != "E" or amount != "exit" or amount != "Exit" or amount != "EXIT":
            if amount == 0 or amount == "0":
                print("Please input a valid amount of passwords you'd like to generate.")
                generate_password(password)
            if amount == "e" or amount == "E" or amount == "exit" or amount == "Exit" or amount == "EXIT":
                stop
            if amount != (amount != 0 or amount != "0" or amount == "e" or amount == "E" or amount == "exit" or amount == "Exit" or amount == "EXIT"):
                print("---------- Password", l, "----------")
                working()
                
        elif amount == 0 or amount != isinstance(amount, int):
            print("Goodbye")
            exit
        
        else:
            print("Error")

        l -= 1

def working():
    length = int(input("How long would you like your password? \n Answer: "))
    option = input("What is the purpose of this password? \n Answer: ")
    array = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", 
            ":", "'", "<", ">", ",", ".", "?", "/", "|", "`", "~", " ")
    sel = 0
    for i in range(0, length):
        sel = random.randint(1, 98)
        password.append(sel)
        length -= 1
        
    m = 0
    for i in range(0, length):
        print(password[m])
        m -= 1
        
working()
