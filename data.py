""""""
import json

file_path = 'clients.json'

def load_data(file_path = 'clients.json'):
    with open(file_path, 'r') as file:
        clients = json.load(file)
    return clients
    
def write_data(clients):
    with open(file_path, 'w') as file:
        json.dump(clients, file, indent=4)
