# --------------------------------------------------------------------------- #
# Ghost Game 3: Revenge of the Spirit #
# Version 1.0 #
import math
import os
import sys
import time
from random import choice
from random import randint
# --------------------------------------------------------------------------- #
# Game Setup #
class Game:
    run = True
    room = 1
    floor = 1
    appirition = ""
    hp = 0
# --------------------------------------------------------------------------- #
# Player Setup #
class Player:
    name = ""
    title = ""
    lvl = 1
    exp = 0
    exp_req = 10
    max_hp = 20
    hp = 20
    str = 10
    dex = 12
    hor = 10
    inv = ["Haunted Candy"]
# --------------------------------------------------------------------------- #
# Boss Setup #
class Boss:
    lvl = 10
    max_hp = 100
    hp = 100
    str = 20
    dex = 25
    hor = 30
# --------------------------------------------------------------------------- #
def boss():
    name = Game.floor
    names = {
        1: "The Ghost Amalgamation",
        2: "The Fragmented Ghoul",
        3: "The Spirit Snatcher",
        4: "The Eon Spectre",
        5: "The Phantom Blood",
        6: "The Fear Reaper",
        7: "The Shade Wraith",
        8: "Eidolon The Worm",
        9: "Phantasm The Impending",
        10: "Polterghast The Unchained",
        11: "Your Soul"
        }
    Game.appirition = names[name]
    return Game.appirition
# --------------------------------------------------------------------------- #
# Ghost Setup #
class Ghost:
    lvl = 1
    max_hp = 10
    hp = 10
    str = 5
    dex = 8
    hor = 7
# --------------------------------------------------------------------------- #
def ghost():
    name = randint(1,7)
    names = {
        1: "Ghost",
        2: "Ghoul",
        3: "Spirit",
        4: "Spectre",
        5: "Phantom",
        6: "Reaper",
        7: "Wraith"
        }
    Game.appirition = names[name]
    return Game.appirition
# --------------------------------------------------------------------------- #
# Displays The Title Screen #
def title():
    print("""
    ____________________________________________

                    Welcome to
        Ghost Game  3: Revenge Of The Spirit

    --------------------------------------------
        > Play
        > Help
        > Quit
    ____________________________________________
    """)
    menu()
# --------------------------------------------------------------------------- #
def menu():
    while Game.run == True:
        option = input("> ").lower()
        if option == "play":
            os.system("cls")
            start()
        elif option == "help":
            os.system("cls")
            helps()
        elif option == "quit":
            os.system("cls")
            quit()
        else:
            print("\n\tPlease enter a valid command")
# --------------------------------------------------------------------------- #
# Starting The Game #
def start():
    while Player.hp > 0:
        if Game.room % 10 == 0:
            print("\n\tYou feel an ominous presence coming from the next room...")
            time.sleep(1)
            door_b()
            enter = input("...")
            battle()
        else:
            door_n()
            option = input("> ").lower()
            os.system("cls")
            if option == "1":
                chance()
            elif option == "2":
                chance()
            elif option == "3":
                chance()
            elif option == "options":
                options()
            else:
                print("\n\tPlease enter a valid command")
    else:
        lose()
# --------------------------------------------------------------------------- #
# Chance Of Battle Or Item Or Advancing #
def chance():
    update()
    chance = randint(1,3)
    if chance == 1:
        battle()
    elif chance == 2:
        item()
    elif chance == 3:
        advance()
# --------------------------------------------------------------------------- #
# Battle Start #
def battle():
    if Game.room % 10 == 0:
        Game.hp = Boss.hp
        print(f"\n\t...")
        time.sleep(1)
        print(f"\n\t...")
        time.sleep(1)
        print(f"\n\t...")
        time.sleep(1)
        print(f"\n\tThe air grows cold as {boss()} approaches...")
        time.sleep(1)
        print(f"\n\t...")
        time.sleep(1)
        print(f"\n\t...")
        time.sleep(1)
        print(f"\n\t...")
        time.sleep(1)
    else:
        Game.hp = Ghost.hp
        print(f"\n\tYou have encountered a {ghost()}")
    phase()
# --------------------------------------------------------------------------- #
# The Battle Phase #
def phase():
    while Player.hp > 0:
        fight()
        decision = input("> ")
        os.system("cls")
        if decision == "1":
            exorcise()
        elif decision == "2":
            horrify()
        elif decision == "3":
            escape()
        elif decision == "4":
            inventory()
        else:
            print("\n\tEnter a valid option.")
            phase()
    lose()
# --------------------------------------------------------------------------- #
# Exorcise #
def exorcise():
    if Game.room % 10 == 0:
        if randint(Player.dex // 2, Player.dex * 2) < Boss.dex:
            print(f"\n\tYou took significant damage")
            Player.hp = Player.hp - Boss.str
            phase()
        else:
            print(f"\n\tYou managed to land an attack on {Game.appirition}")
            Game.hp = Game.hp - Player.str
            if Game.hp <= 0:
                Game.room = Game.room + 1
                Game.floor = Game.floor + 1
                win_b()
            else:
                phase()
    else:
        if randint(Player.dex // 2, Player.dex * 2) < Ghost.dex:
            print(f"\n\tYou took damage")
            Player.hp = Player.hp - Ghost.str // 2
            phase()
        else:
            print(f"\n\tYou dealt damge")
            Game.hp = Game.hp - Player.str // 2
            if Game.hp <= 0:
                Game.room = Game.room + 1
                win()
            else:
                phase()
# --------------------------------------------------------------------------- #
# Horrify #
def horrify():
    if Game.room % 10 == 0:
        if randint(Player.hor, Player.hor * 2) < Boss.hor:
            print(f"\n\t{Game.appirition} thinks nothing of your Horror")
            time.sleep(1)
            print(f"\n\t{Game.appirition}'s gaze pierces your mind")
            time.sleep(1)
            Player.hp = Player.hp - Boss.str
            phase()
        else:
            print(f"\n\t{Game.appirition} acknowledges your Horror")
            time.sleep(1)
            print(f"\n\tBut this means nothing")
            time.sleep(1)
            phase()
    else:
        if randint(Player.hor // 2, Player.hor * 2) < Ghost.hor:
            print(f"\n\tYour Horror failed to overwhelm the Ghost")
            Player.hp = Player.hp - Ghost.str // 2
            phase()
        else:
            print("\n\tYou managed to scare the Ghost away")
            Game.room = Game.room + 1
            update()
            start()
# --------------------------------------------------------------------------- #
# Escape #
def escape():
    if Game.room % 10 == 0:
        if randint(Player.dex // 2, Player.dex * 2) < Boss.dex:
            print("\n\tRunning away is futile")
            time.sleep(1)
            phase()
        else:
            print("\n\tThere is no escape")
            time.sleep(1)
            phase()
    else:
        if Player.dex < Ghost.dex // 2:
            Player.hp = Player.hp - Ghost.str // 2
            print("\n\tYou failed to Escape")
            phase()
        else:
            print("\n\tYou managed to Escape")
            update()
            start()
# --------------------------------------------------------------------------- #
# Items #
def item():
    Game.room = Game.room + 1
    item = choice(["Souls", "Ectoplasm", "Haunted Candy"])
    Player.inv.append(item)
    print(f"\n\tYou found {item}!")
    start()
# --------------------------------------------------------------------------- #
# Advancing #
def advance():
    Game.room = Game.room + 1
    print("\n\tYou safely made it to the next room.")
    start()
# --------------------------------------------------------------------------- #
# The Options Menu #
def options():
    while True:
        print(f"""
    ____________________________________________

                    - Options -

    --------------------------------------------
        > 1: Stats
        > 2: Inventory
        > 3: Back to Game
        > 4: Quit to Title
    ____________________________________________
    """)
        option = input("> ")
        if option == "1":
            os.system("cls")
            stats()
        elif option == "2":
            os.system("cls")
            inventory()
        elif option == "3":
            os.system("cls")
            start()
        elif option == "4":
            os.system("cls")
            title()
        else:
            os.system("cls")
            print("\n\tEnter a valid option.")
# --------------------------------------------------------------------------- #
def inventory():
    while True:
        if Player.inv == []:
            print("\n\tThere is nothing in your inventory")
            break
        else:
            print(f"\n\tInventory: {Player.inv}")
            print(f"""
    ____________________________________________

                    - Inventory -

    --------------------------------------------
            What do you want to use?

        > 1: Souls
        > 2: Ectoplasm
        > 3: Huanted Candy
        > 4: Don't use an item
    ____________________________________________
""")
            try:
                use = input("> ")
                if use == "1":
                    if Player.hp == Player.max_hp:
                        print("\n\tYour Willpower is at its limit")
                    else:
                        Player.inv.remove("Souls")
                        Player.hp = Player.max_hp
                        os.system("cls")
                        print("\n\tYou consumed the a Souls and recovered Willpower!")
                elif use == "2":
                    Player.inv.remove("Ectoplasm")
                    Player.str = Player.str + Game.room // 2
                    Player.dex = Player.dex + Game.room // 2
                    Player.hor = Player.hor + Game.room // 2
                    os.system("cls")
                    print("\n\tYou consumed the Ectoplasm.")
                    print("\n\tYour abilities increased surpassed their limits!")
                elif use == "3":
                    os.system("cls")
                    Player.inv.remove("Haunted Candy")
                    print("\n\tYou consumed the Haunted Candy!")
                    Player.exp = Player.exp_req
                    up()
                elif use == "4":
                    os.system("cls")
                    print("\n\tYou didn't use an item.")
                    break
                else:
                    os.system("cls")
                    print("\n\tEnter a valid option.")
            except ValueError:
                print("\n\tThat item isnt in your inventory.")
# --------------------------------------------------------------------------- #
def up():
    Player.lvl = Player.lvl + 1
    Player.exp_req = Player.exp_req * 2
    Player.max_hp = Player.max_hp + randint(Player.lvl, Player.lvl * 5)
    Player.hp = Player.max_hp
    Player.str = Player.str + randint(Player.lvl // 2, Player.lvl * 2)
    Player.dex = Player.dex + randint(Player.lvl // 2, Player.lvl * 2)
    Player.hor = Player.hor + randint(Player.lvl // 2, Player.lvl * 2)
    print(f"\n\tYou leveled up to level {Player.lvl}")
    stats()
# --------------------------------------------------------------------------- #
# Winning Normally #
def win():
    exp = randint(Game.room, Game.room * 2)
    Player.exp = Player.exp + exp
    print(f"\n\tYou defeated the {Game.appirition} and gained {exp} experience.")
    if Player.exp >= Player.exp_req:
        up()
        start()
    else:
        print(f"\n\tExp: [{Player.exp} / {Player.exp_req}]")
        next = input()
    start()
# --------------------------------------------------------------------------- #
# Winning Boss #
def win_b():
    exp = randint(Game.floor * 10, Game.floor * 50)
    Player.exp = Player.exp + exp
    print(f"\n\tYou defeated {Game.appirition} and gained {exp} experience.")
    if Player.exp >= Player.exp_req:
        up()
        start()
    else:
        print(f"\n\tExp: [{Player.exp} / {Player.exp_req}]")
        next = input()
    print(f"\n\t...")
    time.sleep(1)
    print(f"\n\t...")
    time.sleep(1)
    print(f"\n\t...")
    time.sleep(1)
    print(f"\n\tThe appirition disspates and souls pour out into the sky...")
    time.sleep(1)
    start()
# --------------------------------------------------------------------------- #
# losing #
def lose():
    print(f"\n\tF...")
    time.sleep(1)
    print(f"\n\tF...")
    time.sleep(1)
    print(f"\n\tF...")
    time.sleep(1)
    os.system("cls")
    sys.exit()
# --------------------------------------------------------------------------- #
# Display Screens #
# --------------------------------------------------------------------------- #
# Boss Door #
def door_b():
    print(f"""
    ____________________________________________

            - Final Room of this Floor -

    --------------------------------------------
            You have no choice but to enter...

        > Enter

    ____________________________________________
""")
# --------------------------------------------------------------------------- #
# Normal Door #
def door_n():
    print(f"""
    ____________________________________________

        - Floor {Game.floor}: Room {Game.room} -

    --------------------------------------------
            Choose a Door

        > 1
        > 2
        > 3
                                    > Options
    ____________________________________________
""")
# --------------------------------------------------------------------------- #
# Displays The Players Stats #
def stats():
    print(f"""
    ____________________________________________

                - Stats -

    --------------------------------------------
        Level: -{Player.lvl}-
        EXP: [{Player.exp} / {Player.exp_req}]

        Willpower: [{Player.hp} / {Player.max_hp}]
        Strength: {Player.str}
        Dexterity: {Player.dex}
        Dread: {Player.hor}
    ____________________________________________
    """)
    next = input()
    os.system("cls")
# --------------------------------------------------------------------------- #
# Displays Fight Screen #
def fight():
    if Game.room % 10 == 0:
        print(f"""
    ____________________________________________

            - You're facing {Game.appirition} -
    --------------------------------------------

        HP: [{Player.hp} / {Player.max_hp}]

        {Game.appirition} HP: [{Game.hp} / {Boss.max_hp}]

    --------------------------------------------
            What do you want to do?

        > 1: Exorcise
        > 2: Horrify
        > 3: Escape
                                > 4: Inventory
    ____________________________________________
    """)
    else:
        print(f"""
    ____________________________________________

        - The {Game.appirition} approaches you -
    ---------------------------------------------

        HP: [{Player.hp} / {Player.max_hp}]

        {Game.appirition} HP: [{Game.hp} / {Ghost.max_hp}]

    ---------------------------------------------
            What do you want to do?

        > 1: Exorcise
        > 2: Horrify
        > 3: Escape
                                > 4: Inventory
    ____________________________________________
    """)
# --------------------------------------------------------------------------- #
# Displays The Help Screen #
def helps():
    print(f"""
    ____________________________________________

                    - Help Menu -

    --------------------------------------------
        General:
        Type out the command to use it.
        While in-game, click Options to access
        further options.

        Game:
        Pick a room to enter.
        In the room you will either, encounter
        a ghost, find an item, or continue.

        Fight deals damage to the enemy ghost.
        Fright allows you to scare the ghost
        off and progress to the next room.
        Flight allows you to end a fight but
        not progress to the next room.

        Souls allows you to recover Willpower.
        Ectoplasm allows you to permanently
        increase your stats.
        Haunted Candy allows you to Level up
        once.

        Tips:
        Flight has a higher chance of working
        than Fright.

        Fight as many ghosts as you can to
        level up, leveling up gives you a
        greater chance of using a move
        successfully
        and a lower chance of getting hit.
    ____________________________________________
        """)
    next = input()
    title()
# --------------------------------------------------------------------------- #
# Displays The Quit Screen #
def quit():
    os.system("cls")
    Game.run = False
    print("\n\tThanks For Playing")
# --------------------------------------------------------------------------- #
# Update Enemy #
def update():
        Boss.lvl = Game.floor * 10
        Boss.max_hp = randint(Boss.lvl * 20, Boss.lvl * 50)
        Boss.hp = Boss.max_hp
        Boss.str = randint(Boss.lvl , Boss.lvl * 2)
        Boss.dex = randint(Boss.lvl * 2, Boss.lvl * 5)
        Boss.hor = randint(Boss.lvl * 2, Boss.lvl * 5)

        Ghost.lvl = Game.room
        Ghost.max_hp = randint(Ghost.lvl * 2, Ghost.lvl * 5)
        Ghost.hp = Ghost.max_hp
        Ghost.str = randint(Ghost.lvl, Ghost.lvl * 2)
        Ghost.dex = randint(Ghost.lvl, Ghost.lvl * 2)
        Ghost.hor = randint(Ghost.lvl, Ghost.lvl * 2)
# --------------------------------------------------------------------------- #
title()
