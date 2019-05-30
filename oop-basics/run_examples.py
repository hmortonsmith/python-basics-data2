from animal_class import *
from reptile_class import *
# run examples here

animal_1 = Animal()
print(type(animal_1))
animal_1.potty()

ringo = Reptile()
# ringo has all behaviours of animal + reptile behaviours
ringo.sleep()
ringo.seek_heat()
ringo.hunt()
ringo.eat('eggs of innocent birds')
