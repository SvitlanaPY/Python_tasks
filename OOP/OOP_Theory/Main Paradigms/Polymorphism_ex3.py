"""
7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.
Create two instances, one of Bear and one of Wolf,
make a tuple of it and by using for call their action using the same method.
"""


class Bear:
    def make_sound(self):
        print("RRRRRRRRR")


class Wolf:
    def make_sound(self):
        print("Woooooooo")


bear = Bear()
wolf = Wolf()
b_w = (bear, wolf)

for elem in b_w:
    elem.make_sound()
# OUTPUT: RRRRRRRRR
# OUTPUT: Woooooooo
