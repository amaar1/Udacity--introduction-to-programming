import time
import random


# Function to print and pause. Pause lasts for 2 seconds
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# Intro to story and description to player of what is happening
def intro(inventory, monster):
    print_pause("\nYou are a cloaked traveler who seeks out adventure. \n")
    print_pause("\nYou heard of a kingdom that is plagued by a beast of"
                "unknown nature which lives near the mount bealmir. \n")
    print_pause("\nHowever you do not know the exact location "
                "of the monster.\n")
    print_pause("\nSeeking out the monster, you come to a "
                "mountain pass on mount bealmir.\n")
    print_pause("\nIn front of you is a small town "
                "that seems unusually quiet.\n")
    print_pause("\nBehind you is a dark cave.\n")
    print_pause("\nFrom the otherside of the mountain you "
                "see a mysterious light.\n")


# Different scenario based on if the player has come here for
# the first time or has chosen to return
def light(inventory, monster):
    if "fairy light" in inventory:
        print_pause("\n You travel to the site otherside of the mountain. \n")
        print_pause("\nYou have already been here, and taken the light"
                    " There is nothing left here. \n")
        print_pause("\nYou travel back to the mountain pass.\n")
    else:
        print_pause("\nYou slowly approach the mysterious light at the "
                    "at the other side of the mountain. \n")
        print_pause("\nThere seems to be no one around. \n")
        print_pause("\nFrom where the light is emanating you see "
                    "a small bottle. \n")
        print_pause("\nIt's a Fairy light that can light up even the darkest "
                    "of places. \n")
        print_pause("\nYou take the fairy light, it may be useful "
                    "in the future. \n")
        print_pause("\nYou travel back to the mountain pass.\n")
        inventory.append("fairy light")
    mountain_pass(inventory, monster)


# Different scenario based on players previous choices
def cave(inventory, monster):
    if "Bow" in inventory:
        print_pause("\nYou enter the dark cave \n.")
        print_pause("\nYou have already been here, and taken the Bow."
                    " There is nothing left here. \n")
        print_pause("\nYou travel back to the mountain pass.\n")
    else:
        print_pause("\nYou silently enter the dark cave. \n")
        if "fairy light" in inventory:
            print_pause("\nIt's too dark to see so you turn the "
                        "fairy light on. \n")
            print_pause("\nLying before you is a chest. \n")
            print_pause("\nInside you find a bow. \n ")
            print_pause("\nAs you lift the bow you hear a whisper, "
                        "use it wisely it said. \n")
            print_pause("\nYou take the bow and hurry out of the cave fearing "
                        "ghosts may be lurking.\n")
            inventory.append("Bow")
        else:
            print_pause("\nYou enter the dark cave. \n")
            print_pause("\nYou can not see anything. \n")
            print_pause("\nBring a light with you next time. \n")
    mountain_pass(inventory, monster)


# Different scenario based on players previous and future choices
def town(inventory, monster):
    print_pause("\nYou enter the town.\n")
    print_pause("\nNo one can be seen and not even a rustle can be heard.\n")
    print_pause("\nA chill crawls up your spine, something is wrong.\n")
    print_pause("\nSuddenly from behind a " + monster + " lets out "
                "a fearsome roar. \n")
    print_pause("\nYou stumbled into the " + monster + "'s lair. \n")
    print_pause("\nThe " + monster + " charges towards you!\n")
    if "Bow" not in inventory:
        print_pause("\nWith no weapons to fight with you know it will "
                    "be difficult to battle the " + monster + ".\n")
    while True:
        choice = input("\nWould you like to (1) fight or (2) flee?\n")
        if choice == "1":
            if "Bow" in inventory:
                print_pause("\nYou have no arrows but you instinctively lift "
                            "your bow\n")
                print_pause("\nSuddenly an arrow of air forms!\n")
                print_pause("\nYou release the arrow. \n")
                print_pause("\nAs the arrow hits the " + monster + " the "
                            "beast crumbles to it's knees and collapses.\n")
                print_pause("\nThe beast has been defeated!!! \n")
                print_pause("\nYou look around, there is no celebration, "
                            "no glory to be earned... you were too late "
                            "the villagers are dead.\n")
            else:
                print_pause("\nYou prepare yourself to fight but "
                            "you are significantly outmatched.\n")
                print_pause("\nYou have been fallen to the enemy!\n")
            play_again()
            break
        if choice == "2":
            print_pause("\nYou flee the village and run back to the "
                        "mountain pass.\n"
                        "\nLuckily, you evaded death this time.\n")
            mountain_pass(inventory, monster)
            break


# Choices given to player on which routes the can take to 2 possible endings
def mountain_pass(inventory, monster):
    print_pause("Enter 1 to enter the mysterious town.")
    print_pause("Enter 2 to explore the dark cave.")
    print_pause("Enter 3 to investigate the mysterious light source.")
    while True:
        decision = input("What would you like to do?"
                         "(Please enter 1, 2 or 3.)\n")
        if decision == "1":
            town(inventory, monster)
            break
        elif decision == "2":
            cave(inventory, monster)
            break
        elif decision == "3":
            light(inventory, monster)
            break


# Option to restart the game or quit once ending reached
def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nRestarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing!\n\n\n")
    else:
        play_again()


# Functions and variables required for the game to be run
def play_game():
    inventory = []
    monsters = ["cyclops", "troll", "chimera", "dragon"]
    monster = random.choice(monsters)
    intro(inventory, monster)
    mountain_pass(inventory, monster)


# calling the game
play_game()
