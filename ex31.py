# -*- coding: utf-8 -*-

print "You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?"

door =raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a chese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Greet the bear and ask it about their day."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        print "You befriend the bear and get a piece of cake."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    print "4. Who is Cthulu and what is a Lovecraft?"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mindof jello. Good job!"

    elif insanity == "4":
        print "You are sitting in a classroom. The walls are painted red. There is a single piece of paper in front of you. It's blank."

    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You are sucked out into the endless void of space."
    print "1. Cry for your mommy."
    print "2. Accept your fate."

    fate = raw_input("> ")

    if fate == "1":
        print "The Allmother emerges, sings you a lullaby and tucks you into bed."

    elif fate == "2":
        print "You die."

    else:
        print "Your lifeless body floats through the galaxy for all eternity. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
