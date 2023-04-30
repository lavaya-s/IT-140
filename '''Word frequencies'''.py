'''Word frequencies'''
sentence=input('Please type as much as you would like.').split()#take input from the user and split into a list
for word in sentence:#iterate over the list
    num=len([1 for w in sentence if w == word]) #create a list of tallies on the condition that it is equal to the current element
                                                #then assign it's total length to the variable for frequency
    print(f'{word} {num}')#print each word and frequencuy of the word in the list