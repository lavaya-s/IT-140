'''Replacing words'''
def replacing_words():#create a function to replace words in the sentence
    for replacement_word in new_dictionary:#iterate over the dictionary for replacements
        index_sentence=-1#set a count for indexing at -1 for accuracy
        for original_word in sentence:#iterate over the sentence to find words to replace
            index_sentence+=1#increase the indexing count
            if original_word == replacement_word:#contidion to check if the word should be replaced
                #assign the new word wioth the value in the dictionary at the index count
                sentence[index_sentence] = new_dictionary[replacement_word]
    return sentence#return the new sentence
replacement_words = input().split()#take input for words tobe replaced
#create dictionary to bind tthe split words from word to be replaced with the replacement words by iterating over them
new_dictionary = {replacement_words[replacement_word]:replacement_words[replacement_word+1] for replacement_word in range(0,len(replacement_words),2)}
sentence = input().split()#take input for the sentence
replacing_words()#call the function to replace words
for word in sentence:#iterate over the new sentence
    #print the new words in the sentence with spaces until the end of the sentence
    print(f'{word} ',end='') if word is not sentence[-1] else print(f'{word}')