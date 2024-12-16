""""""
import json

code = {'show_all':'1', 'add_client': '2', 'find_client':'4',
                   'update_client':'8','delete_client':'16',
                   'transaction':'32','manage_users':'64'}

clients_file = 'clients.json'
users_file = 'users.json'


def load_data(file_path):
    with open(file_path, 'r') as file:
        clients = json.load(file)
    return clients


def write_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


clients = load_data(clients_file)
users = load_data(users_file)
