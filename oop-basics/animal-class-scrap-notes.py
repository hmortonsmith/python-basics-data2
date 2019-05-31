class Animal:
    origin = 'I am an animal from the animal kingdom.. (on earth)'
    # Class is an object blueprint
    # Stores how it looks (method__init__) and how it behaves (methods)
# Special method that runs initially whenver you create an object of this class
# Initialization method
    def __init__(self, species, colour = '', loc = ''):
        self.species = species
        self.alive = True
        self.colour = colour
        self.location = loc
        self.eye = True
        self.lungs = True
        self.cold_blood = False

    # Behaviour (method)
    def sleep(self):
        print('soooo sleeepy... zzleeeep.. zzzzz')

    def breathe(self):
        print('INNNHALLEEEE..... (hold) ... EXHALEEEEE')

    def eat(self, food = ''):
        print('nom nom nom... NOM!', food)
        ## food = '' makes food optional

    def potty(self):
        print('0.0 .... uhhh 0.o ....plop o.o')

    def what_are_you(self):
        # Self refers to the instance of animal class, not the class
        print(self.origin)

# To call the method we need an Animal Object
# instanciate an Animal object
# Create animal using Animal()

doggo = Animal('Doggo')
print(doggo)
print(type(doggo))

# Now that you have an Animal, you can call method on it

doggo.breathe()
doggo.eat('rabbits')
doggo.sleep()
doggo.potty()

doggo.what_are_you()
print(doggo.origin)
print(doggo.species)
print(doggo.colour)



