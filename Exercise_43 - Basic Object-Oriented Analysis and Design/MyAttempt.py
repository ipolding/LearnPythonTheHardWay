

class Scene(object):
    """  Each room will print its own description when the player enters it and then tell the engine what room to run next out of the map """

    def enter(self):
        pass


class Engine(object):
    """ Engine that runs a map full of rooms or scenes """

    def __init__(self, scene_map):
        

    def play(self):
        pass

class Death(Scene):

    def enter(self, cause):
        if cause == "hive mind":
            print "The hive mind takes control of your mind...and your bowels. You make your last movement."
        elif cause == "gothon":
            print "The gothon leaps down from the vents. It injects an acid into your mouth."
            print "It is a laxative. You make your last movement."

class CentralCorridor(Scene):

    """ This is the starting point and has a Gothon already standing there they have to defeat with a joke before continuing."""


    def enter(self, bomb):
        if bomb == True:
            print "With the bomb in hand, you run for the bridge!"
            print bridge.enter(bomb)
        else:
            print "The corridor is long with multiple doors"
        
        

class LaserWeaponArmory(Scene):
    """ This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad he has to guess the number for."""

    def enter(self):
        print "You are in the armory." 
        print "There is a sign saying Neutron bomb behind a locked door."
        print "It has a keypad on it. You try to enter the code."
        key_code = randint(0, 10)
        while True:
            attempt = raw_input("You enter: ")
            if int(attempt) == key_code:
                print "It opened! You pick up the bomb"
                hasBomb = True
                centralCorridor.enter(hasBomb)
            else:
                print "Damn! The code didn't work!"         
        
class TheBridge(Scene):

    """ Another battle scene with a Gothon where the hero places the bomb. """

    def enter(self, bomb):
        if bomb == True:
            print "You place the bomb on the podium." 
            print "Now you must escape!"
        else:
            print "You look around. There is a bomb shaped podium next to the Gothon hive mind, keeping the escape pods locked!"
            decision = raw_input("What do you do? ")
            if "hive mind" in decision:
                Engine('death')
                eath.enter("hive mind")
                
                  
        

class EscapePod(Scene):
    """ Where the hero escapes but only after guessing the right escape pod. """

    def enter(self):
        pass


class Map(object):
    """ tell the engine what room to run next out of the map """

    def __init__(self, start_scene):
        scene_dict = {'central_corridor': CentralCorridor, 'the_bridge': TheBridge, 'armory': LaserWeaponArmory, 'escape_pod': EscapePod}
        scene = scene_dict[scene_map]()
        scene.enter()
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

