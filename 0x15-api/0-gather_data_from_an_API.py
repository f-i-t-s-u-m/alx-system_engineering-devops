#!/usr/bin/python3
""" Gather data from an api """

import requests
import sys

if __name__ == "__main__":

    tasks = []
    completed = 0
    totalTask = 0
    userId = sys.argv[1]

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    userName = user.json().get('name')

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(userId))
    for i in r.json():
        if i['completed'] is True:
            tasks.append(i['title'])
            completed += 1

        totalTask += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(userName, completed, totalTask))

    for i in tasks:
        print('\t '+i)
