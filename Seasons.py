def Seasons():
    input_month = input('Please input the month').lower().strip()
    input_day = int(input('Please input the day'))
    months=['january','february', 'april', 'may', 'march', 'june', 'july', 'august', 'september', 'november', 'october', 'december']
    if input_month not in months or input_day >31  or input_day<=0:
        print('Invalid')
        input_month=0
        input_day=0
    if input_month == 'march':
        if input_day >=20 and input_day<31:
            print('Spring')
        if input_day <20 and input_day>0:
            print('Winter')
    if input_month == 'june':
        if input_day <= 20 and input_day>0:
            print('Spring')
        if input_day > 20 and input_day<31:
            print('Summer')
    if input_month == 'april' or input_month == 'may':
        print('Spring')
    if input_month == 'january' or input_month ==  'february':
        print('Winter')
    if input_month == 'july' or input_month == 'august':
        print('Summer')
    if input_month == 'october' or input_month ==  'november':
        print('Autumn')
    if input_month == 'september':
        if input_day <=21 and input_day>0:
            print('Summer')
        if input_day >=22 and input_day <31:
            print('Autumn')
        if input_day >=31:
            print('Invalid')
    if input_month == 'december':
        if input_day <=20 and input_day>0:
            print('Autumn')
        if input_day >=21 and input_day <31:
            print('Winter')  
Seasons()