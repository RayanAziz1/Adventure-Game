from operator import itemgetter
import time
import random
import sys


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def start(monster):
    print_pause("you find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + monster + " is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your"
                "trusty (but not very effective) dagger.\n")


def valid_input(item, monster):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    player_choice = input("(Please enter 1 or 2.)\n")
    if player_choice == "1":
        house(item, monster)
    elif player_choice == "2":
        cave(item, monster)


def house(item, monster):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a " + monster + ".")
    print_pause("Eep! This is the " + monster + "'s house!")
    print_pause("The " + monster + " attacks you!")
    if item == "dagger":
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny" + item + ".")
        fight(item, monster)


def fight(item, monster):
    player_choice = input("Would you like to (1) fight or (2) run away?\n")
    if player_choice == "1":
        if item == "dagger":
            print_pause("\nYou do your best...")
            print_pause("but your dagger is no match "
                        "for the " + monster + ".")
            print_pause("You have been defeated!\n")
            again()
    elif player_choice == "2":
        print_pause("You run back into the field."
                    "Luckily, you don't seem to have been followed.\n")
    valid_input(item, monster)


def cave(itme, monster):

    if itme == "dagger":
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and"
                    " take the sword with you.")
        print_pause("You walk back out to the field.")
        itme = "magical Sword of Ogoroth"
    else:
        print_pause("You peer cautiously into the cave.\n")
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cavenow.\n")
        print_pause("You walk back to the field.\n")
        itme = "magical Sword of Ogoroth"

    win(monster)


def win(monster):
    player_choice = input("Would you like to (1) fight or (2) run away?\n")
    if player_choice == "1":
        print_pause("As the " + monster + " moves to attack, "
                    "you unsheath your new sword.\n")
        print_pause("The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the "
                    "attack.\n")
        print_pause("But the " + monster + "takes one look at "
                    "your shiny new toy and runs away!\n")
        print_pause("You have rid the town of the " + monster +
                    ". You are victorious!\n")
        again()
    elif player_choice == "2":
        print_pause("You run back into the field."
                    "Luckily, you don't seem to have been followed.\n")
        valid_input(itemgetter, monster)


def again():
    print_pause("Would you like to play again?\n")
    repeat = input("(Please enter y or n.)\n")
    if repeat == "y":
        print_pause("Excellent! Restarting the game ...\n")
        play()
    elif repeat == "n":
        print_pause("Thanks for playing! See you next time.\n")
        sys.exit()
    else:
        (again)


def play():
    monster = random.choice(["pirate", "wicked fairie",
                            "gorgon", "dragon", "troll"])
    item = "dagger"
    start(monster)
    valid_input(item, monster)
    fight(item, monster)


play()