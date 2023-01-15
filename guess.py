
import random
num=random.randint(1,20)
#randint()function specifies an upper and lower random rangewithin its paranthesis
flag=True
#flag variable specifies an initial program conditionthat will allow the program to start
#examining the user's input
guess=0
print('Guess a number 1-20:',end='')
while flag==True:#the while keyword specifies a LOOP control structure that will repeat the statement it contains untila tested condition fails
    guess=input()
    if not guess.isdigit():#the if not guess.isdigit() test specifies an action to "break" the loop if the user input is not an integer whole number
        print('Invalid! Enter only digits 1-20!')
        break
    elif int(guess)<num:#the elif int(guess)<num test specifies an alternative action if the cast user input is lower than the stored random number
        print('Too low, Try again:',end='')
    elif int(guess)>num:#the elif int(guess)>num test specifies an alternative action if the cast user input is greater than the stored random number
        print('Too high, Try again:',end='')
    else:#the else keyword specifies a final alternative action to change the program condition, thereby ending the program
        print('Correct... My number is' + guess)
        flag=False