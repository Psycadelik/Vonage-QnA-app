import os


def phone_number():
    file = open("/home/adrian/personal/QnA/vonage/phone_numbers.txt")
    number = file.read()
    file.close()
    return number


if __name__ == "__main__":
    phone_number()
