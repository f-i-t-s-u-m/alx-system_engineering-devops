#!/usr/bin/python3
""" Gather data from an api """

import requests
from sys import argv

if __name__ == "__main__":

    tasks = []
    completed = 0
    totalTask = 0

    em = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    if len(em.json()) != 0:
        r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
        for i in r.json():
            if i['completed'] is True:
                tasks.append(i['title'])
                completed += 1

            totalTask += 1

        print('Employee {} is done with tasks({}/{}):'
              .format(em.json()['name'], completed, totalTask))

        for i in tasks:
            print('\t '+i)
