amount = 27

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#The variable above describes an amount of money measured in
#dollars. Imagine you want to select the bills (1-dollar bills,
#5-dollar bills, 10-dollar bills, etc.) that make up that
#amount of money. For example, 17 dollars is one $10, one $5,
#and two $1s.
#
#Write a program that will print out the bills needed to
#arrive at the amount shown above. Assume that we always want
#the maximum number of large bills: for example, for 17 dollars,
#we want one $10, one $5, and two $1s, not three $5s and two $1s.
#You may assume that the largest bill you have on hand is a
#$50-dollar bill.
#
#Your code should print the following (with the correct numbers
#based on the value of amount):
#
#Fifties: 0
#Twenties: 0
#Tens: 1
#Fives: 1
#Ones: 2


#Add your code here!
fifty = amount // 50

if (fifty > 0):
    print("Fifties:", int(amount // 50))
    amount *= (amount % 50 / amount)

twenty = (amount // 20)

if (twenty > 0):
    print("Twenties:", int(amount // 20))
    amount *= (amount % 20 / amount)
   
ten = (amount // 10)

if (ten > 0):
    print("Tens:", int(amount // 10))
    amount *= (amount % 10 / amount)

five = (amount // 5)

if (five > 0):
    print("Fives:", int(amount // 5))
    amount *= (amount % 5 / amount)

one = (amount // 1)

if (one > 1):
    print("Ones:", int(amount // 1))
      
    
          



""" moneyInput = 45
allBills = [50, 20, 10, 5, 1]
mapBills = {
    50: "Fifties",
    20: "Twenties",
    10: "Tens",
    5: "Fives",
    1: "Ones"
    }

result = {
    "Fifties": 0,
    "Twenties": 0,
    "Tens": 0,
    "Fives": 0,
    "Ones": 0
    }


def howmany(moneyInput,allBills):
    #list comprehension
    possibleBills = [bill for bill in allBills if bill <= moneyInput]

    maxBill = max(possibleBills)
    
    numberof = int(moneyInput/maxBill) # rounddown by moneyInput//maxBill
    leftover = moneyInput%maxBill
    
    result[mapBills[maxBill]] = numberof
    
    if leftover > 0:
        howmany(leftover, allBills)
    elif leftover == 0:
        pass
    else:
        pass

howmany(45,allBills)



for key,value in result.items():
    print(f'{key}: {value}')

"""
