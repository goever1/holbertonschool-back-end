#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    EMPLOYEE_NAME = ''
    NUMBER_OF_DONE_TASKS = ''
    TOTAL_NUMBER_OF_TASKS = ''

    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        EMPLOYEE_NAME = json_data.get('name')

    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        TOTAL_NUMBER_OF_TASKS = len(json_data)
        complete_tasks = [x for x in json_data if x.get('completed')]
        NUMBER_OF_DONE_TASKS = len(complete_tasks)

    print(f'Employee {EMPLOYEE_NAME} is done with tasks\
({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    [print('\t' + x.get('title')) for x in complete_tasks]