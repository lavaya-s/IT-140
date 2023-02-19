'''Movement Between Rooms'''
#IT-140
#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }
current_room=rooms['Bedroom']#this is how i grab the first dict
#set the current room by accessing nested dictionaries
current_room=current_room['North']#then access the next by assigning the directional value
while current_room != 'exit':#exit will exit the program
    print(f'You are in {current_room}')#this prints the current room
    print('Commands: north east south west exit ')#lets the player know what options to take
    room=input('Please enter a command:').title()#this allows for lowercase or capital
    if current_room == 'Great Hall' and room in rooms['Great Hall']:#checks for both current room and directions
        current_room=rooms['Great Hall'][room]#assigns the room 
    if current_room =='Bedroom' and room in rooms['Bedroom']:
        current_room=rooms['Bedroom'][room]
    if current_room =='Cellar' and room in rooms['Cellar']:
        current_room=rooms['Cellar'][room]
    if room == 'Exit':
        print('Goodbye!')
        current_room='exit'#this breaks the while condition
    else:
        print('Please enter a valid Command!')#loops back around after informing the player

