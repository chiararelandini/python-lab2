'''
Extend the program developed in the previous exercise to save and retrieve the list of tasks to/from
a text file. The file name is read as the first parameter from the command line.
Consequently, at startup, the program takes the list of tasks from the file and saves the changes to
the file as soon as the user decides to close the program.
For this exercise, you can get the task_list.txt file from the GitHub repository of this lab. It contains
6 tasks saved as a separate line on the file.
'''

from sys import argv
script, file = argv

txt = open(file)

tasks = []

lines = txt.read().split("\n")

txt.close()

for line in lines:
    if line != "":
        tasks.append(line)

def is_substring(string, substring):
    if string.find(substring) == -1:
        return False
    else:
        return True

while(True):
    print("What do you want to do now? (options 1-4)")
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
            found = False
            for todo in tasks:
                if is_substring(todo, task) == True:
                    tasks.remove(todo)
                    found = True
                    break
            if(found == False):
                print("The task you want to remove is not in you list!")
    elif choice == 3:
        print("The tasks you have planned are:")
        tasks.sort()
        for task in tasks:
            print(task)
    elif choice == 4:
        target = open(file, "w")
        for task in tasks:
            target.write(task+"\n")
        target.close()
        print("You have chosen to close the program. Your tasks have been saved. Bye bye.")
        exit(0);
    else:
        print("Available choices are options 1-4 !")