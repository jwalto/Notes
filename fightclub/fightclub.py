import sys
import os

def main():
    stay = True
    play_options = {'fight': user_fight, 'Fight': user_fight,
                    'shop': user_shop, 'Shop': user_shop,
                    'give up': end_game, 'quit': end_game}
    print("You wake up in a prison cell outside of an arena.")
    print("A man approaches and asks if you want to fight, shop, or give up")
    while stay == True:
        user_choise = input("What do you wish to do? ").lower()
        if user_choise in play_options:
            stay = play_options[user_choise]()
        else:
            print("Please enter a valid command.\n")

def user_fight():
    print("So you wish to fight")
    input("Return? ")
    return True
def user_shop():
    print("So you wish to shop")
    input("Return? ")
    return True
def end_game():
    print("You give up to easily")
    return False





main()
