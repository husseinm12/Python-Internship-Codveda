import json
import os

TASK_FILE = "task.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE,'r') as f:
        try:
            return json.load(f) # convert JSON from the file into a python list of dictionaries
        except json.JSONDecodeError: 
            return []
        
def save_tasks(tasks):
    with open ( TASK_FILE, 'w') as f:
        json.dump(tasks,f,indent=4) # convert python into JSON and writes it in a pretty format with indentation

def add_task(description):
    tasks = load_tasks()
    task= { "description" : description , "done" : False }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added./n")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
       print(" No tasks found.")
       return
    for i, task in enumerate (tasks):
        status= "✅" if task ["done"] else "❌"
        print(f"{i+1}.[{status}] {task['description']}")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed= tasks.pop(index-1)
        save_tasks(tasks)
        print(f" 🗑️ Deleted task: {removed['description']}")
    except IndexError:
        print(" Error: Task number not found.")

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print(f" ✅ Task marked as done completed.") 

    except IndexError:
        print("❌ Error: Task number not found.")   

    
def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. Add task")
    print("2. List tasks")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Exit")


def main():
    while True:
            show_menu()
            choice = input("Please choose a number ").strip()
            if choice =="1":
                desc = input("please enter a description ").strip()
                add_task(desc)
            elif choice =="2":
                list_tasks()
            elif choice =="3":
                try:
                    i = int(input("Please enter the number of task you want to delete "))
                    delete_task(i)
                except ValueError:
                        print("Invalid number")    
            elif choice=="4":
                try:
                    i= int(input ("Please enter the number of task you want to mark as done "))
                    mark_done(i)
                except ValueError:
                    print("Invalid number")  
            elif choice =="5":
                print("Goodbye!")
                break
            else:
                print("Invalid choise, please enter a number between 1 and 5 ")                     
          


if __name__ == "__main__":
    main()