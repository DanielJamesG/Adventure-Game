import time
import random
import sys

monsters = ("A slithery snake!","A spooky ghost!","Donald Trump!","Bees?","That goldfish you forgot to feed!","A gigantic angry marshmellow!")
boss = random.choice(monsters)

def print_pause(print_message):
    print(print_message)
    time.sleep(2)


def player_intro():
    print_pause("You reach the door.")
    print_pause("Rumor is this mansion's haunted.")
    print_pause("It's been abandoned for centuries.")
    print_pause("Now your friends have dared you to go inside.")


def front_door():
    print_pause("What do you want to do?")
    option = input (">Enter 1 to push open the door.\n"
                    ">Enter 2 to peak through the window.\n")
    if option == '1':
        print_pause("You push open the door.")
        print_pause("Moonlight lights up the hall.")
        print_pause("You take a step.")
        print_pause("SLAM!")
        print_pause("The hall disappears.")
    elif option == '2':
        print_pause("You peak through the window.")
        print_pause("BOO!")
        print_pause("Oh no! It's a spooky ghost.")
        print_pause("You've been spooked to death.")
        you_lose()
    else:
        print_pause("Sorry I didn't get that, please enter 1 or 2.")
        front_door()


def grand_hallway():
    print_pause("To your left you see a light switch.")
    print_pause("What do you want to do?")
    option = input (">Enter 1 to flick the switch.\n"
                    ">Enter 2 to find another way.\n")
    if option == '1':
        print_pause("You flick the swtich.")
        print_pause("SPLAT!")
        print_pause("Oh no! Sticky slime falls from the roof.")
        print_pause("You've been sticky slimed to death.")
        you_lose()
    elif option == '2':
        print_pause("You take out your phone.")
        print_pause("This will have to do.")
        print_pause("You continue walking.")
        print_pause("At the end of the hall is two doors.")
        print_pause("The left is labelled 'Dungeon'.")
        print_pause("The right has no label.")
    else:
        print_pause("Sorry I didn't get that, please enter 1 or 2.")
        grand_hallway()


def choose_door(items):
    print_pause("What do you want to do?")
    option = input (">Enter 1 to go through the left door.\n"
                    ">Enter 2 to go through the right door.\n")
    if option == '1':
        print_pause("You head down to the dungeon.")
        if "dagger" in items:
            print_pause("It seems there isn't much else to do here.")
            print_pause("You head back upstairs.")
            choose_door(items)
        else:
            print_pause("A trail of blood stains the floor.")
            print_pause("You follow it.")
            print_pause("It leads you to a golden dagger.")
            print_pause("This could come in handy later.")
            print_pause("It seems there isn't much else to do here.")
            print_pause("You head back upstairs.")
            items.append("dagger")
            choose_door(items)
    elif option == '2':
        print_pause("You go through the mysterious unlabelled door.")
        print_pause("The room is filled with bones.")
        print_pause("All of a sudden...")
        print_pause("SCEEEEECH!")
        print_pause("Oh no! it's...")
        print_pause(boss)
        if "dagger" in items:
            print_pause("It comes right for you.")
            print_pause("But you're weilding your golden dagger!")
            print_pause("You plunge it forward.")
            print_pause("The monster was no match.")
            you_win()
        else:
            print_pause("You don't stand a chance.")
            print_pause("You've been spooked to death'.")
            you_lose()
    else:
        print_pause("Sorry I didn't get that, please enter 1 or 2.")
        choose_door(items)


def you_win():
    print("You're safe...")
    time.sleep(3)
    print("For now.")
    time.sleep(3)
    option = input (">Enter 1 to play again.\n"
                    ">Enter 2 to quit the game.\n")
    if option == '1':
        print("Loading new game...")
        time.sleep(5)
        play_game()
    elif option == '2':
        print_pause("Thanks for playing.")
        sys.exit()
    else:
        print_pause("Sorry I didn't get that, please enter 1 or 2.")
        you_win()


def you_lose():
    print_pause("GAME OVER.")
    print_pause("Would you like to try again?")
    option = input (">Enter 1 to try again.\n"
                    ">Enter 2 to quit the game.\n")
    if option == '1':
        print("Loading new game...")
        time.sleep(5)
        play_game()
    elif option == '2':
        print_pause("Thanks for playing.")
        sys.exit()
    else:
        print_pause("Sorry I didn't get that, please enter 1 or 2.")
        you_lose()


def play_game():
    items = []
    player_intro()
    front_door()
    grand_hallway()
    choose_door(items)


play_game()
