# 📝 Basic To-Do App in Python (Beginner-Friendly)

This is a simple text-based To-Do app using Python, where users can add and view tasks by selecting options from a menu. 

> 🔄 **All tasks will be saved to a file using Python's `open()` and `json` methods.**

---

## ✅ Step-by-Step Plan

### 1. Start your program.

### 2. Create an empty list
- Use a list to store tasks.
- Each task will contain a **title** and a **description**.

### 3. Create a function to add a new task
- Ask the user to enter:
  - Task **title**
  - Task **description**
- Store the task as a dictionary or tuple.
- Append the task to the list.

### 4. Create a function to view all tasks
- If the list is empty, display:
  - `"No tasks found."`
- If not, loop through and display:
  - Task number
  - Title
  - Description

### 5. Create a main menu inside a loop
- Show options:
- Add Task
- View Tasks
- Exit


- Ask the user for input (1, 2, or 3).

### 6. Use `if-else` or `match-case` to handle options
- If `1` → Call the **add task** function.
- If `2` → Call the **view tasks** function.
- If `3` → Exit the loop/program.
- Else → Show `"Invalid choice."`

### 7. Test your program
- Run and check that all menu options work as expected.

### 8. Optional Features
- Add a **delete task** option.
- Add an **update task** option.
- Save/load tasks to/from a file for persistence.

---
