import random
x = random.randrange(1,10)
i=0
while (i<=4):
    y = input('Guess the Number ')
    if (y == x):
        print('Hooray')
        break
    else:
        if (i<4):
            print('Try Again')
    i=i+1
if y != x: 
    print('The Answer is ' + str(x))  
