####################################################################
words = {}#create dictionaries to hold the keys to inputs
numbers = {}#create empty dict for nums
game = True#bool flag for the while loop
count = 0#start counting iterations
def UserText():#functiion to take user input into dictionaries
    global game, num, noun, count, words, numbers#declare variables
    try:#catch End of file Errors
        noun = input()#variable for user input
        num = int(input())#take input for an integer
        words.update({count:noun})#put the values into the dictionaries 
        numbers.update({count:num})#count is the key for range in the for loop
        if 'quit' in words.values():#stops the while loop when the user enters quit
            game = False#set Boolean value to False
    except EOFError:#this happens once the zybooks input completes
        game = False#this prevents the while loop from continuing
def MadLib(num,noun):#takes args for numbers and nouns
    #format to put user input into the string
    if noun != 'quit':#doesn't print the quit statement
        print(f'Eating {num} {noun} a day keeps the doctor away.')
while game == True:#LOOPS while condition is true. game variable BOOL is effectively ON
    UserText()#call the user text function defined earlier
    count += 1#count after so no index out of range error
#runs only once the while loop completes
for element in range(count):#this runs for each time the input was taken
    num = numbers[element]#uses the value from each key in order of count variable
    noun = words[element]
    MadLib(num, noun)#passes the arguments to the print function
################################################################################