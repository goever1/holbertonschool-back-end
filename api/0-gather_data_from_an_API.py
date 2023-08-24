#!/usr/bin/python3
"""It returns information about a to-do list of an employee"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + user_id, timeout=5)
        name = requests.get('https://jsonplaceholder.typicode.com/users/' + user_id, timeout=5)
    except requests.exceptions.RequestException as e:
        print("Error making HTTP request:", e)
        sys.exit(1)

    if to_do.status_code != 200 or name.status_code != 200:
        print("Failed to retrieve data. Check the user ID.")
        sys.exit(1)

    json_todo = to_do.json()
    json_names = name.json()

    all_tasks = 0
    comp_tasks = 0
    titles = []

    for item in json_todo:
        all_tasks += 1
        if item['completed']:
            comp_tasks += 1
            titles.append(item['title'])

    print("Employee {} is done with tasks ({}/{}):\n{}".format(json_names['name'], comp_tasks, all_tasks, "\n".join(titles)))