# 📋 To-Do List Application 

> AIML Project | CSA2001 – Fundamentals in AI and ML
> **Author:** Ayushi Rai | **Reg No:** 25BCE10017

--- 

## 🧾 Project Overview

This is a simple Command Line Interface (CLI) based To-Do List application built using Python. The project helps users manage their daily tasks efficiently by allowing them to add, view, remove, and mark tasks as completed.

It also provides file handling features so users can save their tasks and access them later. The use of colored output makes the interface more interactive and user-friendly.
This application allows users to:
- Add new tasks
- View existing tasks
- Remove tasks
- Mark tasks as completed
- Save tasks to a file
- Retrieve previously saved tasks

The project focuses on simplicity, usability, and practical implementation of Python concepts like lists, loops, conditionals, and file handling.


---


## 💻 System Requirements

To run this project smoothly, your system should meet the following requirements:

### 🖥️ Software Requirements

- Python 3.x installed  
- Terminal / Command Prompt / PowerShell / VS Code  

### 📦 Python Libraries Required

- colorama

### 🔧 Install Required Library

Run the following command in your terminal:

```bash
pip install colorama
```
--- 

## ⚙️ How to Set Up and Use the Application

Follow the steps below to properly set up and run the To-Do List application on your system.


### 🧩 Step 1: Download the Project

Clone this repository or download the ZIP file:

```bash
git clone https://github.com/your-username/todo-list-python.git
```

### 📂 Step 2: Navigate to Project Folder
Open your terminal and move into the project directory:

```bash
cd todo-list-python
```

### 📦 Step 3: Install Required Dependency
This project uses the colorama library for colored output.
Install it using:

```bash
pip install colorama
```

###▶️ Step 4: Run the Application

```bash
python filename.py
```

### 🎮 Step 5: Use the Application

Once the program starts, you will see:

```bash
========== TO DO LIST ==========
📋 Your To-Do List:

1️⃣  View Tasks 👀
2️⃣  Add Task ➕
3️⃣  Remove Task ❌
4️⃣  Exit 🚪
5️⃣  Mark Complete ✅
6️⃣  View Saved Tasks 📂
```
Enter the number corresponding to your choice and follow the instructions shown on the screen

--- 

## 🚀 Quick Guide

| Option | Action | How to Use |
|--------|--------|------------|
| 👀 1 | View Tasks | `Enter your choice: 1` → Displays all current tasks |
| ➕ 2 | Add Task | `Enter your choice: 2` → Enter your task when prompted |
| ❌ 3 | Remove Task | `Enter your choice: 3` → Enter task index to remove |
| 🚪 4 | Exit | `Enter your choice: 4` → Closes the application |
| ✅ 5 | Mark Complete | `Enter your choice: 5` → Enter task index to mark complete |
| 📂 6 | View Saved Tasks | `Enter your choice: 6` → Enter file name (e.g., tasks.txt) |

--- 

## 🧪 Example Walkthrough

Below is a sample run of the application to help you understand how it works:

```text
========== TO DO LIST ==========

📋 Your To-Do List:

1️⃣  View Tasks 👀
2️⃣  Add Task ➕
3️⃣  Remove Task ❌
4️⃣  Exit 🚪
5️⃣  Mark Complete ✅
6️⃣  View Saved Tasks 📂

Enter your choice: 2
Enter the task: Complete assignment
task added

do you want further changes ?(y/n): y

Enter your choice: 2
Enter the task: Buy groceries
task added

do you want further changes ?(y/n): y

Enter your choice: 1
1. Complete assignment
2. Buy groceries

do you want further changes ?(y/n): y

Enter your choice: 5
1. Complete assignment
2. Buy groceries
Enter index for the task completed: 1

Task left: ['Buy groceries']
Completed task: ['Complete assignment']

do you want further changes ?(y/n): y

Enter your choice: 3
1. Buy groceries
Enter index of the task to be removed: 1
Removed task: 1

do you want further changes ?(y/n): n

Do you want to save your tasks (y/n)? y
Enter file name to open/create (.txt): tasks.txt

 A new file will be created.
File saved successfully

THANK YOU !!

```

## 🛠️ Troubleshooting

| Issue | Possible Cause | Solution |
|------|--------------|---------|
| ModuleNotFoundError: No module named 'colorama' | Library not installed | Run `pip install colorama` |
| File not found error | File does not exist in folder | Check file name and ensure `.txt` file is in same directory |
| Program crashes on input | Invalid input (text instead of number) | Enter only numeric values for menu options |
| Task not removed or completed | Wrong index entered | Make sure index matches displayed task number |
| Tasks not saving | Skipped save option or file issue | Enter `y` when prompted and check file permissions |
| Colors not displaying | Unsupported terminal | Use VS Code terminal / CMD / PowerShell |
| Nothing happens after input | Incorrect flow or skipped step | Follow menu instructions carefully |

---

## 🤖 AI / ML Concepts Used

Although this project is not a full Artificial Intelligence or Machine Learning system, it incorporates some fundamental logical concepts that are commonly used in AI-based applications:

| Concept | Description | Application in Project |
|--------|-------------|----------------------|
| Decision Making | Using conditional statements to choose actions based on input | The program uses `if-else` to perform actions based on user choices |
| State Management | Tracking and managing different states of data | Tasks are divided into "pending" and "completed" lists |
| Rule-Based System | System follows predefined rules to respond | Each menu option triggers a specific operation |
| User Interaction Logic | System responds dynamically to user input | Program continuously interacts using menu-driven interface |
| Data Persistence | Storing and retrieving data for later use | Tasks are saved and loaded using `.txt` files |

### 🧠 Note
This project focuses on core programming logic. These concepts form the foundation for more advanced AI/ML systems but are implemented here in a basic, rule-based manner.

---


*Presented by : Ayushi Rai | Reg No : 25BCE10017*







