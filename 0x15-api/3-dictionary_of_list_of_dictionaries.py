#!/usr/bin/python3
""" Gather data from an api """

import json
import requests

if __name__ == "__main__":

    data = dict()

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    for user in users:
        username = user.get('username')
        id = user.get('id')
        todos = requests.get("https://jsonplaceholder.typicode.com" +
                             "/users/{}/todos".format(id)).json()
        task = []
        for todo in todos:
            task.append({"task": todo.get('title'),
                         "completed": todo.get('completed'),
                         "username": user.get('username')})
        data[id] = task

    with open('todo_all_employees.json', 'w') as jfile:
        json.dump(data, jfile)
