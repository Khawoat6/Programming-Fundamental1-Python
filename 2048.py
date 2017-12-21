'''def merge(row):
    """ Returns a left merged row with zeros

    >>> merge([2, 2, 4, 4])
    [4, 8, 0, 0]
    >>> merge([0, 0, 4, 4])
    [8, 0, 0, 0]
    >>> merge([1, 2, 3, 4])
    [1, 2, 3, 4]
    """

    def inner(b, a=[]):
        """ 
        Helper for merge. If we're finished with the list,
        nothing to do; return the accumulator. Otherwise
        if we have more than one element, combine results of first
        with right if they match; skip over right and continue merge
        """

        if not b:
            return a
        x = b[0]
        if len(b) == 1:
            return inner(b[1:], a + [x])
        return inner(b[2:], a + [2*x]) if x == b[1] else inner(b[1:], a + [x])

    merged = inner([x for x in row if x != 0])
    return merged + [0]*(len(row)-len(merged))

def reverse(x):
    """ Returns a reversed list of x """
    return list(reversed(x))

def left(b):
    """ Returns a left merged board

    >>> merge([2, 2, 4, 0])
    [4, 4, 0, 0]
    """

    return [list(x) for x in map(merge, iter(b))]

def right(b):
    """ Returns a right merged board

    >>> reverse(merge(reverse([2, 2, 4, 0])))
    [0, 0, 4, 4]
    >>> reverse(merge(reverse([4, 4, 4, 4])))
    [0, 0, 8, 8]
    """

    t = map(reverse, iter(b))
    return [reverse(x) for x in map(merge, iter(t))]

def up(b):
    """ Returns an upward merged board
        NOTE: zip(*t) is transpose

    >>> b = [[2, 4, 0, 4],[2, 4, 4, 4],[2, 0, 0, 2],[2, 2, 0, 4]]
    >>> up(b)
    [[4, 8, 4, 8], [4, 2, 0, 2], [0, 0, 0, 4], [0, 0, 0, 0]]
    """

    t = left(zip(*b))
    return [list(x) for x in zip(*t)]

def down(b):
    """ Returns an upward merged board
        NOTE: zip(*t) is transpose

    >>> b = [[2, 4, 0, 4],[2, 4, 4, 4],[2, 0, 0, 2],[2, 2, 0, 4]]
    >>> down(b)
    [[0, 0, 0, 0], [0, 0, 0, 8], [4, 8, 0, 2], [4, 2, 4, 4]]
    """

    t = right(zip(*b))
    return [list(x) for x in zip(*t)]

def can_move(b):
    """ Returns the status (over/not over) of the game

    >>> b = [[1,2,3,4],[5,6,3,8],[1,2,3,4],[5,6,7,8]]
    >>> can_move(b)
    True
    >>> b = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]
    >>> can_move(b)
    False
    >>> b = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,0]]
    >>> can_move(b)
    True
    """

    def inner(b):
        for row in b:
            for x, y in zip(row[:-1], row[1:]):
                if x == y or x == 0 or y == 0:
                    return True
        return False
    return inner(b) or inner(zip(*b))
'''






##class Game2048:
##    """
##    A 2048 game client
##
##    Merge like tiles to reach tile 2048
##    """
##    def __init__(self):
##        self.b = [[0]*4 for i in range(4)]
##        self._spawn(2)
##
##    def _spawn(self, k):
##        dist = [2]*9 + [4]
##        rows = list(range(4))
##        cols = list(range(4))
##
##        random.shuffle(rows)
##        random.shuffle(cols)
##        count = 0
##        for r, c in itertools.product(rows, cols):
##            if count == k:
##                return
##            if self.b[r][c] == 0:
##                self.b[r][c] = random.sample(dist, 1)[0]
##                count += 1
##
##    def pprint(self):
##        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
##                         for row in self.b]))
##
##    def play(self):
##        while can_move(self.b):
##            self.pprint()
##            direc = input("Please enter a direction (w, a, s, d): ")
##
##            if   direc == "w": self.b = up(self.b)
##            elif direc == "s": self.b = down(self.b)
##            elif direc == "a": self.b = left(self.b)
##            elif direc == "d": self.b = right(self.b)
##            else:
##                continue 
##
##            self._spawn(1)
##



ef tab():
    return ({
        (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0,
        (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0,
        (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0,
        (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0
        })

def tab_reduc(t,d):
    if d in ('n', 'N'):
        # Merge whitespace
        for _ in range(4): # FIXME: Massive hack...
            for i in range(1,4):
                for c in range(1,5):
                    if t[i+0, c] == 0 and t[i+1, c] != 0:
                        t[i+0, c] = t[i+1, c]
                        t[i+1, c] = 0

        # Merge neighbors
        for i in reversed(range(1, 4)):
            for c in range(1,5):
                if t[i+0, c] == t[i+1, c] and t[i, c] != 0:
                    t[i+0, c] *= 2
                    t[i+1, c] = 0

        # Merge whitespace
        for _ in range(4): # FIXME: Massive hack
            for i in range(1,4):
                for c in range(1,5):
                    if t[i+0, c] == 0 and t[i+1, c] != 0:
                        t[i+0, c] = t[i+1, c]
                        t[i+1, c] = 0

def tab_print(t):
    for i in range(1, 5):
        for c in range(1, 5):
            print '{:2d}'.format(t[i,c]),
        print
    print

t = tab()
t[(1,4)] = 2
t[(2,4)] = 2
t[(3,4)] = 2
t[(4,4)] = 2
tab_print(t)
tab_reduc(t, 'N')
tab_print(t)
