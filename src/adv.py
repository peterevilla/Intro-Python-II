from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = str(input('Enter your name\n'))
player = Player(player_name)

print(player)
print(room[player.current_room])
print('Select your next move')
user = str(input("[n] North  [s] South   [e] East    [w] West  [q] Quit\n"))

while not user == 'q':
    #OUTSIDE
    current_room = player.current_room
    if(player.current_room == 'outside'):
        if(user == 'n'):
            print(f'*******************************************\nYou are now in the room {room[player.current_room].player_direction(user).name}\n {room[player.current_room].player_direction(user)} ')
            player.current_room = 'foyer'
        else:
            print('Error: Move not allowed')
    #FOYER
    elif(player.current_room == 'foyer'):
        if(user == 'n'):
             print(f'*******************************************\nYou are now in the room {room[player.current_room].player_direction(user).name}\n {room[player.current_room].player_direction(user)} ')
             player.current_room = 'overlook'
        elif(user == 's'):
             print(f'*******************************************\nYou are now in the room {room[player.current_room].player_direction(user).name}\n {room[player.current_room].player_direction(user)} ')
             player.current_room = 'outside'        
        elif(user == 'e'):
            print(f'*******************************************\nYou are now in the room {room[player.current_room].player_direction(user).name}\n {room[player.current_room].player_direction(user)} ')
            player.current_room = 'narrow'
        else:
            print('Error: Move not allowed')
    #OVERLOOK
    elif(player.current_room == 'overlook'):
        if(user == 's'):
            print(f'*******************************************\nYou are now in the room {room[player.current_room].player_direction(user).name}\n {room[player.current_room].player_direction(user)} ')
            player.current_room = 'foyer'
        else:
            print('Error: Move not allowed')
    #NARROW
    elif (player.current_room == 'narrow'):
        if(user == 'w'):
            print(f'*******************************************\nYou are now in the room {room[player.current_room].player_direction(user).name}\n {room[player.current_room].player_direction(user)} ')
            player.current_room = 'foyer'
        elif(user == 'n'):  
            print(f'*******************************************\nYou are now in the room {room[player.current_room].player_direction(user).name}\n {room[player.current_room].player_direction(user)} ')
            player.current_room = 'treasure'
        else:
            print('Error: Move not allowed')
    #TREASURE
    elif (player.current_room == 'treasure'):
        if(user == 's'):
            print(f'*******************************************\nYou are now in the room {room[player.current_room].player_direction(user).name}\n {room[player.current_room].player_direction(user)} ')
            player.current_room = 'narrow'
        else:
            print('Error: Move not allowed')

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
