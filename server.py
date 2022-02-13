import socket
import json
import sys

HOST = ''
PORT = 9876
ADD = (HOST, PORT)
BUFFER_SIZE = 1024
DATA_PATH = '/home/mry/Documents/irt/Info/Projet/dev/data'


def add_user(json_payload):

    try:

        # Get existing users
        with open(f'{DATA_PATH}/users.json', 'r') as f:
            json_data = json.load(f)

        # Create new user's own directory
        json_dir_init = {
            "contacts": []
        }
        json.dumps(json_dir_init)
        
        with open(f'{DATA_PATH}/dirs/{len(json_data["users"])+1}.json', 'w') as f:
            json.dump(json_dir_init, f, indent=2, sort_keys=True)

        # Add new user to the list
        json_data['users'].append(json_payload)

        with open(f'{DATA_PATH}/users.json', 'w') as f:
            json.dump(json_data, f, indent=2, sort_keys=True)

        return 'SUCCESS'

    except:
        return 'ERROR'


def add_contact(json_payload):

    try:

        # Get directory's existing contacts
        with open(f'{DATA_PATH}/dirs/{json_payload["dir_id"]}.json', 'r') as f:
            json_data = json.load(f)

        # Add new contact to the list
        json_data['contacts'].append(json_payload['contact'])

        with open(f'{DATA_PATH}/dirs/{json_payload["dir_id"]}.json', 'w') as f:
            json.dump(json_data, f, indent=2, sort_keys=True)

        return 'SUCCESS'

    except:
        return 'ERROR'

def search_contact(json_payload):

    try:
        results = []

        # Read each directory and search matching contact
        # function of provided filters
        for dir_id in json_payload['search_in_dirs']:

            with open(f'{DATA_PATH}/dirs/{dir_id}.json', 'r') as f:
                json_data = json.load(f)

                for contact in json_data['contacts']:
                    matching = True
                    for filter_obj in json_payload['filters']:
                        if contact[filter_obj['field_name']] != filter_obj['field_value']:
                            matching = False
                    if matching:
                        results.append(contact)

        return results

    except:
        return 'ERROR'


def start_server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'server listening on port {PORT}')
    serv.bind(ADD)
    serv.listen(5)

    while True:
        conn, add = serv.accept()
        print(' client connected ...', add)

        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break

            print('handling data ...')
            print(int.from_bytes(data, sys.byteorder))
            # ...

