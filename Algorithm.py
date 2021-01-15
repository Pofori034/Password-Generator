import secrets


def generator(password_len):
    password_len = int(input("Enter Password Length: "))
    # defining  variables with all the available character
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit = "01234567890"
    symbol = "![]#$%^&*()?"
    available_characters = lower + upper + digit + symbol

    password_str = ""

    for i in range(int(password_len)):
        password = "".join(secrets.choice(available_characters))
        password_str += password

    return password_str
