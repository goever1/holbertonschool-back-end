#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys
from sys import argv


if __name__ == "__main__":
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employe = int(sys.argv[1])
    response = requests.get(f'{BASE_URL}/todos?userId={employe}')
    todos = response.json()
    tasks_completed = [todo for todo in todos if todo['completed']]
    num_tasks_completed = len(tasks_completed)
    num_tasks = len(todos)
    user_response = requests.get(f'{BASE_URL}/users/{employe}')
    user_data = user_response.json()
    empoleye_name = user_data['name']
    print(f"Employee {empoleye_name} is donde with tasks \
           ({num_tasks_completed}/{num_tasks}): ")
    for todo in tasks_completed:
        print(f'\t {todo["title"]}')