#python for text2
#lab9

##class Pet:
##    def say_hi(self):
##        print('Hi there.')

class RationalNumber:
    def __init__(self, nom, denom):
        self.nom = nom
        self.denom = denom

    def add(self, r):
        nom = self.nom * r.denom + r.nom * self.denom
        denom = self.denom * r.denom
        return RationalNumber(nom, denom)

    def show(self):
        print(str(self.nom)+'/'+str(self.denom))

##class RationalNumber:
##    def __init__(self, nom , denom):
##        self.nom = nom
##        self.denom = denom
##        
##    def add(self, r):
##        nom = self.nom * r.denom + r.nom * self.denom
##        denom = self.denom * r.denom
##        return RationalNumber(nom, denom)
##
##    def show(self):
##        print(str(self.nom)+'/'+str(self.denom))
