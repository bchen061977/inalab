import requests
import json
import hashlib
import os

# get data from the API
url = 'http://localhost:5000/data'
response = requests.get(url)
data = response.json()

# create a directory to store the files
directory = 'files'
os.makedirs(directory, exist_ok=True)

# extract samples array

samples = data["samples"]

# process each id in samples
for item in samples:
    id = item["id"]

    # create a file with the ID as the filename
    filename = f'{directory}/{id}.txt'
    with open(filename, 'w') as file:
        file.write(item["name"])

    # calculate the SHA256 sum 
    with open(filename, 'r') as file:
        file_contents = file.read()
        hash_object = hashlib.sha256(file_contents.encode())
        file_hash = hash_object.hexdigest()

    # compare the SHA256 sum with the id
    if file_hash == id:
        print(f'File {filename} has a matching SHA256 sum.')
    else:
        print(f'File {filename} does not have a matching SHA256 sum.')

