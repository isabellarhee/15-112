#classes !!!

'''
when defining a class, write keywrod Class followed
by the class name, some parenthesis, and a colon

when defining a method, first parameter is self
'''


class Dog(object):
    dogCatalog = [] 

    #constructor
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

        self.bones = 0

    def giveBone(self):
        self.bones += 1


    @staticmethod
    def getAllDogNames():
        return dogCatalog #missed this part

#C = Dog("Clifford", 20, "retriever")  making a dog

#class attribute -global variable attached to class
#static method - normal function, attached to class

#magic methods
#__init__ is one
'''
repr(A) is the same as a.__repr__()
A == A is the same as A.__eq__(B)
hash(A) is the same as A.__hash__()
almost all python builtin functions/operatiors have magic method

'''

#card example
def __hash__(self):
    return hash(self.getHashables())

def getHashables(self):
    return (self.number, self.suit) # for cards

def __eq__(self, other):
    return(isinstance(other, PlayingCard) and
            (self.number = other.number) and (self.suit != other.suit) )

def __repr__(self):
    #make it print real nice

'''
subclassing, all classes "inherit" from the object class
ex Dog will inherit methods from object class, such as object class'
repr method unless we overwrite them
super() -> allows to access overwritten version of method
ex fruits
'''
class Fruit(object):
    def __init__(self, name, genus, color):
        #blah
    def __repr__(self):
        #blah

class Citrus(Fruit):
    def __repr__(self):
        s = super.__repr__() # to get fruit method of repr

#isinstance works on subclasses

#-------------------------------------------------------
#oop free response
#create checklist: 
''''
__init__ takes numerator and denom
__repr__ represents as n/d
__eq__ with typecheck and same fraction represented
.times() nondestructively returns a fration from multiplying max, den*den

need to write __hash__
''''
class Fraction(object):
    def __init__(self, num, den):
        g = gcd(num, den)
        num //= g
        den //= g
        self.num = num
        self.den =den

    def __eq__(self, other):
        return isinstance(other, Fraction) and (self.num, self.den) == (other.num, other.den)

    def times(self, other):
        if isinstance(other, int):
            return Fraction(self.num * other, self.den)
        elif isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.den * other.den)

    def __hash__(self):
        return hash((self.num, self.den))


#----------cake class--------------------
class Cake(object):
    def __init__(self, flavor):
        self.flavor = flavor
        self.toppings = []

    def __repr__(self):
        return f'{self.flavor} Cake'

    def addTopping(self, topping):
        self.toppings.append(topping)

class FruitCake(Cake):
    def addTopping(self, topping):
        if len(self.toppings) < 2:
            super().addTopping(topping)

    def __repr__(self):
        return f'no one likes {self.flavor} fruitcakes'

class YummyCake(Cake):
    usedCombos = []
    def __init__(self, flavor, frosting):
        super().__init__(flavor)
        self.frosting = frosting
        YummyCake.usedCombos.append((flavor, frosting))

    def __repr__(self):
        return f'{self.flavor} YummyCake with {self.frosting} frosting'

    def __eq__(self, other):
        return isinstance(other, YummyCake) and self.frosting == other.frosting
                and self.flavor == other.flavor

    def __hash__(self):
        return hash((self.flavor, self.frosting))

    @staticmethod         
    def hasUsedFlavorCombo(flavor, frosting):
        return (flavor, frosting) in usedCombos