#!/usr/bin/python3
""" export to csv file """

import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    userName = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(userId)).json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(userId)).json()

    with open(userId+'.csv', 'w') as csv:
        for todo in todos:
            print('"{}","{}","{}","{}"'
                  .format(userId, userName,
                          todo.get('completed'), todo.get('title')), file=csv)
