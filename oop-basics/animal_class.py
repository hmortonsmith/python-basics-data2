class Animal:

    def __init__(self, colour = ''):
        self.lungs = True
        self.eyes = True
        self.alive = True
        self.colour = colour
        self.age_days = 0
        self.hearts = 1

    def __aging(self): ##double underscore makes a method private (encapsulation)
        self.age_days += 1

    def sleep(self):
        print('zzzzllleeeep...zzz')
        self.__aging()

    def eat(self, food = ''):
        print('nom nom nom... NOM', food)

    def breathe(self):
        print(' INHALE ......... (hold) .........EXHALE')

    def potty(self):
        print('0.0 .... uhhh 0.o ....plop o.o')

    def what_are_you(self):
        print(self.origin)
