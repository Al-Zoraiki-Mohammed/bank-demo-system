""""""
from logic import *
from data import *


def show_main_screen(title='Main Menu Screen'):
    print("=="*30,f"\n\t{title}")
    print("=="*30)

    message ="""    [1] Show all clients.
    [2] Add a new  client.
    [3] Find a client.
    [4] Update a client.
    [5] Delete a client.
    [6] Transactions.
    [7] Manage Users.
    [8] Logout
"""
    print(message, end="")
    print('=='*30)
    
    return read_choice()


def authorized_user(user_name, password):
    for user in users:
        if (users.get(user).get('name') == user_name and 
           users.get(user).get('password') == password):
            return True
         
    return False


def user_login():
    print_screens_header('Login Screen')
    user_name = input('user name: ').strip()
    password = input('password: ').strip()
    
    while not authorized_user(user_name, password):
        print('Wrong user name or password :( ')
        user_name = input('user name: ').strip()
        password = input('password: ').strip()
            
    print('\nLogged in Successfully ..!\n')


if __name__ == "__main__":
    user_login()
    while True:
        choice = show_main_screen()
        if choice == '1':
            show_all_clients()
        elif choice == '2':
            add_new_client()
        elif choice == '3':
            find_client()
        elif choice == '4':
            update_client_data()
        elif choice == '5':
            delete_client()
        elif choice == '6':
            transactions()
        elif choice == '7':
            manage_users()
        elif choice == '8':
            logout()
            break
        
        input('Press Enter to back to main screen ...')
        print()
        
