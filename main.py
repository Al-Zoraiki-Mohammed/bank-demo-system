""""""
from logic import *


def show_main_screen(title='Main Menu Screen'):
    print("=="*30,f"\n\t{title}")
    print("=="*30)

    message ="""    [1] Show all clients.
    [2] Add a new  client.
    [3] Find a client.
    [4] Update a client.
    [5] Delete a client.
    [6] Transactions.
    [7] Exist.
"""
    print(message, end="")
    print('=='*30)
    
    return read_choice()
    

if __name__ == "__main__":
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
            exit()
            break
        
        input('Press Enter to back to main screen ...')
        print()
        


