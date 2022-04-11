#!/usr/bin/python3
""" export to csv file """

import csv
import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    userName = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(userId)).json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(userId)).json()

    with open(userId+'.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL)
        for todo in todos:
            csvwriter.writerow([userId, userName, str(todo.get('completed')),
                                todo.get('title')])
