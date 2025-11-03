class Tree():
    def make_fruits(self):
        print("Ye Lo Fruits!")

class Mango_Tree(Tree):

    def __init__(self, name):
        self.name = name

    def make_fruits(self):
        print("ye lo Mango!")

    def __str__(self):
        return "Hello my name is " + self.name + " The Mango"

mango = Mango_Tree("campa")
mango1 = Mango_Tree("Rupam")

print(mango)
print(mango1)

