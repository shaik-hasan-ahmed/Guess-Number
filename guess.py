import random
guess=random.randint(1,100)
no=int(input('Enter the value between 1 and 100:'))
result=True
count=0
while result:
    if(no==guess):
        print("The guessed Number is correct ")
        print("No of turns you have used are :",count)
        result=False
    elif no>guess:
        no=int(input("the value is greater than the number \nenter the value less than previous number"))
        count=count+1
        print("No of turns you have used are :",count)
    elif(no<guess):
        no=int(input("the value is less than the number \nenter the value greater than previous number"))
        count=count+1
        print("No of turns you have used are :",count)