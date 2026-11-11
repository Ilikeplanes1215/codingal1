total_homework = 4 
original_count = total_homework
completed_count = 0
task_num = 1
while task_num <= total_homework:
    if task_num == 1:
        print("Do your science homework")
    elif task_num == 2:
        print("Do your coding homework")
    elif task_num == 3:
        print("Do your english homework")
    else:
        print("Do your math homework")
    choice = input("Is the task finished?(yes/no) ")
    if choice == "yes":
            completed_count = completed_count + 1
            task_num = task_num + 1
            remaining_tasks = total_homework - completed_count
            print("you have", total_homework - completed_count, "tasks to do")
    print("The original count is: ", original_count,".The completed count is: ", completed_count,".The remaining task are: ", remaining_tasks)