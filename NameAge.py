'''simple program to calculate the year a user was born'''
from datetime import datetime
def NameAge():
#ask user for name
    user_name = input('What is your name? ')
    user_name.strip()#strip any whitespace entered by the user
#ask user for age
    user_age = int(input('How old are you? '))
#take down what year it is
#Use dot notation
#from the datetime module grab the current time and use that to grab the current year
    today = datetime.now()
    year = today.year
#calculate year the user was born using current year minus age
    year_born = year - user_age
    year_born = str(year_born).strip()#strip any whitespace entered by the user
    print(f'Hello {user_name}! You were born in {year_born}.')
loop='no' if input('Can I guess your age?').strip().lower() == ('no')else 0
while loop!='no':
    NameAge()