# def task():
#     tasks=[] #empty list
#     print('----- WELCOME TO THE TASK MANAGEMENT APP ------')

#     total_task=int(input('enter how many task you want to add:-'))
#     for i in range(1,total_task+1):
#         task_name=input(f'Enter task {i}=') # enter task 1=
#         tasks.append(task_name)

#     print(f'Todays tasks are \n{tasks}')
#     while True:
#         operation=int(input(  '  Enter 1- Add \n Enter 2- Update \n Enter 3-Delete \n Enter 4-View \n Enter 5-exit  \n'))
#         if operation==1:
#             add=input('enter task you want to add :-')
#             tasks.append(add)
#             print(f'tasks {add} has been added successfully')
#         elif operation==2:
#             updated_val=input('  enter the task name you want to update:-')
#             if updated_val in tasks:
#                 up=input('enter new task:-')
#                 ind=tasks.index(updated_val) #2
#                 tasks[ind]=up
#                 print(f'updated task {up}')
#         elif operation==3:
#             del_val=input('which task you want to delete:-')
#             if del_val in tasks:
#                 ind=tasks.index(del_val)
#                 del tasks[ind]
#                 print(f'task {del_val} has been deleted')
#         elif operation==4:
#             print('total task=',tasks)

#         elif operation==5:
#             print('closing the program')
#             break

#         else:
#             print('invalid input')

# task()


def task():
    tasks=[]
    print('---welcome to task management app---')
    total_task=int(input('how many task you want to add ='))
    for i in range(1,total_task+1):
        task_name=input(f'enter task{i} =')
        tasks.append(task_name)
    print(f'todays tasks are \n{tasks}')

    while True:
        operation = int(input(" Enter 1- Add \n Enter 2- Update \n Enter 3-Delete \n Enter 4-View \n Enter 5-exit  \n"))
        if operation==1:
            add=input('enter the task you want to add:-')
            tasks.append(add)
            print(f'the task {add} has been added successfully...')
        elif operation==2:
            updated_val=input('enter the task name you want to update :-')
            if updated_val in tasks:
                up=input('enter new task:-')
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print(f'the task {up} has been updated successfully.....')
        elif operation==3:
            del_val=input('enter the task you want to delete:-')
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f'the task {del_val} has been deleted successfully.....')
        elif operation==4:
            print('the tasks is ', tasks)
        elif operation==5:
            print('program is ended')
            break
    
        else:
            print('invalid number') 
            
task()   
                
            
