from abc import ABC, abstractmethod

class BoardGame(ABC):
    name = None

    def display(self):
        print(self.name)

    @abstractmethod
    def location(self):
        pass
    
class TableTopBoardGame(BoardGame):
    location = None
    
    def showLocation(self):
        print("Physical location of game: {}".format(self.location))


class ComputerSimulatedBoardGame(BoardGame):
    location = None
    
    def showLocation(self):
        print("URL of game: {}".format(self.location))
