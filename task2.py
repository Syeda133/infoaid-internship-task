import os 
#create a individual tasks
class Task:
    def __init__(self,title,description):
        self.title=title
        self.description=description
        self.status="Incomplete"
    def __str__(self):
        return f"Title: {self.title}\n Description: {self.description}\n Status:{self.status}\n"
#create a tasks to be performed
class Todolist:
    def __init__(self):
        self.task=[]
    def add_task(self,task):
        self.task.append(task)
    def delete_task(self,index):
        if 0 <= index < len(self.task):
            del self.task[index]
    def view_task(self):
        if not self.task:
            print("NO TASK IS THERE TO VIEW")
        else:
            for i, task in enumerate(self.task):
                print(f"Task {i+1}:\n{task}")

    def save_task(self,filename):
        with open(filename,"w") as file:
            for task in self.task:
                file.write(f"Title:{task.title}\n Description: {task.description}\n Status:{task.status}\n---\n ")
    def load_task(self,filename):
        if os.path.exists(filename):
            with open(filename,"r") as file:
                task_info=file.read().split("---\n")
                for info in task_info:
                    if info.strip():  # Ensure there's content to parse
                        lines = info.strip().split('\n')
                        title = lines[0].replace("Title: ", "")
                        description = lines[1].replace("Description: ", "")
                        status = lines[2].replace("Status: ", "")
                        task = Task(title, description)
                        task.status = status
                        self.add_task(task)
        else:
            print("File not found. No tasks loaded.")


# Main function to run the to-do list app
def main():
    todo_list = Todolist()

    # Load tasks from a file if it exists
    filename = "mine.txt"
    todo_list.load_task(filename)

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks") 
        print("5. Quit")
        choice = input("Enter your choice (1,2,3,4,5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '3':
            todo_list.view_task()
        elif choice == '4':
            todo_list.save_task(filename)
            print("Tasks saved successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Goodbye!")


if __name__ == "__main__":
    main()




    
