TASKS = "list.txt"

def ShowTasks():
    with open(TASKS, "r") as file:
        tasks = file.readlines()
        for task in tasks:
            print(task.strip())

def AddTasks():
    taskadd = input("Enter a task to add: ")
    with open(TASKS, "a") as file:
        file.write(taskadd + "\n")
    print(f"Task '{taskadd}' added")

def DelTasks(line_num):
    with open(TASKS,"r")as file:
        task_list = file.readlines()

    with open(TASKS, "w") as file:
        for i, task in enumerate(task_list):
            if line_num != i + 1:
                file.write(f"{task}")

        print("Task Removed Succesfully")

def CompTasks():
    ShowTasks()
    line_num = int(input("Enter the task number to mark as complete: "))

    with open(TASKS, "r") as file:
        tasks_list = file.readlines()

    with open(TASKS, "w") as file:
        for i, task in enumerate(tasks_list):
            if line_num == i + 1:
                file.write(task.strip() + " (DONE)\n")
            else:
                file.write(task)

    print(f"Task {line_num} marked as complete!")

def EditTasks():
    ShowTasks()
    num_line = int(input("Enter a task to edit: "))
    user_add = input("Enter what you would like to add to this task: ")

    with open(TASKS, "r") as file:
        list_tasks = file.readlines()

    with open(TASKS, "w") as file:
            for i, task in enumerate(list_tasks):
                if num_line == i + 1:
                    file.write(task.strip() + " " + user_add + "\n")  
                else:
                    file.write(task)

    print(f"Task {user_add} has now been updated")

def main():
    MainTrue = True
    while MainTrue == True:
    
        print("1.Show | 2.Add | 3.Delete | 4.Complete | 5.Edit")
        UserInput = input ("Enter what you would like to do: ").strip()

        if UserInput == "1":
            ShowTasks()
        elif UserInput == "2":
            AddTasks()
        elif UserInput == "3":
            DelInput = int(input("Enter the number according to the task: "))
            DelTasks(DelInput)
        elif UserInput == "4":
            CompTasks()
        elif UserInput == "5":
            EditTasks()
        else:
            print("Enter a valid number")

        InputUser = input("Would You like to use the program again (Y/N): ").strip().upper()
        
        UserTrue = True

        if InputUser == "N":
            MainTrue = False
        else:
            MainTrue = True
main()




