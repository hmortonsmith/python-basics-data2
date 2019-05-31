from animal_class import Animal

# define a reptile from animal


class Reptile(Animal):

    def __init__(self, colour = ''):
        super().__init__(colour) # Run the init of parent class
        self.hearts = 4
        self.cold_blood = True

    def eat(self, food = ''):
        print('nom nom nom, found some tasty reptile food')
        print(f'OH snap I found some {food}')

    def seek_heat(self):
        print('find heat')

    def hunt(self):
        print('hunt')
