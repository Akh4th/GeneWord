from termcolor import colored
import itertools


# Settings Area
choices = ["1", "2", "3", "4", "5", "6", "*"]
choices1 = choices[:]
choices1.remove("*")
good = colored("[","red") + "+" + colored("]", "red")
err = colored("[","red") + "!" + colored("]", "red")
spec = colored("[","red") + "*" + colored("]", "red")
abc = "abcdefghijklmnopqrstuvwsyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWSYZ"
nums = "1234567890"
symbols = "!@#$%^&*+=`><?/.,;{}[]()"


# First prints and inputs
print(good + " Hello user !")
file_name = input(good + " Please enter file name : ")
cls = input(good + " Clear " + file_name + " file ?\n" + colored("[Yes/No] : ", "red"))
while cls.lower() != "yes" and cls.lower() != "no":
    cls = input(err + " Wrong input, please try again : ")
if cls.lower() == "yes":
    open(file_name, "w").close()
    print(colored(file_name + " CLEARED !\n", "green"))
print(good + " What type of characters ?\n" + colored("[", "red") + "1" + colored("]", "red") + " Weak password " + colored('(abc)', "green"))
print(colored("[", "red") + "2" + colored("]", "red") + " Medium password " + colored("(Abc)", "green"))
print(colored("[", "red") + "3" + colored("]", "red") + " Medium [2] " + colored("(4bc)", "green"))
print(colored("[", "red") + "4" + colored("]", "red") + " Strong password " + colored("(4Bc)", "green"))
print(colored("[", "red") + "5" + colored("]", "red") + " Extreme password " + colored("(4B<)", "green"))
print(colored("[", "red") + "6" + colored("]", "red") + " PIN Numbers " + colored("123", "green"))
chars = input(spec + colored(" Modify your own password list", "green") + "\n")

# Validating input
while chars not in choices:
    chars = input(err + " Wrong input, try again : ")
# Getting length in case of legit input
if chars in choices:
    min_length = int(input(good + " Minimum length of the password :\n"))
    max_length = int(input(good + " Maximum length of the password :\n"))
    # Validating password length
    while max_length < min_length:
        min_length = int(input(err + " Wrong input, try again. [Minimum] : "))
        max_length = int(input(err + " Wrong input, try again. [Maximum] : "))

# Choosing an sequence according to input
if chars == "1":
    for x in range(min_length, max_length + 1):
        for y in itertools.product(abc, repeat=x):
            with open(file_name, "a+") as file:
                file.write("".join(y) + "\n")
                file.close()
    print(good + colored(" " + file_name + " Was successfully created !", "green"))
elif chars == "2":
    for x in range(min_length, max_length + 1):
        for y in itertools.product(abc+ABC, repeat=x):
            with open(file_name, "a+") as file:
                file.write("".join(y) + "\n")
                file.close()
    print(good + colored(" " + file_name + " Was successfully created !", "green"))
elif chars == "3":
    for x in range(min_length, max_length + 1):
        for y in itertools.product(abc+nums, repeat=x):
            with open(file_name, "a+") as file:
                file.write("".join(y) + "\n")
                file.close()
    print(good + colored(" " + file_name + " Was successfully created !", "green"))
elif chars == "4":
    for x in range(min_length, max_length + 1):
        for y in itertools.product(abc+ABC+nums, repeat=x):
            with open(file_name, "a+") as file:
                file.write("".join(y) + "\n")
                file.close()
    print(good + colored(" " + file_name + " Was successfully created !", "green"))
elif chars == "5":
    for x in range(min_length, max_length + 1):
        for y in itertools.product(abc+ABC+nums+symbols, repeat=x):
            with open(file_name, "a+") as file:
                file.write("".join(y) + "\n")
                file.close()
    print(good + colored(" " + file_name + " Was successfully created !", "green"))
elif chars == "6":
    for x in range(min_length, max_length + 1):
        for y in itertools.product(nums, repeat=x):
            with open(file_name, "a+") as file:
                file.write("".join(y) + "\n")
                file.close()
    print(good + colored(" " + file_name + " Was successfully created !", "green"))
# Modified password !
else:
    print(good + " Do you want to start with specific chars ?\n" + colored("Example : ", "green") + colored("050*******", "red"))
    has_start = input(colored('[Yes/No] : ', 'red'))
    while has_start.lower() != "yes" and has_start.lower() != "no":
        has_start = input(colored(err + 'Please try again, [Yes/No] : ', 'red'))
    if has_start.lower() == 'no':
        print(good + " Do you want to customize your own sequences ?")
        cus = input(colored('[Yes/No] : '))
        while cus.lower() != "yes" and cus.lower() != "no":
            cus = input(err + " Please try again, " + colored('[Yes/No] : ', "red"))
        if cus.lower() == "yes":
            cust = input(good + " Please enter the characters / numbers / symbols you want in your sequence : ")
            for x in range(min_length, max_length + 1):
                for y in itertools.product(cust, repeat=x):
                    with open(file_name, "a+") as file:
                        file.write("".join(y) + "\n")
                        file.close()
            print(good + colored(" " + file_name + " Was successfully created !", "green"))
        else:
            print(err + " So you don't want to use our sequences  AND you don't want to customize your own")
            print(colored("THEN WHAT THE FUCK ARE YOU DOING IN HERE ?!", "red"))
    if has_start.lower() == "yes":
        cust = input(good + " characters you want to start with : ")
        extra = input(good + " ends with " + colored("[abc (1) / 4bc (2) / Abc (3) / 4Bc (4) / 4Bc< (5) / 123 (6)]", "red"))
        while extra not in choices1:
            extra = input(err + " Wrong input, please try again : ")
        if extra == "1":
            extra = abc
        if extra == "2":
            extra = abc+nums
        if extra == "3":
            extra = abc+ABC
        if extra == "4":
            abc+nums+ABC
        if extra == "5":
            abc+nums+ABC+symbols
        else:
            extra = nums
        for x in range(min_length - len(cust), (max_length + 1) - len(cust)):
            for y in itertools.product(extra, repeat=x):
                with open(file_name, "a+") as file:
                    file.write(cust+"".join(y) + "\n")
                    file.close()
        print(good + colored(" " + file_name + " Was successfully created !", "green"))