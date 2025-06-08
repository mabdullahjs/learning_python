import json 

fileName = 'task.txt'
def loadTask():
    try:
        with open(fileName , 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(task):
    with open(fileName, 'w') as file:
        json.dump(task, file)

def viewAllTask():
    task = loadTask()
    for index , task in enumerate(task):
        print("-" * 70)
        print(f"{index + 1}: title => {task["title"]} \ndescription => {task["description"]}")
        print("-" * 70)
    print("*" * 70)

def viewSingleTask():
    task = loadTask()
    if not task:
        print("no task found")
        return 
    
    
    try:
        index = int(input("tell me single task number: "))
        selected = task[index - 1]
        if index < 1 or index > len(task):
            print("invalid task number")
        else:
            print("-" * 70)
            print(f"Title: {selected['title']}")
            print(f"Description: {selected['description']}")
            print("-" * 70)
    except:
        print("Please enter a valid number. ")


def addTask():
    task = loadTask()
    title = input("enter title: ")
    desc = input("enter description: ")
    task.append({"title" : title , "description": desc})
    save_data_helper(task)


def deleteSingleTask():
    task = loadTask()
    try:
        index = int(input("tell me single task number: "))
        if index < 1 or index > len(task):
            print("invalid task number")
        else:
            del task[index - 1]
            save_data_helper(task)
    except:
        print("Please enter a valid number. ")


def deleteAllTask():
    task = []
    save_data_helper(task)

def UpdateTask():
    task = loadTask()
    if not task:
        print("No tasks available to update.")
        return

    try:
        index = int(input("Enter the task number you want to update (starting from 1): "))
        if index < 1 or index > len(task):
            print("❌ Invalid task number.")
            return

        selected = task[index - 1]
        print("\nCurrent Task Details:")
        print(f"Title: {selected['title']}")
        print(f"Description: {selected['description']}")

        new_title = input("Enter new title (leave blank to keep current): ")
        new_description = input("Enter new description (leave blank to keep current): ")

        if new_title:
            selected['title'] = new_title
        if new_description:
            selected['description'] = new_description

        task[index - 1] = selected 
        save_data_helper(task)

        print("Task updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


task = loadTask()

def main():
    while True:
        print('\nWelcome to Todo App \n')
        print('1. View all task')
        print('2. View single task')
        print('3. Add task')
        print('4. Delete single task')
        print('5. Delete all task')
        print('6. Update task')
        print('7. Exit App \n')

        selectedOption = input("enter your choice: ")

        match selectedOption:
            case '1':
                viewAllTask()
            case '2':
                viewSingleTask()
            case '3':
                addTask()
            case '4':
                deleteSingleTask()
            case '5':
                deleteAllTask()
            case '6':
                UpdateTask()
            case '7':
                break
            case _:
                print("invalid input")


if __name__ == "__main__":
    main()