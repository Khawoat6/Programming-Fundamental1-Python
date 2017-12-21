##class Pet:
##    def say_hi(self):
##        print('Hi there.')
##
##    def play_with(self, owner):
##        print('I am playing with ' + owner)

##class Pet:
##    tricks = []
##    def say_hi(self):
##        print('Hi there.')
##
##    def add_trick(self, trick):
##        Pet.tricks.append(trick)
##
##p = Pet()
##q = Pet()
##p.add_trick('roll over')
##q.add_trick('play dead')
##print(p.tricks)

##class Pet:
##    def say_hi(self):
##        print('Hi there. My name is ' + self.name + '.')
##
##    def set_name(self, name):
##        self.name = name
##
##p = Pet()
##q = Pet()
##p.set_name('Panther')
##q.set_name('Cheetah')
##p.say_hi()
##q.say_hi()

##class Pet:
##    def __init__(self):
##        self.tricks = []
##
##    def add_trick(self, trick):
##        self.tricks.append(trick)
##
##p = Pet()
##q = Pet()
##
##p.add_trick('jump')
##q.add_trick('play dead')
##
##print(p.tricks, q.tricks)

##class Pet:
##    number_of_pets = 0
##    def __init__(self, name ='', kind = 'pet', tricks = None):
##        self.name = name
##        self.kind = kind
##        if tricks == None:
##            self.tricks = []
##        else:
##            self.tricks = tricks
##        Pet.number_of_pets += 1
##    def say_hi(self):
##        print('Hi there. My name is ' + self.name + '. I am a ' + self.kind + '.')
##
##    def add_trick(self, trick):
##        self.tricks.append(trick)
##
##p = Pet(name ='Panther', kind = 'cat')
##q = Pet('Pluto', tricks = ['play balls'])
##
##p.say_hi()
##print(p.tricks)
##print(p.number_of_pets)
##
##q.say_hi()
##print(q.tricks)
##print(q.number_of_pets)

##class RationalNumber:
##    def __init__(self, nom, denom):
##        self.nom = nom
##        self.denom = denom
##
##    def add(self, r):
##        nom = self.nom * r.denom + r.nom * self.denom
##        denom = self.denom * denom
##        return RationalNumber(nom, denom)
##
##    def show(self):
##        print(str(self.nom) + '/' + str(self.denom))
##        



##class RationalNumber:
##    def normalize():


'''EX9.1
class RationalNumber:
    p = []
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def normalize(self):
        def god1(x, y):
            m = 0
            n = 0
            for i in range(y + 1):
                if i != 0 and x % i == 0 and y % i == 0 :
                    m = int(x / i)
                    n = int(y / i)
            return m
        def god2(x, y):
            m = 0
            n = 0
            for i in range(y + 1):
                if i != 0 and x % i == 0 and y % i == 0 :
                    m = int(x / i)
                    n = int(y / i)
                return n
        a = god1 (self.a , self.b)
        b = god2 (self.a , self.b)
        self.a = a
        self.b = b
        return RationalNumber(a, b)
    def show(self):
        print(str (self.a) + '/' + str (self.b))
#>>>r = RationalNumber(15,50)
#>>>r.normalize()
#>>>r.show()
#3/10
'''

'''EX9.2
class RationalNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, r):
        a = self.a * r.b+r.a * self.b
        b = self.b * r.b
        self.a = a
        self.b = b
        return RationalNumber.normalize(self)
    def normalize(self):
        def god1(x, y):
            m = 0
            n = 0
            for i in range(y + 1):
                if i != 0 and x % i == 0 and y % i == 0 :
                    m = int(x / i)
                    n = int(y / i)
            return m
        def god2(x, y):
            m = 0
            n = 0
            for i in range(y + 1):
                if i != 0 and x % i == 0 and y % i == 0 :
                    m = int(x / i)
                    n = int(y / i)
            return n
        a = god1(self.a, self.b)
        b = god2(self.a, self.b)
        self.a = a
        self.b = b
        return RationalNumber(a, b)
    
    def show(self):
        print(str(self.a)+ '/'+str(self.b))
#>>>RationalNumber(15,50).add(RationalNumber(15,50)).show()
#3/5
'''

'''EX9.3
class Set:
    def __init__(self):
        self.k = []
    def add(self, r):
        if self.k == []:
            self.k.append(r)
        for i in self.k :
            if i != r:
                self.k.append(r)
        if self.k != []:
            for i in range(len(self.k)-1):
                for j in range(len(self.k)):
                    if i != j and self.k[i] == self.k[j]:
                        self.k.remove(self.k[i])
    def remove(self, r):
        for i in self.k:
            if i == r:
                self.k.remove(r)
    def uion(self, r):
        for i in self.k:
            r.k.append(i)
        return r
    def intersec(self, r):
        inter = []
        for i in r.k:
            if r.k == self.k:
                inter.append(self.k)
        return inter
    def count(self):
        print(len(self.k)-1)
    def show(self):
        a = sorted(self.k)
        print(set(a))

##>>> s1 = Set()
##>>> s1.add(5)
##>>> s1.add(3)
##>>> s1.add(19)
##>>> s2 = Set()
##>>> s2.add(3)
##>>> s2.add(9)
##>>> s2.add(9)
##>>> s1.show()
##{19, 3, 5}
##>>> s2.show()
##{9, 3}
##>>> r = s1.uion(s2)
##>>> r.show()
##{19, 9, 3, 5}
##>>> r.count()
##4
'''
