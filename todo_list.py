# todo.py

tasks = []

def show_menu():
    print("\n📋 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter your task: ")
    tasks.append({'task': task, 'done': False})
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("📭 No tasks yet.")
    else:
        for i, task in enumerate(tasks):
            status = "✔️ Done" if task['done'] else "❌ Not Done"
            print(f"{i+1}. {task['task']} - {status}")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]['done'] = True
            print("🎉 Task marked as done!")
        else:
            print("🚫 Invalid task number.")
    except ValueError:
        print("❌ Enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"🗑️ Removed: {removed['task']}")
        else:
            print("🚫 Invalid task number.")
    except ValueError:
        print("❌ Enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Goodbye! Have a productive day!")
        break
    else:
        print("❗ Invalid choice. Try again.")
