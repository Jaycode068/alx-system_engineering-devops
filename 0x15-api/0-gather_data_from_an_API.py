import requests

def get_employee_todo_progress(employee_id):
    # Make a GET request to the API
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos = response.json()

    # Get employee name
    employee_name = todos[0]['name'].split()[0]

    # Count the number of completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)

    # Display the progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{len(todos)}):")

    # Display the titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

# Provide the employee ID as a command-line argument
employee_id = int(input("Enter the employee ID: "))
get_employee_todo_progress(employee_id)

