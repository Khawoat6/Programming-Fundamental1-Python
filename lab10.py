##class Person:
##    def __init__(self, name):
##        self.name = name
##        self.power = 100
##
##    def say(self, to_whom, something):
##        print(self.name + ' say to ' + to_whom.name + ': ' + something)
##
##    def move(self):
##        print(self.name + ' is walking.')
##
##a = Person('Alice')
##b = Person('Bob')
##
##a.say(b, 'Hi, ' + b.name)
##a.move()
##b.move()

##class Person:
##    def __init__(self, name):
##        self.name = name
##        self.power = 100
##
##    def say(self, to_whom, something):
##        print(self.name + ' say to ' + to_whom.name + ': ' + something)
##
##    def move(self):
##        print(self.name + ' is walking.')
##
##class KUPerson(Person):
##    number_of_members = 0
##
##    def __init__(self, name):
##        Person.__init__(self, name)
##        KUPerson.number_of_members += 1
##        self.member_id = KUPerson.number_of_members
##
##    def move(self):
##        print(self.name + ' is riding a motorcycle.')
##        
##
##a = Person('Alice')
##b = KUPerson('Bob')
##c = KUPerson('Carl')

##class Person:
##    def __init__(self, name):
##        self.name = name
##        self.power = 100
##
##    def say(self, to_whom, something):
##        print(self.name + ' say to ' + to_whom.name + ': ' + something)
##
##    def move(self):
##        print(self.name + ' is walking.')
##
##class KUPerson(Person):
##    number_of_members = 0
##
##    def __init__(self, name):
##        Person.__init__(self, name)
##        KUPerson.number_of_members += 1
##        self.member_id = KUPerson.number_of_members
##
##    def move(self):
##        print(self.name + ' is riding a motorcycle.')
##        
##class Prof(KUPerson):
##    def __init__(self, name, rank):
##        KUPerson.__init__(self,name)
##        self.rank = rank
##        self.teaching = []
##
##    def add_teaching(self, subj):
##        self.teaching.append(subj)
##
##class Student(KUPerson):
##    def __ init__(self, name):
##        KUPerson.__init__(self, name)
##        self.year = 1
##
##    def set_year(self, year):
##        self.year = year 

    

##class Person:
##    def __init__(self, name):
##        self.name = name
##        self.power = 100
##
##    def say(self, to_whom, something):
##        print(self.name + ' say to ' + to_whom.name + ': ' + something)
##
##    def move(self):
##        print(self.name + ' is walking.')
##
##class KUPerson(Person):
##    number_of_members = 0
##
##    def __init__(self, name):
##        Person.__init__(self, name)
##        KUPerson.number_of_members += 1
##        self.member_id = KUPerson.number_of_members
##
##    def move(self):
##        print(self.name + ' is riding a motorcycle.')
##        
##class Prof(KUPerson):
##    def __init__(self, name, rank):
##        KUPerson.__init__(self,name)
##        self.rank = rank
##        self.teaching = []
##
##    def add_teaching(self, subj):
##        self.teaching.append(subj)
##
##class Student(KUPerson):
##    def __init__(self, name):
##        KUPerson.__init__(self, name)
##        self.year = 1
##
##    def set_year(self, year):
##        if year > 0:
##            self.year = year
##        else:
##            self.year = 1


##class Person:
##    def __init__(self, name):
##        self.name = name
##        self.power = 100
##
##    def say(self, to_whom, something):
##        print(self.name + ' say to ' + to_whom.name + ': ' + something)
##
##    def move(self):
##        print(self.name + ' is walking.')
##
##class KUPerson(Person):
##    number_of_members = 0
##
##    def __init__(self, name):
##        Person.__init__(self, name)
##        KUPerson.number_of_members += 1
##        self.member_id = KUPerson.number_of_members
##
##    def move(self):
##        print(self.name + ' is riding a motorcycle.')
##        
##class Prof(KUPerson):
##    def __init__(self, name, rank):
##        KUPerson.__init__(self,name)
##        self.rank = rank
##        self.teaching = []
##
##    def add_teaching(self, subj):
##        self.teaching.append(subj)
##
##class Student(KUPerson):
##    def __init__(self, name):
##        KUPerson.__init__(self, name)
##        self.year = 1
##
##    def set_year(self, year):
##        if year > 0:
##            self.year = year
##        else:
##            self.year = 1

##class Runner(Person):
##    def move(self):
##        print(self.name + 'is running.')
##
##class RunningStudent(Runner, Student):
##    def __init__(self, name):
##        Student.__init__(self, name)
##a = Runner('HI')
##a.move()



'''EX10.1
class Person:
    def __init__(self, name):
        self.name = name
class KUPerson(Person):
    number_of_member = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.teaching = []
class Prof(KUPerson):
    def __init__(self, name, rank):
        KUPerson.__init__(self, name)
        self.name = name
        self.rank = rank
    def add_teaching(self, subj):
        self.teaching.append((self.name ,subj))
class Department(Prof):
    def __init__(self, name):
        KUPerson.__init__(self,name)
        self.sum = []
    def add(self, who):
        for i in who.teaching:
            self.sum.append(i)
    def get_all_subj(self):
        return(self.sum)
##>>> p1 = Prof('Poonna', 'Full')
##>>> p2 = Prof('Anan', 'Full')
##>>> p1.add_teaching('Java')
##>>> p1.add_teaching('F#')
##>>> p2.add_teaching('AI')
##>>> cpe = Department('Computer Engineering')
##>>> cpe.add(p1)
##>>> cpe.add(p2)
##>>> cpe.get_all_subj()
##[('Poonna', 'Java'), ('Poonna', 'F#'), ('Anan', 'AI')]
'''


'''EX10.2
class Queue:
    def __init__(self):
        self.l = 1
        self.k = []
    def push(self, k):
        self.k.append(k)
    def pop(self):
        def god(g):
            r = []
            for i in range(-1, -len(g)-1, -1):
                r.append(g[i])
            return r
        self.l = self.l - 1
        if self.l == 0:
            self.k = god(self.k)
        return self.k.pop()
    def is_empty(self):
        if len(self.k) == 0:
            return True
        else:
            return False
##>>> q = Queue()
##>>> q.push(5)
##>>> q.push(3)
##>>> q.push(19)
##>>> q.push(10)
##>>> while not q.is_empty():
##	print(q.pop())
##
##	
##5
##3
##19
##10
'''


'''EX10.3
class Queue:
    def __init__(self):
        self.l = 1
        self.k = []
    def push(self, k):
        self.k.append(k)
    def pop(self):
        def god(g):
            r = []
            for i in range(-1, -len(g)-1, -1):
                r.append(g[i])
            return r
        self.l = self.l - 1
        if self.l == 0:
            self.k = god(self.k)
        return self.k.pop()
    def is_empty(self):
        if len(self.k) == 0:
            return True
        else:
            return False
class PriorityQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    def pop(self):
        def god(d):
            for i in range(len(d)-1):
                for j in range(len(d)-i-1):
                    if d[j] < d[j+1]:
                        d[j], d[j+1] = d[j+1], d[j]
            return d
        self.k = god(self.k)
        return self.k.pop()
##>>> q = PriorityQueue()
##>>> q.push(5)
##>>> q.push(3)
##>>> q.push(19)
##>>> q.push(10)
##>>> while not q.is_empty():
##	print(q.pop())
##3
##5
##10
##19
'''

















