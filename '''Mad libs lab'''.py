'''Mad libs lab'''
noun = input()
num = input()
while noun != 'quit':#While loop that runs until the user enters quit

    
    #format to put user input into the string
    print(f'Eating {num} {noun} a day keeps the doctor away.')
    noun = input()#variable for user input
    num = input()
#I tried multiple versoins of this and they all failed the tests

#####################################################################

noun = input()
num = input()
while noun != 'quit':#While loop that runs until the user enters quit

    
    #format to put user input into the string
    print(f'Eating {num} {noun} a day keeps the doctor away.')
    try:
        noun = input()#variable for user input
        num = input()
    except EOFError:
        break
    
##############################################################

noun = input()
num = input()
while noun != 'quit':#While loop that runs until the user enters quit

    if noun != 'quit':
    #format to put user input into the string
        print(f'Eating {num} {noun} a day keeps the doctor away.')
    try:
        noun = input()#variable for user input
        num = input()
    except EOFError:
        break
    
###############################################################

noun = ''
def UserText():
        try:
            noun = input()#variable for user input
            num = input()
            if noun != 'quit':
                MadLib(num,noun)
        except EOFError:
            noun = 'quit'
            num = '0'
def MadLib(num,noun):
    #format to put user input into the string
    print(f'Eating {num} {noun} a day keeps the doctor away.')
    UserText()
UserText()

##################################################################

noun = ''
game = True
def UserText():
        try:
            noun = input()#variable for user input
            num = input()
        except EOFError:#this happens once the zybooks input completes
            game = False#this prevents the while loop from continuing
def MadLib(num,noun):
    #format to put user input into the string
    print(f'Eating {num} {noun} a day keeps the doctor away.')
while game == True:
    UserText()
#runs only once the while loop completes
MadLib()

####################################################################

words = {}#create dictionaries to hold the keys to inputs
numbers={}
game = True#bool flag for the while loop
count = 0#start counting iterations
def UserText():#functiion to take user input into dictionaries
    global game, num, noun, count, words, numbers#declare variables
    try:
        noun = input()#variable for user input
        num = input()
        words.update({count:noun})#put the values into the dictionaries 
        numbers.update({count:num})#count is the key for range in the for loop
        if 'quit' in words.values():#stops the while loop when the user enters quit
            game = False
    except EOFError:#this happens once the zybooks input completes
        game = False#this prevents the while loop from continuing
def MadLib(num,noun):#takes args for numbers and nouns
    #format to put user input into the string
    if noun != 'quit':#doesn't print the quit statement
        print(f'Eating {num} {noun} a day keeps the doctor away.')
while game == True:
    UserText()
    count += 1#count after so no index out of range error
#runs only once the while loop completes
for element in range(count):#this runs for each time the input was taken
    num = numbers[element]#uses the value from each key in order of count variable
    noun = words[element]
    MadLib(num, noun)#passes the arguments to the print function

################################################################################