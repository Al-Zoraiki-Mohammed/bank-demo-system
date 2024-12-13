""""""
from data import *

clients = load_data(clients_file)

def read_choice(length=7):
    choices = [str(i) for i in range(1,length +1)]

    choice = input(f'Type your choice from 1 to {length}: ').strip()
    while choice not in choices:
        choice = input(f'Type valid choice from 1 to {length}: ').strip()
        
    return choice


def print_clients_header():
    print()
    print(f'\t\t\tClients list: {len(clients)} clients')
    print('--'*30)
    print('| Acount NO.\t| PIN Code | Name\t\t| Balance ')
    print('--'*30)


def show_all_clients():
    print_clients_header()

    for key, value in clients.items():
        print(f"| {key}\t\t| {value.get('Pincode')}\t   | {value.get('Name')}\t\t| {value.get('Balance')} ")

def print_screens_header(screen_name):
    print()
    print('=='*30,'\n\t\t', f"{screen_name}",'\t\t')
    print('=='*30)


def print_client_info(account_no):
    print()
    print('\tClient Details')
    print('--' * 30)

    print(f'Account Number: {account_no}')
    for key, vlaue in clients.get(account_no).items():
        print(f'{key}: {vlaue}')

    print('--' * 30) 

def is_key_exist(account_no):
    return account_no in clients.keys()


def find_client(text='Find Client Screen'):
    print_screens_header(text)
    account_no = input('Type account number: ')
    if  is_key_exist(account_no):
        print_client_info(account_no)
    else:
        print(f'Account Number: {account_no} not found :(  ')
    
    return account_no



def insert_data(account_no):
    pincode = input('Type PIN Code: ')
    name = input('Type account name: ')
    balance = input('Type balance: ')

    clients[account_no] = {'Pincode':pincode, 'Name':name,'Balance': balance}
    write_data(clients)

def add_new_client():
    print_screens_header('Add New Client Screen')
    add_more = True
    while add_more == True:

        account_no = input('Type account no: ')
        while is_key_exist(account_no):
            account_no = input(f'Account no: [{account_no}] already exists. Type new: ')
        
        insert_data(account_no)
        print('client Added Successfully !')

        add_more = 'y' == input('Would you like to add more? y/n: ').strip().lower()


def update_client_data():
    account_no = find_client('Update Client Screen')

    is_confirmed = 'y' == input('Are you sure you wanna update this account? y/n: ')
    if is_confirmed:
        insert_data(account_no)
        print('Updated Successfully !!')


def delete_client():
    account_no = find_client('Delete Screen')

    if is_key_exist(account_no):
        is_confirmed = 'y' == input('Are you sure you wanna delete this account? y/n: ')
        if is_confirmed:
            clients.pop(account_no)
            write_data(clients)
            print('Deleted Successfully !!')


def balance_inquery(account_no):
    return clients[account_no].get('Balance')

def deposit():
    account_no = find_client('Deposit Screen')
    if is_key_exist(account_no):
        amount = int(input('Enter amount to deposit(i.e: 100 ): ').strip())
        int_balance = int(balance_inquery(account_no)[:-1])
        clients[account_no]['Balance'] = f'{int_balance + amount}$'
        print('Deposited sucessfully ! ..')
        write_data(clients)
        print(f'Updated balance is {balance_inquery(account_no)}')
        
    
def withdraw():
    account_no = find_client('Withdraw Screen')
    if is_key_exist(account_no):
        amount = int(input('Enter amount to withdraw (i.e: 100 ): ').strip())
        int_balance = int(balance_inquery(account_no)[:-1])

        if int_balance >= amount: 
            clients[account_no]['Balance'] = f'{int_balance - amount}$'
            print(f'{amount} is withdrawn sucessfully ! ..')
            write_data(clients)
            print(f'Updated balance is {balance_inquery(account_no)}')
        else:
            print(f'Insufficient amount, you can not withdraw more than {int_balance}$')


def transactions():
    trans_message ="""    [1] Deposit.
    [2] Withdraw.
    [3] Total Balance.
    [4] Main Menue.
"""
    while True:
        print_screens_header('Transactions Menue Screen')

        print(trans_message)

        choice = read_choice(length=4)
        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            print(f'Current balance: {balance_inquery(find_client("Balance Inquery"))}')
        elif choice == '4':
            break


def exit():
    print_screens_header('Exit Screen')
    print('Good bye !!  :) ')
    
