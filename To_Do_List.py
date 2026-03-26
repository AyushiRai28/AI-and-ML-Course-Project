from colorama import Fore, Style, init
import os

init(autoreset=True)

print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '========== TO DO LIST ==========')

print(Fore.CYAN + Style.BRIGHT + "📋 Your To-Do List:\n")

print( '''1️⃣  View Tasks 👀
2️⃣  Add Task ➕
3️⃣  Remove Task ❌
4️⃣  Exit 🚪
5️⃣  Mark Complete ✅
6️⃣  View Saved Tasks 📂
 ''')

def search_saved_file():
    name = input( Fore.CYANy + "Name of the file : ")
    if os.path.exists(name):
        print(Fore.LIGHTGREEN_EX + "✅Task File found!\n")
        
        with open(name, 'r') as file:
            content = file.read()
            print(Fore.LIGHTWHITE_EX + "--- Your tasks ---\n")
            print(content)
    else:
        print(Fore.LIGHTRED_EX + "❌ Task file not found in current folder")


task = []
completed = []
while True:
    choice = int(input( "Enter your choice: "))
    if choice == 2:
        inp = input(Fore.GREEN + "Enter the task: ")
        task.append(inp)
        print(Fore.GREEN + "task added")

    elif choice == 1:
        if task:
            for i, t in enumerate(task):
                print(Fore.LIGHTWHITE_EX + f"{i+1}. {t}")
                
        else:
            print(Fore.LIGHTBLUE_EX + "No tasks yet.")
            new = input("Search in saved files? (y/n)")
            if new == 'y' :
                search_saved_file()

    elif choice== 3:
        if task:
            for i,t in enumerate(task):
                print(f"{i+1}. {t}")
        rem1 = int(input(Fore.LIGHTMAGENTA_EX + "Enter index of the task to be removed: ") )
        rem = rem1 - 1
        if 0 <= rem < len(task):
            task.pop(rem)
            print(Fore.LIGHTMAGENTA_EX + f"Removed task: {rem1}")
    
        else:
            print(Fore.LIGHTRED_EX + "task not found")
            print (Fore.LIGHTRED_EX + "try again!!") 
            continue

    elif choice == 4:
        break    

    elif choice == 5:
        if task:
            for i,t in enumerate(task):
                print(f"{i+1}. {t}")
        completee = int(input(Fore.LIGHTYELLOW_EX + "Enter index for the task completed : "))
        complete = completee - 1

        if 0<= complete < len(task) :
            completed.append(task[complete])
            task.pop(complete)

            print("Task left: " , task)
            print("Completed task: ", completed)
        else:
            print(Fore.LIGHTRED_EX + "task not found")
            print (Fore.LIGHTRED_EX + "try again!!") 
            continue

    elif choice == 6 :
        search_saved_file()

    else :
        print(Fore.LIGHTYELLOW_EX + "invalid input!!")
        continue
        
    option = input(Fore.LIGHTWHITE_EX + "do you want further changes ?(y/n): ").lower()
    if option != "y" :
        break

final = { 'Tasks :' : task , 'Task completed :' : completed }    

savefile = input(Fore.LIGHTCYAN_EX + "Do you want  to save your tasks (y/n)??  ")
if savefile == 'y':

    filename = input(Fore.LIGHTBLUE_EX + "Enter file name to open/create (.txt): ")
    
    try:
        with open(filename, 'r') as file:
            print( Fore.LIGHTRED_EX + "\n--- Existing Content ---")
            content = file.read()
            print(content)
            add = input(Fore.BLUE + "Do you wanna add ? (y/n) ")
            if add == 'y' :
                with open(filename, 'a') as file:
                    file.write( str(final))
                    
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "\n A new file will be created.")
        
        with open(filename , 'w') as file:
            file.write(str(final))
            
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "File saved successfully")    

print(Style.BRIGHT + "THANK YOU !!")    


        




