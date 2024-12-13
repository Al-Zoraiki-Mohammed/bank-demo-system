""""""
import json

clients_file = 'clients.json'
users_file = 'users.json'

def load_data(file_path=clients_file):
    with open(file_path, 'r') as file:
        clients = json.load(file)
    return clients
    
def write_data(data, file_path=clients_file):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
