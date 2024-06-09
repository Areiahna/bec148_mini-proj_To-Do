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
            view_list()
        elif (ans == "3"):
            pass
            complete_task()
        elif (ans == "4"):
            delete_task()
        elif (ans == "5") :
            # Quitting the application.
            print("Thanks for using my app!")
            break
        else:
            print("Please enter choose an option below")
            continue

# Adding a task. 
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

# Viewing the list of tasks 
def view_list ():
    print("Your To-Do List")
    print("-" * 16)
    for task in range(len(todo_list)):
        print(f" - {todo_list[task]}")

# Marking a task as complete.
def complete_task ():
    mark_it = " [X]"
    task = input("Which task would you like to mark as complete?: ").lower()
    while True:
        try: 
            for x in range(len(todo_list)):
                if task == todo_list[x].lower():
                    todo_list[x] = task + mark_it
                
        except ValueError:
            print(f"It looks like you don't have {task} on your list\n")
            break
        else:
            print(f"COMPLETED\n")
            break

        finally:
            view_list()

# Deleting a task.
def delete_task ():

    task = input("Which task would you like to REMOVE?: ")
    while True:
        try:
            todo_list.remove(task)
        except ValueError:
            print(f"It looks like '{task}' is not on your list\n")
            break
        else:
            print("Task removed!\n")
            break
        finally:
            view_list()



main(todo_list)

