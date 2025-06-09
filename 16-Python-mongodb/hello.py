import pymongo

client = pymongo.MongoClient("mongodb+srv://mabdullah2037:bustop123@testing.fsplzwv.mongodb.net/", tlsAllowInvalidCertificates=True)

print(client)
db = client["taskmanager"]
todo_collection = db["todo"]

def getTaskList():
    tasks = list(todo_collection.find())
    for i, todo in enumerate(tasks, start=1):
        print(f"{i}. Title: {todo['title']}, Description: {todo['description']}")
    return tasks

def viewAllTask():
    for index , todo in enumerate(todo_collection.find()):
        print(f"no:{index + 1}, title={todo["title"]}, desc={todo["description"]}")



def addTask():
    title = input("enter title: ")
    description = input("enter description: ")
    todo_collection.insert_one({"title": title, "description": description})
    print("todo added successfully")


def deleteTask(id):
    todo_collection.delete_one({"_id": id})


def UpdateTask(id):
    title = input("enter title: ")
    description = input("enter description: ")

    update_data = {}

    if title:
        update_data["title"] = title
    if description:
        update_data["description"] = description

    if not update_data:
        print("Please enter at least one value to update.")
        return

    todo_collection.update_one(
        {"_id": id},
        {"$set": update_data}
    )
    
    print("todo updated")



def main():
    while True:
        print('\nWelcome to Todo App \n')
        print('1. View all task')
        print('2. Add task')
        print('3. Delete task')
        print('4. Update task')
        print('5. Exit App \n')

        selectedOption = input("enter your choice: ")

        match selectedOption:
            case '1':
                viewAllTask()
            case '2':
                addTask()
            case '3':
                tasks = getTaskList()
                index = int(input("which task do you want to delete: "))
                deleteTask(tasks[index - 1]["_id"])
            case '4':
                tasks = getTaskList()
                index = int(input("which task do you want to delete: "))
                UpdateTask(tasks[index - 1]["_id"])
            case '5':
                break
            case _:
                print("invalid input")


if __name__ == "__main__":
    main()