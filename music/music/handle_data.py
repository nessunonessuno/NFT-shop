import subprocess
import os
import json


def upload_file_ipfs(file):
    with open(f'/home/poliziacantonale/{file.name}', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
    DEVNULL = open(os.devnull, "wb")
    upload = f'/home/poliziacantonale/{file.name}'
    response = subprocess.check_output(f'ipfs add {upload}', shell=True, stderr=DEVNULL, stdin=DEVNULL)
    os.system(f"rm {upload}")
    return response.split()[1].decode()

def mint_with_metadata(data, filelink):
    # Create a JSON Object
    json_obj = {}
    json_obj['name'] = data['name']
    json_obj['desctiption'] = data['description']
    json_obj['image'] = f'http://127.0.0.1:8080/ipfs/{filelink}'

    # Write the object to file.
    with open('/home/poliziacantonale/example.json', 'w') as jsonFile:
        json.dump(json_obj, jsonFile)

