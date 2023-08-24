#!/usr/bin/python3
"""it returns infomration of a to do list of an employee"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)
        
    to_do: requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         sys.argv[1], timeout=5)
    name = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1], timeout=5)
    
    json_todo = to_do.json()
    json_names = name.json()

    all_tasks = 0
    comp_task = 0
    title = ""

    for item in json_todo:
        all_tasks += 1
        if item ['completed'] is True:
            comp_task += 1
            comp_task.appened(item['title'])

    print("Employee {} is done with tasks({}/20):\n{}".format(name['name'],
                                                              comp_task, title),
          end='')