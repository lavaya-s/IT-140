'''Text based adventure game'''
#IT-140 SNHU
#A
#import dependencies
import sys
from random import randint#random for dice rolls
import time#time import for scrolling
Game=True#this is for the while condition to run the game
lockpick=True
Villian_room=False#this becomes true if the player solves the puzzle//unlocking area Villian_room vilian room
Writing=False#boolean flag for locked rooms
Drawing=False
def Load():# made this to load game assets at the beggining but am considering eliomniting this function
    global rooms,current_room,inventory
    rooms = {#player input only takes first letter of direction
            'Entrance': {'N': 'Stalagmite'},#set all cardinal directions to single letters
            'Stalagmite': {'N': 'Hall', 'E': 'Skeletons','W':'Library','S':'Entrance'},
            'Skeletons': {'W': 'Stalagmite'},
            'Library':{'E':'Stalagmite'},
            'Hall':{'S':'Stalagmite','W':'Drawing','E':'Writing'},
            'Drawing':{'N':'Chest','E':'Hall'},
            'Writing':{'N':'Puzzle','W':'Hall'},
            'Chest':{'S':'Drawing'},
            'Puzzle':{'S':'Writing','E':'Villian'},
            'Villian':{'W':'Puzzle'}
            #I added the villian room for the scene function
        }
    current_room=rooms['Stalagmite']
    #set the current room by accessing nested dictionaries
    current_room=current_room['S']
    #create empty inventory
    inventory=[]#empty list for storing items
def text(string):#creates scrolling text for the game
    for i in string:#iterate over the print statement
        print(i, end='',flush=True)#Set flush to true so this runs , end='' eliminates default newline
        time.sleep(0.04)#Prints with a time delay so the text scrolls
def PlayerAction():#this function is the default screen for the game where the player chooses which function to go to next
    global Game
    text('What would you like to do?\n\t')#use tab and newline characters for formatting
    action=input('\t([i]- inspect, [m]-move, [g]-grab,[c]-check inventory, [e]exit game): ').title().strip()#uses title case and strips whitespace
    try:#this is if the player accidentaly presses enter
        if action[0] == 'I':#accesses only the first letter in title case in case of misspelled words. 
            Inspect()
        if action[0] == 'M':
            Move()
        if action[0] == 'G':
            Grab()
        if action[0] == 'C':
            Checkinventory()
        if action[0] == 'E':
            end()#runs the endgame function
        else:
            PlayerAction()#invalid options loop back
    except IndexError:
        PlayerAction()#if the player enters an empty string with no [0] index it loops back
def Inspect():#this is to help find hidden items
    global lockpick
    if current_room == 'Entrance':#check to see what room you are in
        text('\nYou poke around through the brush. \nAfter some time you realize your efforts are fruitless\n')
        text('There is nothing here\n')
        PlayerAction()
    if current_room == 'Stalagmite' and 'Star key' not in inventory:
        inventory.append('Star key')
        text('You look up through haze and notice a glimmer between the stalagmites on the cieling.\n ')
        text('Without missing a beat you jiggle your ebony wand, aptly named "Chaelu\'s Wand of the Frigid Grasp"\n')
        text('A bone chilling horror of icicle fingers swoop out of the wand and clammer to grasp the object through the mist.\n')
        text('as you put your hands down you see it is holding a very intricate and delicate looking ivory key.\n')
        text('the key has a star medallion on it\'s handle.\n')
        PlayerAction()
    if current_room == 'Skeletons' and 'Flask of oil' not in inventory:
        inventory.append('Flask of oil')
        text('You pour your eyes over the bodies of the dead, each one looking contemptable and dirty.\n')
        text('between the pile of bones an object catches your eye. "Is this a flask?" you wonder.\n')
        text('You open it to see it is filled with a type of oil.\n')
        PlayerAction()
    if current_room == 'Library' and 'Spell scroll' in inventory and 'Doll' not in inventory:
        text('After reading the spell scroll you notice a doll on the shelf next to were you dropped the glass\n')
        inventory.append('Doll')
        PlayerAction()
    if current_room == 'Puzzle' and 'Skull key' not in inventory:
        text('As you shuffle around to find your balance, you almost trip.\n')
        text('you kick the object out of your way to stablize yourself\n')
        PlayerAction()
    if current_room == 'Chest' and 'Golden statuette' not in inventory:
        if 'Lock pick' in inventory:
            text('You look closer at the chest.... It appears locked.\n You you shake it and slap it around')
            time.sleep(1)
            text('It is sealed shut...\n.... After a moment you have an idea....\n....Why not use the lock picking set')
            success=randint(1,21)
            if success > 15:
                text('\nAfter a good long while and some deep concentration you hear a little "click"....\n')
                text('You did it.... you succesfully opened the Treasure chest!!\n')
                text('Inside you find agolden statuette.\n')
                text('Upon further inspection you see that this statuette is of the Goddess of luck "Tymora"\n')
                inventory.append('Golden statuette')
                text('Commonly known as Lady Luck, Tymora shone upon those who took risks\n')
                text('and blessed those who dealt harshly with the followers of Beshaba.\n')
                text('As you observe the statuette you notice and inscryption on the bottom\n')
                text('from when Tymorans were struck with misfortune:\n')
                text('"Sometimes the Lady smiles, sometimes she laughs out loud."\n')
                PlayerAction()
            else:
                inventory.remove('Lock pick')#remove item from list so this doesn't run again
                lockpick = False# set lockpick to false so you  cant get it again
                text('\nAfter a good long while and some deep concentration you hear a little "click"....\n')
                text('You pull out the end of your lock pick.\n ')
                text('A tear falls down your face as you cry out, NOOO I BROKE MY ONLY LOCK PICK\n')
                text('How will you open the Treasure chest now?\n')
                Inspect()#go back and ignore to lock pick if clause
        elif 'Skull key' in inventory:
            text('You look closely at the treasure chest and see that it is engraved with a skull shaped lock\n')
            text('You pull the skull key out of your satchel and carefully insert it into the lock\n')
            text('You did it.... you succesfully opened the Treasure chest!!\n')
            text('Inside you find a golden statuette.\n')
            text('Upon further inspection you see that this statuette is of the Goddess of luck "Tymora"\n')
            inventory.append('Golden statuette')
            text('Commonly known as Lady Luck, Tymora shone upon those who took risks\n')
            text('and blessed those who dealt harshly with the followers of Beshaba.\n')
            text('As you observe the statuette you notice and inscryption on the bottom\n')
            text('from when Tymorans were struck with misfortune:\n')
            text('"Sometimes the Lady smiles, sometimes she laughs out loud."\n')
            PlayerAction()
        else:
            text('You look closely at the treasure chest and see that it is engraved with a skull shaped lock\n')
            PlayerAction()
    if current_room == 'Drawing' and 'Moon key' not in inventory:
        text('You push your hands through the rubble, pouring over every crevace.\n')
        text('amongst the rubble, buried in the dirt you uncover a key with a crescent moon on it.\n')
        inventory.append('Moon key')
        PlayerAction()
    else:
        text('You have already inspected this area\n')
        PlayerAction()
def intro():#I made this to have an introductuion seperate from the main game with variable that can still be accessed
    global name, character_name#variables to access later
    name=input('please type your name: ')
    text('Hello ')
    text(name)
    print()
    time.sleep(1)#the time sleeps are in here for dramatic effect.
    character_name=input('please type character name: ')
    time.sleep(1)
    text(' hello ')
    text(character_name)#text function only allows one argument at a time
    text(' welcome to the dungeon of Mephistopheles!!!.\n')
    text(character_name)
    text(' is a wizard from neverwinter who is  researching magical events in the sword coast of Fearun.\n')
    text('through your research you find out that There is a magical portal located in the marsh between\n')
    text('the Cloakwood, and Baldur\'s gate with the legendary demon, Mephistopheles about to break through\n')
    text('from the nine hells, Will you be able to collect all the of the items required to recite the magical\n')
    text('incantation and perform the ritual to close the portal? \n')
    text('Or will the demon lord on the other side be your demise?\n')
    time.sleep(1)
    text('As you make your way through the land you stumble upon the cave entrance for which you seek\n')
    text('The entrance to this mystical cavern is a crooked, rough, oblate opening,\n')
    text('with brush overgrowth from the dismal swamp leading up to it.\n ')
    time.sleep(1)
def Scene():#sets the scene for each room
    global Drawing, Writing
    if current_room == 'Entrance':#check to see what room[0] the player is in
        text('You see the same dismal swamp you previously trekked through.\n')
        text('The brush off to the side of the cavern')
        text('nothing new or interesting catches your eyes')
        #no call to anything else, this should go back to player action after it resolves
    if current_room == 'Stalagmite':
        text('In this next area you see dimly glowing stalagmite,\n')
        text('glittering from some mystical aura that sends shivers down your spine.\n')
        text('you see puddles of brown slush, and polka dotted mushrooms, about three inches average,\n')
        text('growing on the edges of the puddles.\n')
        text('This intersection of caverns has a misty haze running throughout.\n')
        text('3 jagged corridors cracked into the rock in front of you, you consult your trusty compass,\n')
        text('they go in the cardinal directions, East, North, and West.\n')
        text('There is a glimmer of something on the ceiling above.\n South is the direction you came from.\n')
    if current_room == 'Skeletons':
        text('In this cramped, dusty space you see skeletons of old warriors.\n')
        text('dusty bones and dilapidated shields.\n')
        text('The air in this room has a sense of dread and despair.\n')
        if 'Lock pick' not in inventory and lockpick == True:
            text('You notice a small satchel that one of the skeletons is clutching\n')
    if current_room == 'Library':
        text('As you enter this room you see it is the ruins of an old library,\n')
        text('carved into the cavern eons ago. shelving is rotten and the books are all crumbled.\n')
        if 'Spell scroll' not in inventory:
            text('You see a peice of paper encased in glass with a cork on the top.\n')
    if current_room == 'Hall':
        text('This long corridor grows dark and unsettling opening up after a while,\n')
        text('before forking into two doorways. both doors are closed and made of stone.\n')
        text('one to the west, with the shape of a star emblazoned in ethereal mist,\n')
        text('and one to the east with a crescent moon on it.\n')
        if Drawing == False and Writing == False:
            text('It appears as though you need a special key to open each.\n')
        if Drawing == False and 'Star key' in inventory:
            text('The door to the West creaks open slowly as you watch in amazment\n')
            #dont remove from inventory// this way the boolean flags don't cause scenes to repeat
            Drawing=True
        if Writing == False and 'Moon key' in inventory:
            text('The door to the East creaks open slowly while you watch in amazment\n')
            #dont remove from inventory
            Writing=True
    if current_room == 'Drawing':#add descriptions for puzzle
        text('You enter a mostly empty room. rubble is scattered amongst dirt and dust. \n')
        text('There is what looks to be a map of a city by the Triboar trail and the surrounding area.\n')
        text('It details the river Surbrin, the westernmost area of Neverwinter wood,\n')
        text('and the bustling city of Longsaddle.\n')
        text('you look over and see you can either go back or move toward a dead end to the north\n')
        text('You can see that room is empty as well,\n')
        text('all except for a glorious and decorated looking treasure chest\n')
    if current_room == 'Writing':#add descriptions for puzzle
        text('You enter this room and notice dust and rubble across the floor. \n')
        text('Nothing special looking here except for etchings on the walls written in an ancient language\n')
        text('An opening in the cave to the north.\n')
        memory=0
        memory=randint(1,21)
        if memory >= 11:
            text('You recall Some scripts you picked up on your last visit to candelkeep.\n')
            text('You remember enough of the symbols to decipher the etchings on each wall.\n')
            text('"What has cities \tbut no houses \nforests \tbut no trees \nrivers \tbut no water?"\n')
            text('curious, almost reads like a riddle\n')
    if current_room == 'Chest':
        text('You see the chest up close\nIt looks almost delicate.\nThere is nothing else interesting here.\n')
    if current_room == 'Puzzle':
        text('You find that this room feels eerie and strange,\n\tsomething bright fills your entire vision\n')
        text('A solid mildly translucent door is set to the east of this hazy and disorienting room.\n')
        if Villian_room == False:
            text('from the burst of light appears an extremely tall (about ten and a half feet) human woman,\n')
            text('well-muscled and physically fit. Their features are aristocratic,\n')
            text('Their skin tone shifting from pale blue to a more dark tan characteristic of Zakharans.\n')
            text('Their eyes are blue. Garments that are shimmering silk,\n')
            text('designed for comfort and to flaunt her muscular physiques.\n')
            text('She speaks with a burst, violently shaking the already unstable ground on which you stand.\n')
            text('"Speak the magic 3 letter word!"\n')
            Solve()
    if current_room == 'Villian':
        text('As you enter this room you are filled with dread.\n')
        text('A featureless black sphere of nothingness sits in middle of this cavernous ruin\n')
        text('It appears to destroy everything in its wake, warping the very fabric of reality as it pulsates.\n')
        text('Mephistopheles struts out of the feirce ball of nothingness,\n')
        text('playing up his infernal image as much as possible,\n')
        text('intentionally appearing as the classic archetype of a diabolical devil.\n')
        text('He stands 9ft tall.\nstriking a self confident pose\n')
        text('A charming, yet unnerving smile of self-superiority contrasted by his more monstrous features.\n')
        text('His fiendish claws, bright, crimson red skin, large,\n')
        text('bat-like wings and impressive, curling ram horns all left his hellish heritage on proud display.\n')
        text('Another source of contrast was his dead-white eyes against his long, straight, black hair,\n')
        text('as well as his dramatic, flowing cape as dark as the portal he stepped through\n')
        if  'Mushroom' and 'Flask of oil' and 'Golden statuette' and 'Doll' and 'Spell scroll' in inventory:
            text('You raise your wand and throw down the materials!\n')
            text('chanting the magical script on your scroll.\n\t"GO...AWAY...EVIL...DEMON!"')
            text('His skin changed to a  blue-black hue across his heavily muscled body;\n')
            text('wings, horns, and claws a deep shade of blue, scales of sooty black,\n')
            text('and eyes morphed to a pale blue except for the red irises and pupils.\n')
            text('he drops to the ground with a thud as the protal closes behind him\n')
            text('You defeated the demon\n')
            time.sleep(1)
            end()
        else:
            text('He strikes you down as swiftly as possible.\n')
            text('you have been defeated')
            end()
def Grab():#This is to grab items
    if current_room == 'Stalagmite' and 'Mushroom' not in inventory:#moved to check both instead of nested if statements
        inventory.append('Mushroom')
        text('You slosh around in the mud puddles, careful not to dirty your robe of Eyes.\n')
        text('Gifted to you by Janussi, The keeper of tomes at the massive citadel of Candlekeep.\n')
        text('Situated atop a rocky crag overlooking the Sea of Swords, \n')
        text('Candlekeep is Fearuns largest repository of written lore.\n')
        text('You think to yourself\n ')
        text('"I should head back there sometime and see if they have any new information for me"\n')
        text('You observe the polka dotted mushrooms closely. they remind you of the entrance to Gnomengarde\n')
        text('southeast of the mining town of phandlalin.\n')
        text('"These are harmless" you utter as you grab one and stuff it in your satchel\n')
        PlayerAction()
    if current_room == 'Library' and 'Spell scroll' not in inventory:
        text('You reach out and grab the bottle.\n')
        print('OOPS!')
        text('The bottle slips out of your hands and smashes down on the floor.\n')
        text('You bend down and pick up the paper. it reads: "Spell Of Portal Closing!"\n')
        text('Ingredients needed to cast this spell.\n\t1 Mushroom \n\t1 Flask of oil \n')
        text('\tThe golden statue of Tymora\n\t1 voodoo doll\n\t and this very spell scroll\n\t\n')
        inventory.append('Spell scroll')
        PlayerAction()
    if current_room == 'Chest' and 'Golden statuette' not in inventory:
        text('You try to pry open the treasure chest but all your efforts are futile!\n')
        PlayerAction()
    if current_room == 'Skeletons' and 'Lock pick' not in inventory and lockpick == True:
        text('You look closer at the satchel held by one of the skeletons\n')
        text('You open it to find an old, yet somehow intact, lock picking set\n')
        inventory.append('Lock pick')
        PlayerAction()
    if current_room == 'Puzzle' and 'Skull key' not in inventory:
        text('you bend over and grab the object you nearly tripped over.\n')
        inventory.append('Skull key')
    else:
        text('There is nothing here to grab\n')
        PlayerAction()
def Checkinventory():#this is a prompt for checking inventory
    text(character_name)
    text(' rummages through their pockets and trusty satchel and finds\n ')
    print(inventory)
    print()
    PlayerAction()
def Solve():#this is only accessed from the puzzle room
    global Villian_room#need the boolean value to unlock the next room
    if Villian_room == False:
        text(character_name)
        text(' Do you have the intelligence to solve this great mystery!!!\n')
        solution=input('Please type the magic word: ').lower().strip()
        if solution == 'map':
            Villian_room=True
            text('The blue door vanishes in a flash of intesnity!\n')
        else:
            text('She growls "WRONG" and the mist slowly swirls around\nSealing the door shut still\n')
            PlayerAction()
    PlayerAction()
def Move():
    global current_room
    print(f'You are in {current_room}')
    print('\nCommands: [n]-north [e]-east [s]-south [w]-west\n')
    room=input('\tPlease enter a command:').title()#this will set title case
    if current_room == 'Entrance' and room[0] in rooms['Entrance']:#check room[0] and available options
        current_room=rooms['Entrance'][room[0]]#only access the first element of the dict/input
        Scene()#set the scene before going back to player ation so it triggers only when you move
        PlayerAction()
    if current_room =='Stalagmite' and room[0] in rooms['Stalagmite']:
        current_room=rooms['Stalagmite'][room[0]]
        Scene()
        PlayerAction()
    if current_room =='Skeletons' and room[0] in rooms['Skeletons']:
        current_room=rooms['Skeletons'][room[0]]
        Scene()
        PlayerAction()
    if current_room =='Library' and room[0] in rooms['Library']:
        current_room=rooms['Library'][room[0]]
        Scene()
        PlayerAction()
    if current_room =='Hall' and room[0] =='S':
        current_room='Stalagmite'
        Scene()
        PlayerAction()
    if current_room =='Hall' and room[0] == 'W' and Drawing == True:
        current_room='Drawing'
        Scene()
        PlayerAction()
    if current_room == 'Hall' and room[0] == 'E' and Writing == True:
        current_room='Writing'
        Scene()
        PlayerAction()
    if current_room =='Drawing' and room[0] in rooms['Drawing']:
        current_room=rooms['Drawing'][room[0]]
        Scene()
        PlayerAction()
    if current_room =='Writing' and room[0] in rooms['Writing']:
        current_room=rooms['Writing'][room[0]]
        Scene()
        PlayerAction()
    if current_room =='Chest' and room[0] in rooms['Chest']:
        current_room=rooms['Chest'][room[0]]
        Scene()
        PlayerAction()
    if current_room =='Puzzle' and room[0] == 'S':
        current_room = 'Writing'
        Scene()
        PlayerAction()
    if current_room =='Puzzle' and room[0] == 'E' and Villian_room == True:
        current_room = 'Villian'
        Scene()
    if current_room =='Villian' and room[0] in rooms['Villian']:
        current_room=rooms['Villian'][room[0]]
        Scene()
        PlayerAction()
    else:
        print('Please enter a valid Command!')#this is for all other commands
        Move()#loops back to input
def Main():#main game loop after intro
    if Game == True:#if this gets set to false the loop ends
        PlayerAction()
def end():
    global Game
    text('Goodbye')#this executes only after the main playeractionloop stops
    print()
    text('Thanks for playing! ')
    text(name)
    sys.exit()
while Game == True:
    Load()#load global assets
    intro()#introduction to the game
    Main()#main game loop with exit condition
