# Jai's code
from time import sleep

def countdown(count):
    while count > 0:
        print(f"{count} SECOND(S)!")
        count -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(count):
    while count > 0:
        print(f"{count} SECOND(S)!")
        count -= 1
        sleep(1)
    print("HAPPY NEW YEAR!")
