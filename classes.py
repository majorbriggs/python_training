class MyClassWithRepr():
    def __init__(self):
        pass

    def __repr__(self):
        return "This is my class"


class MyClassWithoutRepr():
    def __init__(self):
        pass


x = MyClassWithoutRepr()

y = MyClassWithRepr()

print(x)
print(y)

class Vector1D():

    def __init__(self, *args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Vector1D can store only integer values")

        self._values = args

    def __str__(self):
        return self._values

    def __add__(self, other):
        if not isinstance(other, Vector1D):
            raise ValueError('Expected Vector1D, instead got {}'.format(other.__class__))

        if len(self._values) != len(other._values):
            raise ValueError('Added vectors have to have the same lenght')

        return [i + j for i, j in zip(self._values, other._values)]

    def __eq__(self, other):
        return self._values == other._values

    def __ne__(self, other):
        return self._values != other._values

A = Vector1D(1, 2, 3, 4)

B = Vector1D(5, 6, 7, 8)

C = A + B

print(A == B) # False

print(C)
# -> [6, 8, 10, 12]



class Animal():
    def __init__(self, name, make_sound_method):
        self.name = name
        self.make_sound = make_sound_method


def quack():
    print('Quack!')


def moo():
    print('Moooo!')


def bah():
    print('Bah!')


bah = Animal(name='Sheep', make_sound_method=bah)

bah.make_sound()