
balance = 100000
deposit = 0
withdraw = 0
pin_counter = 0
pin_limit = 3
services = ['1.View bank balance',
            '2.Deposit money',
            '3.Withdraw money',
            '4.Quit bank service'
            ]

name = input("Enter your username please: ")
print(f"Welcome {name}")

while pin_counter < pin_limit:
    pin = input("Enter your pin please: ")
    pin_counter += 1
    if pin == '3036':
        print("--------Welcome to vin banking service--------")
        for service in services:
            print(f"{service}")
        print('**********************************************')
        bank_service = input("Enter bank service: ")
        if bank_service == '1':
                print(f"Your bank balance is {balance}")
        elif bank_service == '2':
                deposit = int(input("Enter amount to deposit: "))
                balance += deposit
                print(f"Your new bank balance is {balance}")
        elif bank_service == '3':
                withdraw = int(input("Enter amount to withdraw: "))
                if balance > withdraw:
                    balance -= withdraw
                    print(f"Your new bank balance is {balance}")
                else:
                    print("Insufficient funds")

    else:
        print("Wrong pin!")







