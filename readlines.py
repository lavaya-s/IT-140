#Write a program that first reads in the name of an input file 
file=open('file1.txt','r')
file.close()
#then reads the input file using the file.readlines() method
lines=file.readlines()
#Your program should put the contents of the input file into a dictionary where the number of seasons are the keys
seasons = {}
count=0
temp_list=[]
for line in lines:
    if line in lines[:count]:
        line+=';'
        print(f'{line}')
        temp_line+=line
        pass
    elif count %2==0:
        temp_line=line
        temp_list.append(temp_line[:-1]) if temp_line not in temp_list else None
        print(f'{temp_list}')
#and a list of TV shows are the values (since multiple shows could have the same number of seasons)
    elif count %2!=0:
        seasons.update({temp_line[:-1]:line}) if line not in seasons else temp_line.append(line)
    count+=1
    print(f'{seasons}')
#Sort the dictionary by key (least to greatest) 
titles=''
keys=''
temp_list=sorted(temp_list)

#output the results to a file named output_keys.txt
file=open('output_keys.txt','w')
count2=[0 for item in temp_line]
count=0
for num in count2:
    count-=1
for line in sorted(seasons):
    keys+=str(temp_list[count])
    keys+=': '
    count+=1
    keys+=str(seasons[line])
    print(f'{keys}')
file.write(keys)
file.close()
#separating multiple TV shows associated with the same key with a semicolon (;)
#Next, sort the dictionary by values (alphabetical order)
file=open('output_titles.txt','w')
for line in sorted(seasons.values()):
    titles+=str((line))
    print(f'{titles}')
file.write(titles)
file.close()
#output the results to a file named output_titles.txt