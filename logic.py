""""""
from data import *


def read_choice(length=8):
    choices = [str(i) for i in range(1,length +1)]

    choice = input(f'Type your choice from 1 to {length}: ').strip()
    while choice not in choices:
        choice = input(f'Type valid choice from 1 to {length}: ').strip()
        
    return choice


def print_header(header, num_rows, **Kwargs):
    print()
    print(f'\t\t\t{header}: {num_rows} rows')
    print('--'*30)
    print(f"| {Kwargs.get('k0')}.\t| {Kwargs.get('k1')} | {Kwargs.get('k2')}\t\t| {Kwargs.get('k3')} ")
    print('--'*30)


def show_all_data(data):
    for key, value in data.items():
        inner_ks = list(value.keys())
        print(f"| {key}\t\t| {value.get(inner_ks[0])}\t   | {value.get(inner_ks[1])}\t\t| {value.get(inner_ks[2])} ")


def show_clients():
    print_header('Clients List',len(clients), k0='Acount NO', k1='PIN Code', k2='Name', k3='Balance')
    show_all_data(clients)


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


def is_key_exist(key, data):
    return key in data.keys()


def find_client(title='Find Client Screen'):
    print_screens_header(title)
    account_no = input('Type account number: ')
    if  is_key_exist(account_no, clients):
        print_client_info(account_no)
    else:
        print(f'Account Number: {account_no} not found :(  ')
    
    return account_no



def insert_client(account_no):
    pincode = input('Type PIN Code: ')
    name = input('Type account name: ')
    balance = input('Type balance: ')

    clients[account_no] = {'Pincode':pincode, 'Name':name,'Balance': balance}
    write_data(clients, clients_file)


def add_new_client():
    print_screens_header('Add New Client Screen')
    add_more = True
    while add_more == True:

        account_no = input('Type account no: ')
        while is_key_exist(account_no, clients):
            account_no = input(f'Account no: [{account_no}] already exists. Type new: ')
        
        insert_client(account_no)
        print('client Added Successfully !')

        add_more = 'y' == input('Would you like to add more? y/n: ').strip().lower()


def update_client():
    account_no = find_client('Update Client Screen')

    is_confirmed = 'y' == input('Are you sure you wanna update this account? y/n: ')
    if is_confirmed:
        insert_client(account_no)
        print('Updated Successfully !!')


def delete_row(key, data, file):
    if is_key_exist(key, data):
        is_confirmed = 'y' == input('Are you sure you wanna delete this data? y/n: ')
        if is_confirmed:
            data.pop(key)
            write_data(data, file)
            print(f'Row of no: {key} Deleted Successfully !!')


def delete_client():
    account_no = find_client('Delete Screen')
    delete_row(account_no, clients, clients_file)

    
def balance_inquery(account_no):
    if is_key_exist(account_no, clients):
        return clients[account_no].get('Balance')


def deposit():
    account_no = find_client('Deposit Screen')
    if is_key_exist(account_no, clients):
        amount = int(input('Enter amount to deposit(i.e: 100 ): ').strip())
        int_balance = int(balance_inquery(account_no)[:-1])
        clients[account_no]['Balance'] = f'{int_balance + amount}$'
        print('Deposited sucessfully ! ..')
        write_data(clients, clients_file)
        print(f'Updated balance is {balance_inquery(account_no)}')
        
    
def withdraw():
    account_no = find_client('Withdraw Screen')
    if is_key_exist(account_no, clients):
        amount = int(input('Enter amount to withdraw (i.e: 100 ): ').strip())
        int_balance = int(balance_inquery(account_no)[:-1])

        if int_balance >= amount: 
            clients[account_no]['Balance'] = f'{int_balance - amount}$'
            print(f'{amount} is withdrawn sucessfully ! ..')
            write_data(clients, clients_file)
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


def logout():
    print_screens_header('Logout Screen')
    print('\nGood bye !!  :) \n')


def show_users():
    print_header('Users List',len(users), k0=' User Id', k1='Username', k2='Password', k3='Permission')
    show_all_data(users)
    
    input('\nPress Enter to back to main screen ...')


def insert_permission():
    return 1

def insert_user(user_id):
    name = input('Type user name: ').strip()
    password = input('Type password: ').strip()
    permission = insert_permission()
    users[user_id] = {'name': name, 'password': password, 'permission': permission}
    write_data(users, users_file)


def add_user():
    print_screens_header('Add New User Screen')
    add_more = True
    while add_more == True:

        user_id = input('Type User id: ')
        while is_key_exist(user_id, users):
            user_id = input(f'User id: [{user_id}] already exists. Type a new one: ')
        
        insert_user(user_id)
        print('User Added Successfully !')

        add_more = 'y' == input('Would you like to add more? y/n: ').strip().lower()

def print_user_info(user_id):
    print()
    print('\tUser Details')
    print('--' * 30)

    print(f'User Id: {user_id}')
    for key, vlaue in users.get(user_id).items():
        print(f'{key}: {vlaue}')

    print('--' * 30)


def find_user( title = 'Find User Screen'):
    print_screens_header(title)
    user_id = input('Type User id: ').strip()
    
    if is_key_exist(user_id, users):
        print_user_info(user_id)
    else:
        print(f'User with user_id {user_id} is not found :( ')
    
    return user_id


def delete_user():
    user_id = find_user('Delete Screen')
    delete_row(user_id, users, users_file)




def update_user():
    user_id = find_user('Update User Screen')

    is_confirmed = 'y' == input('Are you sure you wanna update? y/n: ')
    if is_confirmed:
        insert_user(user_id)
        print('User Updated Successfully !!')

def manage_users():
    users_message ="""    [1] List Users.
    [2] Add New User.
    [3] Delete User.
    [4] Update User.
    [5] Find User.
    [6] Main Menue.
"""  
    while True:
        print_screens_header('Manage Users Screen')
        print(users_message)

        choice = read_choice(length=6)

        if choice == '1':
            show_users()
        elif choice == '2':
            add_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            update_user()
        elif choice == '5':
            find_user()
        elif choice == '6':
            break

