# Alex Thompson 498430
# Software Engineering coursework
# 20/01/2013
#

from graphics import *

def main():
    while True:
        try:
            tasks = int(input("Please enter the number of tasks in your project: "))
            if tasks > 0 and tasks <= 10:
                break
            else:
                print("Invalid value, the number of tasks must be between 1 and 15")
                print("Maximum number of tasks is 10!")
        except ValueError:
            print("Value invalid!")
    theTasks(tasks)

def theTasks(tasks):
    win = GraphWin("Gantt Chart, Pert Chart, WBT", 100, 50)
    task = 1
    for i in range(tasks):
        print("Task", task)
        taskName = input("What is the name for this task: ")
        while True:
            try:
                subTasks = int(input("Please enter the number of sub tasks in your project: "))
                if subTasks >= 0 and subTasks <= 5:
                    break
                else:
                    print("This value is invalid!")
                   print("The tasks need to be between 0 and 5.")
            except ValueError:
                print("Value invalid!")
        subTask = 1
        for i in range(subTasks):
            print("Sub Task", subTask)
            subTaskName = input("What is the name for this sub task: ")
            while True:
                try:
                    duration = int(input("Please enter the duration for this sub tasks (days): "))
                    if duration > 0 and duration <= 5:
                        break
                    else:
                       print("Maximum number for duration is 5 days!")
                except ValueError:
                    print("Value invalid!")
            subTask = subTask + 1
        task = task + 1

    win.getMouse()
    win.close()
    
main()

