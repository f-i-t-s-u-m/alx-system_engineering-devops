#!/usr/bin/python3
""" Gather data from an api """


if __name__ == "__main__":
    import requests
    from sys import argv

    tasks = []
    done_task = 0
    all_tasks = 0

    em = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    if len(em.json()) != 0:
        r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
        for i in r.json():
            if i['completed'] is True:
                tasks.append(i['title'])
                done_task += 1

            all_tasks += 1

        print('Employee {} is done with tasks({}/{})'
              .format(em.json()['name'], done_task, all_tasks))
        for i in tasks:
            print('\t '+i)
