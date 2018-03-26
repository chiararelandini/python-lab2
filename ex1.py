'''
Given a list of tasks (i.e., actions that the user wants to do in the future) implement a todo_manager
program to perform 4 actions:
1. insert a new task (a string of text);
2. remove a task (by typing its content, exactly);
3. show all existing tasks, sorted in alphabetic order;
4. close the program.
At startup, the program shows a menu with the 4 options and, for each choice, performs the requested action.
After the action (except action 4), the program returns to the prompt for actions.
'''

tasks = []

while(True):
    print("What do you want to do? (options 1-4)")
    print("1. insert a new task (a string of text);"
          + "\n2. remove a task (by typing its content, exactly);"
          + "\n3. show all existing tasks, sorted in alphabetic order;"
          + "\n4. close the program.")
    choice = int(input())
    if choice == 1:
        print("Which task do you want to insert?")
        new = input()
        tasks.append(new)
    elif choice == 2:
        print("Which task do you want to remove?")
        task = input()
        if task in tasks:
            tasks.remove(task)
        else :
            print("The task you want to remove is not in you list!")
    elif choice == 3:
        print("The tasks you have planned are:")
        tasks.sort()
        for task in tasks:
            print(task)
    elif choice == 4:
        print("You have chosen to close the program. Bye bye.")
        exit(0);
    else:
        print("Available choices are options 1-4 !")