# -*- coding: utf-8 -*-

from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print"You have to define the scene."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('saved')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out last scene
        current_scene.enter()

class Lose(Scene):

    quips = [
        "You are dead and your teammate is probably too.",
        "You failed your mission.",
    ]

    def enter(self):
        print Lose.quips[randint(0, len(self.quips)-1)]
        exit(1)


class Battle(Scene):

    def enter(self):
        global name
        print "\n"
        print "It's the year 3008. You are on a mission to find your teammate and friend."
        print "You and your team were on your usual way to save the universe."
        print "All five of you in their own fighter-class spaceships. Everything"
        print "Was well until you were attaced by a whole fleet of evil alien ships."
        print "You tried to flee with your whole team, flying through a wormhole in formation."
        print "None of you noticed the single enemy fighter that managed to follow you."
        print "Only four of you made the jump through the wormhole. One of your teammates"
        print "was shot by the enemy and dissapeared."
        print "What is your teammates name?"
        name = raw_input("> ")

        print "Your tech obsessed and super smart teammate managed to calculate where"
        print "your lost teammates ship might have crashed. They could narrow it down"
        print "to one single planet."
        print "You are currently on your mothership and approaching said planet."
        print "Your teamlader is about to start the breifing on your mission when suddenly"
        print "the ships alarms get off. You are under attack again."
        print "Your teamleader turns to you and commands you to run to the ships hangar,"
        print "get in your pod and fly to the planet."
        print "'You need to get to %s before they do!'" % name
        print "..."
        print "You can see a battle raging on behind you. Thankfully the enemy did not seem"
        print "to notice the leaving vessel. This could be your chance to launch"
        print "a surprise attack on them."
        print "Will you engage in combat?"
        choice = raw_input("> ")

        if choice == "yes":
            print "You decide to neglect your possibly injured friend, disobey orders"
            print "and attack the enemy ship."
            print "You did not really think that this would end well did you?"
            print "Sadly your surpise attack fails. The enemy's ship radar decets you."
            print "They immediately shoot you with their laser cannons and you die."
            return 'lose'

        elif choice == "no":
            print "You decide to obey orders and save %s." % name
            return 'open_field'

        else:
            print "Try somethin else."
            return 'battle'




class OpenField(Scene):

    def enter(self):
        print "You land on a opne field on the planet."
        print "Your ships scanners detect small lifeforms but they are not big enough"
        print "to be your teammate. There is also no ship wreck anywhere nearby."
        print "You will have to search somewhere else."
        print "Not far too away you can see a wood. If you look to the other side"
        print "you can see mountains in the distance."
        print "In the whole twenty years you have lived in this universe,"
        print "You never had to make such a hard decision."
        print "Where do you think %s could have crashed?" % name

        choice = raw_input("> ")

        if choice == "woods":
            return 'woods'

        elif choice == "mountains":
            return 'mountains'

        else:
            print "That is not an option."
            return 'open_field'


class Mountains(Scene):

    def enter(self):
        print "You fly over the mountains, scanning the planets surface below."
        print "Thee is barely any sign of living organisms."
        print "What you can detect are broken pieces of what once must have been"
        print "a space ship. It looks a lot like the ship you are currently sitting"
        print "in. However it is impossible to say for sure. There also is a gigantic"
        print "cave that seems to lead deep into the mountain. If %s really" % name
        print "crashed here and survived they might have gone into the cave to hide."
        print "Would you like to examine the cave?"

        choice = raw_input("> ")

        if choice == "yes":
            print "You find a place to land your ship and make your way to the cave's"
            print "entrance. There are bones lying around everywhere. You can hear"
            print "your blood pumping. You enter the cave."
            print "There are sounds coming from inside. It's some kind of rustling."
            print "You think it might be %s." % name
            print "You continue walking thorough the cave, the fancy gadgets of you"
            print "space suit lighting up your surroundings."
            print "Suddenly you hear someone or rather something growling."
            print "Everything happens so fast. The last thing you ever see is a giant"
            print "shadowy figure flying towards you."
            return 'lose'

        elif choice == "no":
            print "Since there is noting else here to check out you fly towards"
            print "the woods. Surely %s will be there." % name

        else:
            print "Try typing somethin else."
            return 'mountains'


class Woods(Scene):

    def enter(self):
        print "As you are flying over the wood you notice a big white sheet lying"
        print "on top of the trees. This must be a parachute!"
        print "You are filled with hope and land your ship nearby."
        print "You run towards the place where you saw the parachute."
        print "The parachute is hanging in the trees but there is no teammate nearby."
        print "You can feel your heart sink."
        print "What will you do? Give up or keep looking?"

        choice = raw_input("> ")

        if choice == "give up":
            print "You give up searching for %s and start walking" % name
            print "back towards your ship. You don't care waht your other teammates"
            print "will think of you. You don't care about anything anymore."
            print "You walk without paying attention to your surroundings."
            print "Your inattentive behaivour leads to you being attacked and"
            print "eaten by a wild animal."
            return 'lose'

        elif choice == "keep looking":
            print "Maybe %s managed to get to safety somewhere."
            print "You start looking for clues."
            print "You stop in your tracks when you see a puddle of blood near a tree."
            print "Your eyes follow the little drops of blood that lead away from the"
            print "parachute. And oddly enough into the same direction you just came from."
            print "How could you not have noticed that before?"
            print "You follow the tracks back to your ship. Careful to not attract"
            print "the wild animals attention."
            print "Back at your ship you notice that it's locked. From inside."
            print "In order to get inside you will have to punch in the corrcect code."
            print "You remember that you set your birthyear as the access code for"
            print "Your ship. You have three guesses."

            code = "2988"
            guess = raw_input("[keypad]> ")
            guesses = 0

            while guess != code and guesses < 3:
                print "That was the wrong code!"
                guesses += 1
                guess = raw_input("> ")

                if guess == "2988":
                    print "You unlock the ship and it opns with a hiss."
                    print "Inside you see %s. They are unconcious and bleeding" % name
                    print "from the scratches they must have gotten from landing inside a tree."
                    print "They seem fine otherwise. You bandage the deepest wounds"
                    print "and start your way back to your mothership."

                    return 'saved'


                else:
                    print "That was the wron code. One might think you would be capable"
                    print "of remembering your birthyear. Since it was exactly 20 years ago"
                    print "that you were born. The math should not be too hard."
                    print "Not knowing what else to do, you sit outside your ship, waiting"
                    print "for somethin to happen. Soon it turns dark and you hear some rustling"
                    print "in the bushes. Then suddenly a dark figure is leaping towards you."
                    print "It's big claws reaching for your face."
                    print "You die."
                    return 'lose'



class Saved(Scene):

    def enter(self):
        print "When you arrive there is no enemy ship to be seen."
        print "your team won and you brought %s savely home." % name
        return 'saved'



class Map(object):

    scenes = {
        'battle': Battle(),
        'open_field': OpenField(),
        'mountains': Mountains(),
        'woods': Woods(),
        'saved': Saved(),
        'lose': Lose(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('battle')
a_game = Engine(a_map)
a_game.play()
