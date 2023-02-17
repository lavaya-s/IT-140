import csv
csvfile=csv.reader(open(input(),'r'))#take input for the file name and open using csvreader
frequency={}#create an empty dictionary
for word in csvfile:#iterate twice to go from rows to columns
    for k,v in enumerate(word):#create a dict for the words
        frequency.update({k:v})#update the dict for the words
words = []#create an empty list
line = [word for word in frequency.values()]#make a list for each word in the file
for word in line:#iterate over the words in the file
     if word not in words:#conditional to see if the word exists in the list
         print(word, line.count(word))#cal the wordd count to count words
         words.append(word)#ad o the list to skip it next