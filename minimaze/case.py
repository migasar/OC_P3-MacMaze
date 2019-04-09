"""DOCSTRING"""


from dataclasses import dataclass


@dataclass(order=True)
class Case:
    x: int
    y: int
    #position : tuple
    path: bool
    landing: str = ""
    toping: str = ""
#    visual : str


"""
class Case:

    # Attributes of the class :
    path = ["True", "False"]
    landing = [None, "start", "goal"]
    toping = [None, "hero", "enemy", "item1", "item2", "item3"]


    def __init__(self, position, path, landing=None, toping=None):
        self.position = position
        self.path = path
        self.landing = landing
        self.toping = toping
    # Attributes :
    # position (main attribute) - fixed
    # path (boolean) - fixed
    # landing: only one from the list ["regular", "start", "goal"] - fixed
    # toping: None or only one from the 3 equipments and the 2 persons - not fixed

    # Magic Methods :
    # __repr__
    # __str__

    # Properties :

    @property
    def path(self):
        return self.path

    # Methods :
    # def remove_toping(self, top):
    # def test_collision():
    # def solve_collision():
        # if collide with equipment:
            # load remove_toping()
            # modify count in toolbox of the hero
        # if collide with enemy --> showdown
            # if toolbox is completed, hero wins
            #  --> "winner, winner, needle dinner"
            # if toolbox is not completed, hero loses
            #  --> "these violent delights have violent ends"
    pass
"""


""" 
# TEST
def main():
    pass

if __name__ == "__main__":
    main()
"""
