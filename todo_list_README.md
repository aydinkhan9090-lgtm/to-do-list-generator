<div align="center">

# 📝 To Do List CLI

![Python](https://img.shields.io/badge/Python-3.x-00ff41?style=for-the-badge&logo=python&logoColor=00ff41&labelColor=0d1117)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-00ff41?style=for-the-badge&labelColor=0d1117)
![Status](https://img.shields.io/badge/Status-Complete-00ff41?style=for-the-badge&labelColor=0d1117)

> **Project #7 — Add. Remove. View. Your tasks. Your control. 🖤**

</div>

---

## 💡 What It Does

```
1. Add any task you want
2. View all your tasks
3. Remove any task
4. Exit when done
```

---

## 🎮 Demo

```bash
Welcome to To Do List 📝
1. Add tasks
2. Remove tasks
3. Show tasks
4. Exit

1/2/3/4: 1
What is your task: Study Python
1/2/3/4: 1
What is your task: Go gym
1/2/3/4: 3
Study Python
Go gym
1/2/3/4: 2
Which task to remove: Go gym
1/2/3/4: 3
Study Python
1/2/3/4: 4
```

---

## ▶️ Run It

```bash
python todo_list.py
```

---

## 🧠 Concepts Used

| Concept | Purpose |
|---------|---------|
| `tasks = []` | Empty list to store tasks |
| `tasks.append(task)` | Add task to list |
| `tasks.remove(task)` | Remove task from list |
| `for task in tasks` | Loop through all tasks |
| `while True` | Keep running until exit |
| `if / elif / else` | Check user's choice |
| `break` | Exit when user picks 4 |

---

## 💻 Source Code

```python
print("Welcome to To Do List 📝")
print("1. Add tasks")
print("2. Remove tasks")
print("3. Show tasks")
print("4. Exit")

tasks = []

while True:
    choice = input("1/2/3/4: ")
    if choice == "1":
        task = input("What is your task: ")
        tasks.append(task)
    elif choice == "2":
        task = input("Which task to remove: ")
        tasks.remove(task)
    elif choice == "3":
        for task in tasks:
            print(task)
    elif choice == "4":
        break
    else:
        print("Choose from 1/2/3/4")
```

---

<div align="center">

[🔙 Back to Portfolio](../README.md) • [👤 My Profile](https://github.com/AYDINKHAN)

</div>
