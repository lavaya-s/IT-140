# 
#
#Uses singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.
coins = int(input())#make sure the input is a number
if coins <=0:#this checks if the user is broke or in debt
    print('No change')
if coins >= 100:#This only runs if there is a dollar or more
    dollar = coins//100#floor divide o ignore the remainder
    coins =coins%100#this sets the value of coins to the remainder after geting the dolar amount
    if dollar >1:#check to see if plural
        print(dollar,'Dollars')
    elif dollar ==1:#check to see if singular
        print(dollar,'Dollar')
if coins >=25:#same logic as the last block
    quarter = coins//25
    coins=coins%25
    if quarter >1:
        print(quarter,'Quarters')
    if quarter ==1:
        print(quarter,'Quarter')
if coins >=10:    
    dimes=coins//10
    coins=coins%10
    if dimes>1:
        print(dimes,'Dimes')
    if dimes==1:
        print(dimes,'Dime')
if coins >=5:   
    nickels=coins//5
    coins=coins%5
    if nickels>1:
        print(nickels,'Nickels')
    if nickels==1:
        print(nickels,'Nickel')
if coins !=0:#this checks to see if there are any coins left after taking out the other values
    if coins ==1:
        print(coins,'Penny')
    elif coins >1:
        print(coins,'Pennies')
#use a dict and iterate over it instead 
#cointainerizing is more effective than a ton of if statements. 