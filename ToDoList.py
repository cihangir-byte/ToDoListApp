class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

if __name__ == "__main__":
    my_list = ToDoList()

    while True:
        print("1: Add task, 2: Remove task, 3: View tasks, 4: Quit")
        option = int(input("Choose an option: "))

        if option == 1:
            task = input("Enter a task: ")
            my_list.add_task(task)
        elif option == 2:
            task = input("Enter a task to remove: ")
            my_list.remove_task(task)
        elif option == 3:
            my_list.view_tasks()
        elif option == 4:
            break
