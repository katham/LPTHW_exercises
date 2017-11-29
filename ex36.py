# -*- coding: utf-8 -*-

from sys import exit

clothes = False
pie = False

def start():
    print "You wake up and find yourself in your bed."
    print "It`s warm and cozy."
    print "Will you get up or turn around and keep sleeping?"

    choice = raw_input("> ")

    if choice == "get up":
        bedroom()
    elif choice == "sleep":
        print "You drift back to sleep and dream about applepie and school."

def bedroom():
    print "It's dark. You can't see anything."
    print "Do you want to turn on the lights?"

    choice = raw_input("> ")

    if choice == "yes":
        print "It takes a moment for your eyes to adjust to the brightness."
        print "..."
        print "You look around your room."
        print "There is a door and a wardrobe in front of you."
        print "Do you want to leave the room or open the wardrobe?"

        choice = raw_input("> ")

        if "leave" in choice:
            hallway()
        elif choice == "wardrobe":
            wardrobe()

    elif choice == "no":
        print "It's too dark to see anything and you are still groggy from sleep."
        print "You sumble over something and fall back into bed."
        print "The mattres is still warm and the sheets hug you softly."
        print "You fall asleep."

def hallway():
    print "You exit your bedroom and enter a hallway."
    print "Will you go left or right?"

    choice = raw_input("> ")

    if choice == "left":
            kitchen()
    elif choice == "right":
            crossroad()

def wardrobe():
    global clothes
    print "Inside you find your clothes."
    print "Will you put some of them on?"

    choice = raw_input("> ")

    if choice == "yes":
            clothes = True
            print "Now you are ready for the world. You walk out of your room."
            hallway()
    elif choice == "no":
            print "Thats okay. I won't judge you."
            print "I guess some people really prefer to only wear underwear."
            hallway()

def kitchen():
    print "You find yourself in the kitchen."
    print "It's your normal kitchen. It looks like it always does."
    print "There is the kitchen counter, a few chairs, the microwave oven and the fridge."
    print "What of these things would you like to check out?"
    print "Or do you want to go back to the hallway?"

    choice = raw_input("> ")

    if choice == "hallway":
            hallway2()
    elif choice == "counter":
            print "There is nothing here. Not a single crumb."
            print "You remember that you cleaned the kitchen yesterday before going to bed."
            kitchen()
    elif "chair" in choice:
            print "The chairs are red. You sit one one."
            print "This reminds you of your bed back in your room."
            print "You want to go back to sleep."
            print "But something in the back of your mind tells you to hurry."
            kitchen()
    elif choice ==  "microwave":
            print "There is nothing here what did you expect?"
            print "Wait ther are some drops of dried tomato sauce."
            print "You forgot to clean the microwave yesterday! That's not good!"
            print "But right now you dont have time for this."
            kitchen()
    elif choice == "fridge":
            print "There is some leftover pie here."
            print "Do you want to eat it?"

            choice = raw_input("> ")

            if choice == "yes":
                global pie
                pie = True
                print "Hmmm that was tasty."
                kitchen()

            if choice == "no":
                print "That's okay."
                kitchen()

def hallway2():
    print "You are back in the hallway."
    print "Let's go to the other end of it."
    print "You pass your bedroom door. Do you want to enter it?"

    choice = raw_input("> ")

    if choice == "yes":
            bedroom2()
    elif choice == "no":
            crossroad()

def beedroom2():
    print "You look around your room."
    print "There is a door and a wardrobe in front of you."
    print "Do you want to leave the room or open the wardrobe?"

    choice = raw_input("> ")

    if choice == "leave":
        hallway()
    elif choice == "wardrobe":
        wardrobe()

def crossroad():
    print "The hallway leads straight to a door."
    print "Do you want to open it?"

    choice = raw_input("> ")

    if choice == "yes":
            print "You walk through the door."
            print "Now you are standing outside. It's snowing."
            print "You hear the door fall shut behind you."
            print "Oh no! You locked yourself out."

            if clothes == True:
                print "There is a path leading away from the house."
                print "Do you want to follow it?"

                choice = raw_input("> ")

                if choice == "yes":
                        path()

                else:
                    print "Then let's just wait here and do nothing."
                    print "..."
                    print "After a few hours you fall asleep and never wake up again."

            else:
                print "This is bad. It's so cold and you are only wearing underwear."
                print "No, don't sit down. I know you are cold but you can't give up now."
                print "Okay but listen ...o me: Do ...ot fall aslee......"
                print "........."
                print "You don't wake up again."

    else:
        print "That is probably the better choice."
        print "Let's go back to sleep."

def path():
    print "The path leads you through a snowfield and into a small wood."

    if pie == True:
        print "You keep walking and eventually get to a road."
        print "You see a schoolbus."
        print "One of the students inside waves to you."
        print "Will you get into the bus?"

        choice = raw_input("> ")

        if choice == "yes":
                print "Congratulations! You got to school on time! Well done!"
        else:
                print "The bus leaves without you."
                print "There wont be another bus coming for a long time."
                print "You have nothing left to do but sit on the bench at the bus stop."
                print "After some time you are hungry, exhausted and freezing."
                print "You fall asleep."
                print "..."
                print "You feel someone touching you."
                print "They pick you up and carry you away."
                print "..."
                start()

    else:
        print "The walk through the woods is exhausting."
        print "You are breating heavily and start to regret that you did not have breakfast."
        print "Eventually you collapse at the side of the path."
        print "You never wake up."




start()
