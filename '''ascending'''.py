'''ascending'''
values = []#create empty list to store data
value = input().split()#take input from user
#iterate over user input to store into the empty list
for v in value:
    if v != ' ':#ignore spaces
        values.append(int(v))#add the values to the list      
def insertion_sort(array):
    for index in range(1,len(array)):
        value=array[index]
        while array[index-1]>value and index>=1:
            array[index]=array[index-1]
            index-=1
            array[index]=value
insertion_sort(values)
order=''#empty string
for num in values:#iterate over the new list
    if num >= 0:#only use positive numbers
        order += str(num) + ' '#add the numbers to the ordered list with spaces
print(order)