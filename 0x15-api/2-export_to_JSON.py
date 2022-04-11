#!/usr/bin/python3
""" Gather data from an api """

import json
import requests
import sys

if __name__ == "__main__":

    data = []
    completed = 0
    totalTask = 0
    userId = sys.argv[1]

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    userName = user.get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(userId)).json()

    for todo in todos:
        data.append({"task": todo.get('title'),
                     "completed": todo.get('completed'),
                     "username": user.get('username')})

    with open(userId+'.json', 'w') as jfile:
        json.dump({userId: data}, jfile)
