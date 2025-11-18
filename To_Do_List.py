
task = []   #task yhn pe store hoga (task will be store here)


while True:
    print(f"Your Choice List")
    print("-"*50)
    print(f"1.  Add Task")
    print(f"2.  Show Task")
    print(f"3.  Mark as done")
    print(f"4.  Delete Task")
    print(f"5.  Update Task")
    print(f"6.  Exit")

    choice = int(input("Enter Your Choice--->> (1-4):  "))

    if choice == 1:
        tasks = input("Enter Your Task: ")
        deadline = input("Enter the Deadline  (Ex--> Tomarrow/5pm/Monday)")
        task.append([tasks, "Pending -", deadline])
        print("Task Added")

    elif choice == 2:
        print("\nYour Task")
        for i in range(len(task)):
            print(i+1, task[i][0], "-" , task[i][1], task[i][2])

    elif choice == 3:
        num = int(input("Enter Choice Number to Mark Done: "))
        task[num-1][1] = "Done"
        print("Task Updated")

    elif choice == 4:
        num = int(input("Enter Choice Number to Delete: "))
        del task[num-1]
        print("Task Deleted")

    elif choice == 5:
        num = int(input("Enter Task Number To Update: "))

        print("\nWhat do You Want to Update")
        print("1. Task Name")
        print("2. Task Status")
        print("3. Tast Deadline")
        print("4. Full Task Update")

        update = int(input("Enter Update Choice: "))

        if update ==1:
            new_name = input("Enter The New Task Name: ")
            task[num-1][0] = new_name
            print("New Name Updated")
        elif update ==2:
            new_status = input("Enter New Status---> (Done/Pendng): ")
            task[num-1][1] = new_status
            print("New Status Updated")
        if update ==3:
            new_deadline = input("Enter New Deadline: ")
            task[num-1][2] = new_deadline
            print("New Deadline Updated")
        if update ==4:
            new_name = input("Enter The New Task Name: ")
            new_status = input("Enter New Status:  (Done/Pendng): ")
            new_deadline = input("Enter New Deadline: ")
            task[num-1] = [new_name, new_status , new_deadline]
            print("Full Task Updated")
        

    elif choice == 6:
        print("Thank You, Task Over")
        break
    else:
        print("Invalid Choice")









