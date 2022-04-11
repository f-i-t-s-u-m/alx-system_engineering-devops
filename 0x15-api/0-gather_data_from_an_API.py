#!/usr/bin/python3
""" Gather data from an api """

import json
import requests
from sys import argv

tasks = []
done_task = 0
all_tasks = 0


em = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
r = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos')
for i in r.json():
    if i['completed'] == True:
        tasks.append(i['title'])
        done_task += 1
    
    all_tasks += 1

print('Employee {} is done with tasks({}/{})'
        .format(em.json()['name'], done_task, all_tasks))
for i in tasks:
    print('\t '+i)

