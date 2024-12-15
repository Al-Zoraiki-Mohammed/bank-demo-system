""" Needed to finish add users with permission. finish insert_aurhorization() functin.)"""
from logic import *
from data import *

code = {'show_all':'1', 'add_client': '2', 'find_client':'4',
                   'update_client':'8','delete_client':'16',
                   'transaction':'32','manage_users':'64'}

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


def get_permission(user_name, password):
    for user in users:
        if (users.get(user).get('name') == user_name and 
           users.get(user).get('password') == password):
            return True, users.get(user).get('permission')
         
    return False, 0


def user_login():
    print_screens_header('Login Screen')
    user_name = input('user name: ').strip()
    password = input('password: ').strip()
    
    is_authorized, permission = get_permission(user_name, password)
    while not is_authorized:
        print('Wrong user name or password :( ')
        user_name = input('user name: ').strip()
        password = input('password: ').strip()
        is_authorized, permission = get_permission(user_name, password)
            
    print('\nLogged in Successfully ..!\n')

    return permission


def is_permited(permission_scope, code):
    return int(permission_scope) & int(code) == int(code)


def print_no_enouph_permission():
    msg = """ Sorry, You don't have engough permission !!
    Please, contact your admin or simply logout :)
"""
    print(msg)


if __name__ == "__main__":
    permission_scope = user_login()
    while True:
        choice = show_main_screen()
        if choice == '1':
            if is_permited(permission_scope, code.get('show_all') ):
                show_clients()
            else: print_no_enouph_permission()

        elif choice == '2':
            if is_permited(permission_scope, code.get('add_client') ):
                add_new_client()
            else: print_no_enouph_permission()

        elif choice == '3':
            if is_permited(permission_scope, code.get('find_client') ):
                find_client()
            else: print_no_enouph_permission()
            
        elif choice == '4':
            if is_permited(permission_scope, code.get('update_client') ):
                update_client()
            else: print_no_enouph_permission()

        elif choice == '5':
            if is_permited(permission_scope, code.get('delete_client') ):
                delete_client()
            else: print_no_enouph_permission()

        elif choice == '6':
            if is_permited(permission_scope, code.get('transaction') ):
                transactions()
            else: print_no_enouph_permission()

        elif choice == '7':
            if is_permited(permission_scope, code.get('manage_users') ):
                manage_users()
            else: print_no_enouph_permission()

        elif choice == '8':
            logout()
            break
        
        input('\nPress Enter to back to main screen ...')
        print()
  
