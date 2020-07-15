# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, name, current_room = 'outside'):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        output = f'Hi {self.name} you are {self.current_room}'
        return output












        