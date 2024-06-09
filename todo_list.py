# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task.
# Viewing the list of tasks 
# Marking a task as complete. (Bonus) (Hint: Use string manipulation to add "X" to the end of a task)
# Deleting a task.
# Quitting the application.

todo_list = []

def main(list):
    while True:
        ans = input(''' 
        Welcome to the To-Do List App!

        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit

        ''')

        if (ans == "1"):
            add_task()
        elif (ans == "2"):
            pass
        elif (ans == "3"):
            pass
        elif (ans == "4"):
            pass
        elif (ans == "5") :
            print(todo_list)
            print("Thanks for using my app!")
            break
        else:
            print("Please enter chose an option below")
            continue

def add_task (): 
    while True:
        ans = input("What would you like to add?: ")
        todo_list.append(ans)
        ans = input('''
        Would you like to add another item?
        y - yes
        n - no

        ''')
        if (ans == "y"):
            continue
        else:
            break


main(todo_list)