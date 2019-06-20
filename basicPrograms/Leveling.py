import os
import sys

def main():
    os.system('cls')
    print("Welcome to the level calculator")
    print("Developed by Jeffery Walto")
    stay = True
    while stay == True:
        print("Do you want character(1), skill(2), bulk(3), or quit(4)?")
        choise = input("> ")
        if choise in ["character", "1"]:
            character_level()
        elif choise in ["skill", "2"]:
            skill_level()
        elif choise in ["bulk", "3"]:
            bulk_level()
        elif choise in ["quit", "4"]:
            print("\nThank you for using the level calculator!")
            sys.exit()
        else:
            print("Choose again")

def character_level():
    do_again = True
    while do_again == True:
        level = int(input("\nWhat level is your character? "))
        needed_experience = ((level ** 2) * 100)
        exp = (f"{needed_experience:,d}")
        print("You need " + exp + " exp to level up your character.\n")
        again = input("again? ")
        if again in ['yes', 'y', 'again']:
            do_again = True
        else:
            do_again = False
    return True

def skill_level():
    do_again = True
    while do_again == True:
        level = int(input("\nWhat level is your skill? "))
        needed_experience = ((level ** 2) * 100)
        exp = (f"{needed_experience:,d}")
        print("\nYou need " + exp + " exp to level up your skill.\n")
        again = input("again? ")
        if again in ['yes', 'y', 'again']:
            do_again = True
        else:
            do_again = False  
    return True

def bulk_level():
    print("Welcome to bulk leveling!")
    do_again = True
    while do_again == True:
        level = int(input("\nWhat level is your character? "))
        n = int(input("How many levels?"))
        while (level <= n):
            needed_experience = ((level ** 2) * 100)
            exp = (f"{needed_experience:,d}")
            level += 1
            print("You need " + exp + " exp to reach lvl " + str(level))

        again = input("again? ")
        if again in ['yes', 'y', 'again']:
            do_again = True
        else:
            do_again = False
    return True

main()
