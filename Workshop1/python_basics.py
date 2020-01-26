"""
MDST Workshop 1 - Python Basics Starter Code
"""

import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if (num % 2 == 0):
        print("even")
    else:
        print("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    user_input = ""
    while (user_input != "exit"):
        print('Guess a number within 1 to 9. Type "exit" to leave. ', end = '')
        user_input = input()
        rand_num = random.randint(0, 10)
        try:
            if (int(user_input) < rand_num):
                print("You guessed too low")
            elif (int(user_input) > rand_num):
                print("You guessed too high")
            else:
                print("You guessed exactly right")
        except:
            pass


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    for i in range(int(len(string)/2)):
        if (string[i] != string[-(i+1)]):
            print("Is not a palindrome")
            return
    print("Is a palindrome")

def strToB64(string):
    return base64.b64encode(string.encode('utf-8'))

def b64ToStr(base):
    return base64.b64decode(base).decode('utf-8')

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    with open(filename, 'w') as f:
        username = strToB64(username)
        password = strToB64(password)
        f.write(username.decode('utf-8') + "\n")
        f.write(password.decode('utf-8'))

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    with open(filename, 'r') as f:
        username = f.readline()
        username = b64ToStr(username)
        print(username)
        print(b64ToStr(f.readline()))
    
    if (password != None):
        part4a(filename, username, password)


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")