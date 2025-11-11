# tasks = []   # yaha saare tasks store honge

# while True:
#     print("\n1. Add Task")
#     print("2. Show Tasks")
#     print("3. Mark Task as Done")
#     print("4. Delete Task")
#     print("5. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         task_name = input("Enter task: ")
#         tasks.append([task_name, "Pending"])   # list: [task, status]
#         print("Task Added.")

#     elif choice == 2:
#         print("\nYour Tasks:")
#         for i in range(len(tasks)):
#             print(i+1, tasks[i][0], "-", tasks[i][1])

#     elif choice == 3:
#         num = int(input("Enter task number to mark Done: "))
#         tasks[num-1][1] = "Done"
#         print("Task Updated.")

#     elif choice == 4:
#         num = int(input("Enter task number to delete: "))
#         del tasks[num-1]
#         print("Task Deleted.")

#     elif choice == 5:
#         break

#     else:
#         print("Invalid Choice.")


# ----------------------------------------------------------------------------------------------


task = []

while True:

    print("\nNo.1--> Add Taks")
    print("No.2--> Show Taks")
    print("No.3--> Mark as Taks Done")
    print("No.4--> Delete Taks")
    print("No.5--> Exit")

    choice = int(input("Enter Your Choice: "))

    if choice==1:
        task_name = input("Enter Your task: ")
        deadline = input("Enter deadline (Ex: Tomorrow / 5 PM / Monday): ")
        task.append([task_name, "Pending -", deadline])
        print("Task Added")

    elif choice==2:
        print("\nYour Task")
        print("-"*50)
        for i in range(len(task)):
            print(i+1, task[i][0], "-", task[i][1], task[i][2])
        print("-"*50)

    elif choice==3:
        num = int(input("Enter which no. you want: "))
        task[num-1][1] = "Done"
        print("Task Updated")

    elif choice==4:
        num = int(input("Enter the numbet to delete: "))
        del task[num-1]
        print("Task Deleted")

    elif choice==5:
        print("Thank You---- Task is Over")
        break

    else:
        print("Invalid Choice")


