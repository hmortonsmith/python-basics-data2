from animal_class import *
from reptile_class import *
# run examples here

# animal_1 = Animal()
# print(type(animal_1))
# animal_1.potty()
# print(animal_1.age_days, 'days old')
# animal_1.sleep()
# print(animal_1.age_days, 'days old')

ringo = Reptile('green')
# ringo has all behaviours of animal + reptile behaviours
ringo.sleep()
ringo.seek_heat()
ringo.hunt()
ringo.eat('reptile food')
print(ringo.colour)
print(ringo.hearts)