class TodoApp:
    def __init__(self):
        print("WellCome To ToDo App")
        self.task_list = []
    def menu(self):
        while (True):
            try:
                print("(1)- Add Task\n(2)- Remove Task\n(3)- Show Task List\n(0)- Exit")
                choose_option = int(input("Enter Your Choice:"))
                if (choose_option == 1):
                    self.addTask()
                elif (choose_option == 2):
                    self.removeTask()
                elif (choose_option == 3):
                    self.showTask()
                elif (choose_option == 0):
                    exit()
                else:
                    print("Invalid Choice")
            except ValueError:
                print("----------Please Enter Valid Choice---------------")

    def addTask(self):
        while(True):
            print("(Type 'Back' For Back)")
            add = input("Enter Task:")
            self.task_list.append(add)
            if (add == "back" or add == "Back"):
                pass
            else:
                print(f"Task Added : '{add}'")
            if(add=="back" or add=="Back"):
                self.task_list.remove(add)
                break
        TodoApp()
    def removeTask(self):
        remove_task=input('Enter Task You Want to Remove:')
        if(remove_task not in self.task_list):
            print("---------Task not Available For Remove---------")
        else:
            self.task_list.remove(remove_task)
            print(f"Task '{remove_task}' Sucsesfully Removed")
            TodoApp()

    def showTask(self):
        print("--------Task List--------")
        num = 0
        for task in self.task_list:
            num = num+ 1
            print(f"\t\t\t({num})- {task}")
        print("--------Task List End--------")
        TodoApp()


if __name__ == '__main__':
    app=TodoApp()
    app.menu()

