# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory


    def __str__(self):
        output = ""
        if len(self.inventory) < 1:
            output = f"Hello {self.name } You are in {self.current_room}  You have no Items"
        for p in self.inventory:
            output += "Hello" + self.name + ", You are in " + self.current_room + "\n" + str(p) + "\n" 
        return output












        