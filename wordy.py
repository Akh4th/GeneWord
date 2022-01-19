import itertools
import argparse

p = argparse.ArgumentParser(description="Generates wordlist")
p.add_argument("--file_name", metavar="", nargs=1, type=str)
p.add_argument("--chars", metavar="", nargs=1, type=int, help="1=abc , 2=Abc , 3=4bc , 4=4Bc , 5=4B< , 6=123")
p.add_argument("--min", metavar="", nargs=1, type=int)
p.add_argument("--max", metavar="", nargs=1, type=int)
p.add_argument("--starts", metavar="", nargs=1, type=str)
args = p.parse_args()

# Settings Area
choices = ["1", "2", "3", "4", "5", "6"]
abc = "abcdefghijklmnopqrstuvwsyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWSYZ"
nums = "1234567890"
symbols = "!@#$%^&*+=`><?/.,;{}[]()"


# Variables from arg parser
try:
    file_name = args.file_name[0]
    chars = args.chars[0]
    min_length = args.min[0]
    max_length = args.max[0]
    try:
        if args.starts:
            starts = args.starts[0]
            start = True
    except NameError:
        start = False
        pass
    if min_length > max_length:
        print("Minimum can't be bigger than maximum")
        quit()
    if max_length <= 0 or min_length <= 0:
        print("Length can't be negative or 0.")
        quit()
    if str(chars) not in choices:
        print("Wrong chars input.")
        quit()
except Exception as e:
    print(f"Error code : {e}")
    quit()


def go(char, min, max, filed):
    if start:
        min = min - len(starts)
        max = max - len(starts)
        if max < 0 or min < 0:
            print("Length error.")
            quit()
        else:
            for x in (min, max):
                for y in itertools.product(char, repeat=x):
                    with open("generated//" + filed, "a+") as file:
                        file.write(starts + "".join(y) + "\n")
                        file.close()
            print(f"{filed} was successfully created !")
    else:
        for x in range(min, max):
            for y in itertools.product(char, repeat=x):
                print(f"\r{y}", end=" ")
                with open("generated//" + filed, "a+") as file:
                    file.write("".join(y) + "\n")
                    file.close()
        print(f"{filed} was successfully created !")


# Choosing an sequence according to input
if chars == 1:
    go(abc, min_length, max_length, file_name)
elif chars == 2:
    go(abc + ABC, min_length, max_length, file_name)
elif chars == 3:
    go(abc + nums, min_length, max_length, file_name)
elif chars == 4:
    go(abc + ABC + nums, min_length, max_length, file_name)
elif chars == 5:
    go(abc+ABC+nums+symbols, min_length, max_length, file_name)
else:
    go(nums, min_length, max_length, file_name)
