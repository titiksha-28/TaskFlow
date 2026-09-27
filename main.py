import tkinter as tk


# =========================
# Main Window
# =========================

root = tk.Tk()
root.title("TaskFlow")
root.geometry("600x600")
root.resizable(False, False)

# App colors
BG_COLOR = "#F5F7FB"
TEXT_COLOR = "#1F2937"

root.configure(bg=BG_COLOR)

# =========================
# Functions
# =========================

# Add a new task
def add_task():
    task = task_entry.get()

    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)


# Delete selected task
def delete_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_list.delete(selected_task[0])


# Mark selected task as complete
def complete_task():
    selected_task = task_list.curselection()

    if selected_task:
        index = selected_task[0]
        task = task_list.get(index)

        if not task.startswith("✓ "):
            task_list.delete(index)
            task_list.insert(index, "✓ " + task)


# Load selected task into entry box for editing
def edit_task():
    selected_task = task_list.curselection()

    if selected_task:
        index = selected_task[0]
        task = task_list.get(index)

        task_entry.delete(0, tk.END)
        task_entry.insert(0, task)


# Save edited task
def save_edit():
    selected_task = task_list.curselection()

    if selected_task:
        index = selected_task[0]
        new_task = task_entry.get()

        if new_task:
            task_list.delete(index)
            task_list.insert(index, new_task)
            task_entry.delete(0, tk.END)


# Delete all tasks
def clear_tasks():
    task_list.delete(0, tk.END)


# =========================
# App Heading
# =========================

title_label = tk.Label(
    root,
    text="TaskFlow",
    font=("Arial", 24, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

title_label.pack(pady=15)


# =========================
# Input Section
# =========================

input_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

input_frame.pack(pady=20)


task_label = tk.Label(
    input_frame,
    text="Enter Task",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

task_label.pack(side="left", padx=5)


task_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 11),
    bg="white",
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#D9DEE8",
    highlightcolor="#4F46E5"
)

task_entry.pack(side="left", padx=5)


# =========================
# Task List
# =========================

task_list = tk.Listbox(
    root,
    width=50,
    height=10,
    font=("Arial", 11),
    bg="white",
    fg=TEXT_COLOR,
    selectbackground="#DCE6F9",
    selectforeground=TEXT_COLOR,
    borderwidth=0,
    highlightthickness=1,
    highlightbackground="#D9DEE8",
    activestyle="none"
)

task_list.pack(pady=10,padx=20,ipady=5)


# =========================
# Button Section
# =========================

button_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

button_frame.pack(pady=10)

button_row1 = tk.Frame(
    button_frame,
    bg=BG_COLOR
)

button_row1.pack(pady=3)


button_row2 = tk.Frame(
    button_frame,
    bg=BG_COLOR
)

button_row2.pack(pady=3)
button_font = ("Arial", 10, "bold")

button_config = {
    "font": button_font,
    "width": 15,
    "bd": 0,
    "relief": "flat",
    "cursor": "hand2",
    "pady": 6
}

# =========================
# Buttons
# =========================

# Row 1
add_button = tk.Button(
    button_row1,
    text="Add Task",
    command=add_task,
    bg="#4F46E5",
    fg="white",
    activebackground="#4338CA",
    activeforeground="white",
    **button_config
)

add_button.pack(side="left", padx=5)


complete_button = tk.Button(
    button_row1,
    text="Complete Task",
    command=complete_task,
    bg="#10B981",
    fg="white",
    activebackground="#059669",
    activeforeground="white",
    **button_config
)

complete_button.pack(side="left", padx=5)


edit_button = tk.Button(
    button_row1,
    text="Edit Task",
    command=edit_task,
    bg="#F59E0B",
    fg="white",
    activebackground="#D97706",
    activeforeground="white",
    **button_config
)

edit_button.pack(side="left", padx=5)


# Row 2
delete_button = tk.Button(
    button_row2,
    text="Delete Task",
    command=delete_task,
    bg="#EF4444",
    fg="white",
    activebackground="#DC2626",
    activeforeground="white",
    **button_config
)

delete_button.pack(side="left", padx=5)


save_button = tk.Button(
    button_row2,
    text="Save Edit",
    command=save_edit,
    bg="#6366F1",
    fg="white",
    activebackground="#4F46E5",
    activeforeground="white",
    **button_config
)

save_button.pack(side="left", padx=5)


clear_button = tk.Button(
    button_row2,
    text="Clear All",
    command=clear_tasks,
    bg="#6B7280",
    fg="white",
    activebackground="#4B5563",
    activeforeground="white",
    **button_config
)

clear_button.pack(side="left", padx=5)


# =========================
# Keyboard Shortcut
# =========================

root.bind(
    "<Return>",
    lambda event: add_task()
)


# =========================
# Run Application
# =========================

root.mainloop()