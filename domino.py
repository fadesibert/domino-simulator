from random import sample


class Tile:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right

    def __repr__(self):
        return "[{}|{}]".format(self.left, self.right)

    def is_double(self):
        return self.left == self.right

class Table:
    pass

class Hand:
    def __init__(self):
        self.contents = set()

    def take_tile(self, tile):
        self.contents.add(tile)

    def play_tile(self, tile):
        self.contents.remove(tile)

    def __repr__(self):
        return str(self.contents)


class Boneyard:
    def __init__(self):
        self.contents = set()

    def add(self, tile):
        self.contents.add(tile)

    def pick(self):
        tile = sample(self.contents, 1)[0]
        self.contents.remove(tile)
        return tile

    def __str__(self):
        return "{} left in the 'yard".format(len(self.contents))

###
# Shuffle the Boneyard
###
boneyard = Boneyard()

for i in range(0,7):
    for j in range(0,7):
        if i <= j:
            boneyard.add(Tile(i, j))

print(boneyard)
###
# Draw tiles into each players hand
###

p1 = Hand()
p2 = Hand()

for _ in range(0, 8):
    p1.take_tile(boneyard.pick())
    p2.take_tile(boneyard.pick())

print(p1)
print(p2)

###
# Initialize the Table
###

###
# Play the hand
###
