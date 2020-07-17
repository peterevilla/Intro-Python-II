from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# List of Items

knife = Item('knife', 'This is a weapon, use wisely')
drink = Item('drink', 'Recover your health')
TheMap = Item('map', 'Find the treasure')
shield = Item('shield', 'defend from enemies')






#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = str(input('Enter your name\n'))
player_room = room["outside"]
player = Player(player_name, player_room)
print('Select your next move')
user = str(input("[n] North  [s] South   [e] East    [w] West  [q] Quit\n"))

while not user == 'q':
    current_room = player_room
    if(user == 'n'):
        if hasattr(current_room, 'n_to'):
            print(current_room.n_to) 
            player_room = current_room.n_to
        else:
            print('movement not allowed')
    elif(user == 's'):
        if hasattr(current_room, 's_to'):
            print(current_room.s_to) 
            player_room = current_room.s_to
        else:
            print('movement not allowed')
    elif(user == 'e'):
        if hasattr(current_room, 'e_to'):
            print(current_room.e_to) 
            player_room = current_room.e_to
        else:
            print('movement not allowed')
    elif (user == 'w'):
        if hasattr(current_room, 'w_to'):
            print(current_room.w_to) 
            player_room = current_room.w_to
        else:
            print('movement not allowed')
    else:
        print('Error, please select a valid command')
    

    print('Select your next move\n*******************************************\n*******************************************')
    user = str(input("[n] North  [s] South   [e] East    [w] West  [q] Quit\n"))

print('Thanks for Play')








# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# 
# 
