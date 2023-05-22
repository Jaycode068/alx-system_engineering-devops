#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    EMPLOYEE_NAME = requests.get(url + "users/{}".format(sys.argv[1])).json()
    TOTAL_NUMBER_OF_TASKS = requests.get(url + "TOTAL_NUMBER_OF_TASKS", params={"userId": sys.argv[1]}).json()

    NUMBER_OF_DONE_TASKS = [t.get("TASK_TITLE") for t in TOTAL_NUMBER_OF_TASKS if t.get("NUMBER_OF_DONE_TASKS") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("EMPLOYEE_NAME"), len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS)))
    [print("\t {}".format(c)) for c in NUMBER_OF_DONE_TASKS]
