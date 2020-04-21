#practice questions

def is_multiple(n, m) :
    return (m % n == 0 if type(m // n) == int else False )

def is_even(k) :
    even = False
    for i in range(0, (k+1), 2) :
        if i == k :
            even = True
    return even

def minmax(data) :
    sorted(data)
    return data[0],data[-1]

def sum_squares(n) :
    return sum((i**2 for i in range(n)))

def oddsum_squares(n) :
    return sum(map(lambda x: x**2,(filter(lambda x : x % 2 != 0 , range(n)))))

def productodd(seq) :
    z = []
    for i in range(len(seq)) :
        for j in range(len(seq)) :
            if seq[i] != seq[j] :
                product = seq[i] * seq[j]
                if product % 2 != 0 :
                    z.append((seq[i],seq[j]))
    if len(z) > 0 :
        return True
    return False

def distinct(seq) :
    list = [seq[0] ]
    for i in range(len(seq))  :
        if seq[i] not in list :
            list.append(seq[i])

    if len(list) < len(seq) :
        return 'Not Distinct'
    return 'Distinct'

list = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
    #   0  1  2   3   4   5   6   7   8   9
    #   1  2  3   4   5   6   7   8   9   10

LIST = [i * (i +1) for i in range(10)]

def countvowels(string) :
    vowel_counts = {}
    for vowels in 'aeiou' :
        count = string.lower().count(vowels)
        vowel_counts[vowels] = count
    return vowel_counts

def sortfactors(n) :
    l = []
    for i in factors(n) :
        l.append(i)
    return sorted(l)

def factors(n): # generator that computes factors
    k=1
    while k * k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k

def sortfactors(function):
    l = []
    for i in function:
        l.append(i)
    return sorted(l)


def norm(v, p =2) :
    z = (sum(map(lambda x: x ** p ,v)))**(1/p)
    print(z)

list = ['c', 'a', 't', 'd', 'o', 'g']

def permutations(x) :
    if len(x) == 0 :
        return []
    if len(x) == 1 :
        return x
    l = []
    for i in range(len(x)) :
        m = x[i]

        z = x[:i] + x[i+1:]

        for j in permutations(z):
            l.append([m] + z)
        return l

def timesdivisibley2(integer) :
    if integer <= 2  :
        return('Invalid Input')
    elif integer > 2:
        while integer > 2 :
            integer = integer/ 2
            count += 1
        return (count)



def change(c, g) :
    available_change = [2, 5, 10, 0.1, 0.5, 0.2, 1]
    z = {}
    if c == g :
        return 'No Change is given'
    elif c < g :
        amt = g - c
        print(amt//10, '10 dollars')
        amt = amt % 10
        print(amt // 5, '5 dollars')
        amt = amt % 5
        print(amt // 2, '2 dollars')
        amt = amt % 2
        print(amt // 1, '1 dollars')
        amt = amt % 1
        print(amt // 0.5, '50 cents')
        amt = amt % 0.5
        print(amt // 0.2, ' 20 cents')
        amt = amt % 0.2
        print(amt // 0.1, '10 cents')

def fibonacciprogression() :
    a = 0
    b = 1
    for i in range(100):
        print(a)
        future = a + b
        a = b
        b = future

class Flower :
    def __init__(self, name, petals, price) :
        self._name = name
        self._petals = int(petals)
        self._price = float(price)

    def __str__(self):
        return self._name

    def get_petals(self):
        return self._number

    def get_price(self):
        return self._price

Rose = Flower('Rosie', 10, 40.50)

class CreditCard :
    def __init__(self, customer, bank, acnt, limit, balance = 0):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_acnt(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        '''Charge the card assuming sufficient credit limit
        return True if charge was processed; False if charge was denied'''
        if isinstance(price, (int,float)):
            if price + self._balance > self._limit :
                return False
            else:
                self._balance += price
                return True
        else:
            raise TypeError ('amount must be numeric')

    def make_payment(self, amount):
        '''Process customer payment that reduces balance'''
        if not isinstance(amount, (int,float)):
            raise TypeError ("Amount must be numeric")
        elif amount < 0 :
            raise ValueError ("Amount must be positive")
        self._balance -= amount


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d,):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:  # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        '''return the difference between two vectors'''
        if len(self) != len(other) :
            raise ValueError ('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

    def __neg__(self):
        """Return copy of vector with all coordinates negated."""
        result = Vector(len(self))
        for j in range(len(self)) :
            result[j] = -self[j]
        return result

    def __lt__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords

    def __le__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords

    def __mul__(self, factor):
        '''return a copy of the vector with all coordinates negated'''
        result = Vector(len(self))
        for j in range(len(self)) :
            result[j] = self[j] * factor
        return result

    def __rmul__(self, factor):
        '''return a copy of the vector with all coordinates negated'''
        result = Vector(len(self))
        for j in range(len(self)) :
            result[j] = factor * self[j]
        return result

    def __mul__(other1, other2):
        """Return copy of vector with all coordinates negated."""
        result = 0  # start with vector of zeros
        for j in range(len(other1)):
            result += other1[j] * other2[j]
        return result

class ReversedSequenceIterator :
    def __init__(self, seq) :
        self._seq = seq
        self._length = len(seq)

    def __next__(self):
        self._length -= 1
        if self._length > -1 :
            return self._seq[self._length]
        else:
            raise StopIteration

    def __iter__(self):
        return self
