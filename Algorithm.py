import pyperclip
import random
import string

'''
pyperclip: a python module that copies an output onto your computer's clipboard
random: a module that randomly generates items with a given length
String: a module that converts from any datatype to a string
password_generator function includes an algorithm that randomly generate password with a specified length
copy_password function copies the generated password on the computer's clipboard
'''
project_title = "Password Generator"
project_type = "Group Project 1"
print("==========", project_title, "==========")
print("----------\t", project_type, " ----------")
password_len = int(input("Enter Password Length: "))


def password_generator():
    generated_password = ''

    count1 = 0
    while count1 < password_len and count1 < 4:
        generated_password += random.choice(string.ascii_uppercase + string.ascii_lowercase +
                                            string.digits + string.punctuation)
        count1 += 1
    count2 = 0
    while count2 < password_len - 4:
        generated_password += random.choice(string.ascii_uppercase + string.ascii_lowercase +
                                            string.digits + string.punctuation)
        count2 += 1
    return generated_password


def copy_password():
    pyperclip.copy(password_generator())

