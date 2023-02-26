def ints(args):#define a function to accept any number of arguments
    global max_int,average#set the max_int and average variable to global so it can be accessed later
    max_int=0#set it to zero
    average=0#set the average to zero
    count=0#set the count to zero
    numbers = []#create empty list
    for arg in args:#iterate over the list
        numbers.append(arg)#append the argument to the end of the list
    for arg in numbers:#iterate over the list
        count+=1#increment the count for the floor division of average
        average += arg#add the numbers together
        if arg > max_int:#check to see if it is greater
         max_int=arg#assign the greatest value
    average//=(count)#divide by total arguments to get average after adding together
    return average,max_int#return the values
values = []#create empty list to store data
value = input().split(' ')#take input from user
#iterate over user input to store into the empty list
for v in value:#iterate over the list
    if v != ' ':#ignore spaces
        values.append(int(v))#add the values to the end of the list
#callthe function to add all arguments passed through
ints(values)#remember to unpck the list to create all the arguments
print(average,max_int)#print the results