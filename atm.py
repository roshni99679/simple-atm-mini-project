import time     #for stoppping program execution for some time

print('please insert your card')

time.sleep(5)       #for card processing

accountholdername = 'roohi sharma'

balance=34550
password=4567

name=input('please enter your name')
pin=int(input('please enter your atm pin'))


if pin==password:

    while True:
        print('*****Welcome to BANK OF MUMBAI*****')
        print('hello',accountholdername)
        print("press 1 to check balance ")
        print("press 2 to withdraw ")
        print("press 3 to deposit")
        print("press 4 to transfer money ")
        print("press 5 to change pin ")
        print("press 6 to exit ")

        try:
            option=int(input('please enter your choice '))
        except:
            print('please enter the correct choice')

    
        if option==1:
            print('your current balance is' , balance)

        if option==2:
            withdrawl=int(input('please enter the amount you want to withdraw'))
            balance=balance-withdrawl
            print('amount debited is' , withdrawl)
            print('your updated balance is' , balance)

        if option==3:
            deposit=int(input('please enter the amount you want to deposit'))
            balance=balance+deposit
            print('amount credited to your account is ' , deposit)
            print('your updated balance is' , balance)

        if option==4:
            rec=int(input("enter the account number of the receiver"))
            
            if rec==1234567899:
                cash=int(input("enter the amount you wish to transfer"))
                print(cash," rupees successfully transferred")
            else:
                print('Entered account number not found')
        
        if option==5:
            old=int(input("enter the old passcode here"))
            if old==password:
                new=int(input('enter new passcode you wish to set'))
                print('your passcode has been succesfully changed')
            else:
                print('passcode you entered is incorrect')


        if option==6:
            break

else:
    print('oops!! wrong pin')





    
