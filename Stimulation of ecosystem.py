import random

class Animal :
    def __init__(self, gender=None , strength=None) :
        if gender == None :
            self._gender = random.choice(['M', 'F'])
        else:
            self._gender = gender

        if strength == None :
            self._strength = random.randint(0,9)

    def get_gender(self) :
            return self._gender

    def get_strength(self) :
            return self._strength

class Fish (Animal) :
    def __init__(self, gender=None, strength=None):
        super().__init__(gender,strength)

class Bear(Animal) :
    def __init__(self, gender=None, strength=None):
        super().__init__(gender,strength)

class River :
    def __init__(self, length):
        self._length = length
        self._consists = []
        animal_types = (Bear, Fish)
        for i in range(self._length):
            objects = random.randint(0,len(animal_types))
            if objects == 1:
                self._consists.append(Bear())
            elif objects == 2 :
                self._consists.append(Fish())
            else:
                self._consists.append(None)

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        '''retrieve kth item in self._consists'''
        return self._consists[k]

    def __setitem__(self, k, value):
        '''setting the value of the kth item in the list'''
        self._contents[k] = value

    def count_none(self):
        '''count the number of empty cells in the list'''
        return self._consists.count(None)
    def add_random(self, animal):
        if self.count_none() > 0:
            choices = [i for i,x in enumerate(self._consists) if x == None]
            index = random.choice(choices)
            self._consists[index] = animal
    def update_cell(self, i):
        if self._consists[i] != None :
            move = random.randint(-1,1)
            if move != 0 and 0 <= i + move < self._length :
                if self._consists[(i + move)] == None :
                    self._consists[(i + move)] = self._consists[i]
                    self._consists[i] = None
                elif type(self._consists[i]) == type(self._consists[(i + move)]):
                    if self._consists[i].get_gender() != self._consists[(i + move)].get_gender():
                        '''same type, different gender'''
                        if type(self._consists[i]) == Bear:
                            self.add_random(Bear())
                        else:
                            self.add_random(Fish())
                    else:
                        '''same type, same gender'''
                        if self._consists[i].get_strength() > self._consists[(i + move)].get_strength() :
                            self._consists[(i + move)] = self._consists[i]
                        self._consists[i] = None
                else:
                    if type(self._consists[i]) == Bear :
                        self._consists[(i + move)] = self._consists[i]
                    self._consists[i] = None

    def update_river(self):
        '''Update every single cell in the river list'''
        for i in range(len(self._consists)) :
            self.update_cell(i)

    def print_river(self):
        s = '|'
        for x in self._consists :
            if x :
                if type(x) == Bear :
                    s += 'B'
                elif type(x) == Fish :
                    s += 'F'
                s += str(x.get_strength())
                s += x.get_gender()
            else:
                s +=' '
            s += '|'
        print(s)


if __name__ == '__main__' :
    river = River(10)
    for i in range(10) :
        print('Year', i)
        river.print_river()
        river.update_river()


