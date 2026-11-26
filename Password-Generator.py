import math
import random
import string

# This project should be able to create, store, generate, and manage passwords. 
# All this while being purely python based, have it's own encryption system and have security of it's own when it comes to logging into the eventual application.
password = ()

def generate_password(password):
    # Generates a password based on the details provided by the user
    l = input("How many passwords would you like to generate? \n Answer: ")
    for l in range(int(l)):
        length = input("How long would you like your password? \n Answer: ")
        option = input("What is the purpose of this password? \n Answer: ")
        array = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                 "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                 "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", 
                 ":", "'", "<", ">", ",", ".", "?", "/", "|", "`", "~", " ")
        password_r = ""
        for i in range(int(length)):
            sel = random.randint(1, 98)
            l -= 1
            print(array[sel], end="")
        
    print(password)

generate_password(password)
