# https://www.youtube.com/channel/UC5akxkiQHpxCzPZWskdBbQQ Bryan Tong
import cmd
import textwrap
import sys
import random
import time
import os

screen_width = 100
maze = None
class player():
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.job = ''
        self.location = 'b2'
        self.game_over = False
myPlayer = player()

def title_secreen_selections():
    global maze
    option = input("> ")
    while option.lower() not in ['play', 'help', 'exit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            print("Which maze do you want to run? 1 or 2\n")
            maze_to_use = input("> ")
            if maze_to_use == '1':
                import maze01 as maze
                setup_game()
            elif maze_to_use == '2':
                import maze02 as maze
                setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("exit"):
            sys.exit()

def title_screen():
    os.system('cls')
    print('#######################')
    print('# Welcome to the game #')
    print('#######################')
    print('play')
    print('help')
    print('quit')
    title_secreen_selections()

def help_menu():
    print('#######################')
    print('# Welcome to the game #')
    print('#######################')
    print('use up, down, left, right to move')
    title_secreen_selections()

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location.upper() + '#')
    print('#' + maze.zonemap[myPlayer.location][maze.DESCRIPTION] + '#')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "============================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'walk', 'travel', 'quit', 'examine', 'inspect', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    global maze
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = maze.zonemap[myPlayer.location][maze.UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = maze.zonemap[myPlayer.location][maze.DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = maze.zonemap[myPlayer.location][maze.LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = maze.zonemap[myPlayer.location][maze.RIGHT]
        movement_handler(destination)

def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if maze.zonemap[myPlayer.location][maze.SOLVED]:
        print("You have already exausted this zone")
    else:
        print("You can trigger puzzle here")

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # here handle if puzzles have been solved

def setup_game():
    os.system('cls')

    question1 = "Hello what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "What role do you want to play?\n"
    question2added = "(You can play as a warrior, priest, or mage)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    while player_job not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")
    
    if myPlayer.job is 'warrior':
        self.hp = 0
        self.mp = 0
    elif myPlayer.job is 'priest':
        self.hp = 0
        self.mp = 0
    elif myPlayer.job is 'mage':
        self.hp = 0
        self.mp = 0

    question3 = "Welcome, " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "Welcome to this fantasy world\n"
    speech2 = "I hope it greets you well!\n"
    speech3 = "Just make sure you don't get to lost...\n"
    speech4 = "Heheheh...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    os.system('cls')
    print("######################")
    print("#   Lets start now   #")
    print("######################")
    main_game_loop()





title_screen()