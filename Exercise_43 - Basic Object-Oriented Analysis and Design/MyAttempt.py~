from random import randint

class Scene(object):

    def enter(self):
        pass


class Engine(object):
    """ Runs a map full of scenes"""
    ''' has-a Map'''

    def __init__(self, scene_map):
        self.scenes = scene_map

    def play(self):
        self.scenes.opening_scene().enter()
        
    def get_next_scene(self, scene_name):
        return self.scenes.next_scene(scene_name)
        
        
        

class Death(Scene):

    def __init__(self, reason):
        self.reason = reason

    def enter(self):
        if self.reason == "Gothon":
            print "The Gothon kills you. Game over."
            exit(0)
        if self.reason == "acid":
            print "You corrode to death. Game over."
            exit(0)
        elif self.reason == "no fuel":
            print "The escape pod has no fuel. You drift to your death"
            exit(0)                   
        elif self.reason == "no oxygen":
            print "The escape pod has no oxygen. You suffocate"
            exit(0)            

class CentralCorridor(Scene):

    def enter(self):
        print "You are in the central corridor. A gothon attacks. Defeat him with a joke."
        print "You know two jokes:"
        print "1. Why did the chicken cross the road?"
        print "2. What is black and white and red all over"
        joke_choice = raw_input("What joke do you choose?")
        if joke_choice == '1':
            print "To get to the other side!"
            print "The Gothon dies laughing"
            a_game.get_next_scene('central_corridor').enter()
            
            
        elif joke_choice == '2':
            print "...a penguin! ..."
            print "The Gothon is not amused"
            Death("Gothon").enter()
            

class LaserWeaponArmory(Scene):

    def enter(self):
        print "You are in the armory"
        print "There is a key pad which wants a single digit answer"
        self.code_cracked = False
        while not self.code_cracked:        
            answer = 1
            code = int(raw_input("What is the code?"))
            #answer = randint(1,9)
            if code == answer:
                print "You have the bomb!"
                self.code_cracked = True
                next_scene = a_game.get_next_scene('armory')
                next_scene.enter(self.code_cracked)
                break
            

class TheBridge(Scene):

    def __init__(self):
        pass
    
    def enter(self, hasBomb):
        if hasBomb == True:
            print "You have reached the bridge"
            print "A gothon attacks"
            while True:
                attack = raw_input("Do you: \n Kick him in the balls? \n or \n Punch him in the bum")
                if "balls" in attack:
                    "His balls were acid glands"
                    Death("acid").enter()
                elif "bum" in attack:
                    print "Every alien needs a bum. He dies."
                    print "You place the bomb and blow up the bridge"
                    a_game.get_next_scene('the_bridge').enter()
                else:
                    print "Come on!"
        
        
     
        

class EscapePod(Scene):

    def enter(self):
        print "Choose an escape pod"
        while True:
            response = raw_input("Do you choose the middle, left, or right escape pod?")
            if "middle" in response:
                print "Congratulations. You escape and you have won."
            elif "left" in response:
                Death("no fuel").enter()
            elif "right" in response:
                Death("no oxygen").enter()
            else:
                print "This is no time to fool around!"
                


class Map(object):
    """ Collection of scenes """
    scene_dict = {}
    
    def __init__(self, start_scene):
        self.scene_dict = {'central_corridor': CentralCorridor(), 'the_bridge' : TheBridge(), 'the_bridge': EscapePod()}
        self.scene_dict[start_scene]
        
    def next_scene(self, scene_name):
        """ return a collection of next scenes """
        next_scene_dict = {'central_corridor': LaserWeaponArmory(), 'armory' : TheBridge(), 'the_bridge': EscapePod()}
        ''' return the corresponding next scene, given the start scene'''
        return next_scene_dict[scene_name]

    def opening_scene(self):
        return CentralCorridor()


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()



