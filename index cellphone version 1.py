import tkinter as tk
from tkinter import messagebox
import to_do_database as tdd

root=tk.Tk()
root.title("login")
root.geometry("400x300")
root.config(bg="beige")

attempts=0

def login():
    global attempts
    name=username_input.get().strip()
    pass_word=password_input.get().strip()

    matched = any(
        user["username"] == name and user["password"] == pass_word
        for user in tdd.storage
    )

    if matched:
        attempts = 0
        print("correct:)")
        login_frame.pack_forget()
        todo_frame.pack(fill="both", expand=True)
        root.config(menu=menu_bar)
    else:
        label.config(text="Incorrect credentials")
        attempts += 1
        print("incorrect:()")
        if attempts >= 3:
            print("attempts is '3' program destroy")
            root.destroy()

def sign_up():
    sign_name=sign_username_input.get().strip()
    sign_pass_word=sign_password_input.get().strip()

    if not sign_name:
        sign_label.config(text="username cannot be empty")
    elif any(user["username"] == sign_name for user in tdd.storage):
        sign_label.config(text="username already exists")
    elif len(sign_pass_word) < 6:
        sign_label.config(text="password must be at least 6 characters")
    else:
        add_account={"username":sign_name, "password":sign_pass_word}
        tdd.storage.append(add_account)
        sign_username_input.delete(0, tk.END)
        sign_password_input.delete(0, tk.END)
        sign_label.config(text=".")
        label.config(text="account created, please log in")
        sign_up_frame.pack_forget()
        login_frame.pack(fill="both", expand=True)

def login_btn():
    sign_up_frame.pack_forget()
    sign_label.config(text=".")
    sign_username_input.delete(0, tk.END)
    sign_password_input.delete(0, tk.END)
    login_frame.pack(fill="both", expand=True)

def signup_btn():
    login_frame.pack_forget()
    label.config(text=".")
    username_input.delete(0, tk.END)
    password_input.delete(0, tk.END)
    sign_up_frame.pack(fill="both", expand=True)

#----------login-------------
login_frame = tk.Frame(root, bg="beige")
login_frame.pack(fill="both", expand=True)

username=tk.Label(login_frame, text="username:", bg="beige", fg="black", font=("Inter", 12))
username.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

username_input=tk.Entry(login_frame, bg="beige", fg="black", width=20)
username_input.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

password=tk.Label(login_frame, text="password:", bg="beige", fg="black", font=("Inter", 12))
password.place(relx=0.2, rely=0.3, anchor=tk.CENTER)

password_input=tk.Entry(login_frame, bg="beige", fg="black", show="*", width=20)
password_input.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

label=tk.Label(login_frame, text=".", bg="beige", fg="black", font=("Inter", 12))
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

title_login=tk.Label(login_frame, text="LOG IN", bg="beige", fg="black", font=("Inter", 12))
title_login.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

btn=tk.Button(login_frame, text="log in", bg="beige", fg="black", font=("Inter", 12), command=login)
btn.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

sign_up_btn=tk.Button(login_frame, text="sign up account", bg="beige", fg="black", font=("Inter", 12), command=signup_btn)
sign_up_btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


#----------sign up--------------
sign_up_frame = tk.Frame(root, bg="beige")

sign_username=tk.Label(sign_up_frame, text="username:", bg="beige", fg="black", font=("Inter", 12))
sign_username.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

sign_username_input=tk.Entry(sign_up_frame, bg="beige", fg="black", width=20)
sign_username_input.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

sign_password=tk.Label(sign_up_frame, text="password:", bg="beige", fg="black", font=("Inter", 12))
sign_password.place(relx=0.2, rely=0.3, anchor=tk.CENTER)

sign_password_input=tk.Entry(sign_up_frame, bg="beige", fg="black", show="*", width=20)
sign_password_input.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

sign_label=tk.Label(sign_up_frame, text=".", bg="beige", fg="black", font=("Inter", 12))
sign_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

sign_title_label=tk.Label(sign_up_frame, text="SIGN UP", bg="beige", fg="black", font=("Inter", 12))
sign_title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

sign_btn=tk.Button(sign_up_frame, text="sign up", bg="beige", fg="black", font=("Inter", 12), command=sign_up)
sign_btn.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

log_in_btn=tk.Button(sign_up_frame, text="log in to account", bg="beige", fg="black", font=("Inter", 12), command=login_btn)
log_in_btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


password_input.bind("<Return>", lambda event: login())
sign_password_input.bind("<Return>", lambda event: sign_up())

#-----------todo frame------------
todo_frame = tk.Frame(root, bg="beige")

tk.Label(
    todo_frame, text="My To-do List",
    font=("Arial", 16), bg="beige"
).place(relx=0.5, rely=0.1, anchor=tk.CENTER)

task_input = tk.Entry(todo_frame, width=30)
task_input.place(relx=0.5, rely=0.22, anchor=tk.CENTER)

list_frame = tk.Frame(todo_frame)
list_frame.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

list_scrollbar = tk.Scrollbar(list_frame, orient="vertical")
list_scrollbar_x = tk.Scrollbar(list_frame, orient="horizontal")

tasks = tk.Listbox(list_frame, width=35, height=10,
                   yscrollcommand=list_scrollbar.set,
                   xscrollcommand=list_scrollbar_x.set)
tasks.grid(row=0, column=0, sticky="nsew")
list_scrollbar.grid(row=0, column=1, sticky="ns")
list_scrollbar_x.grid(row=1, column=0, sticky="ew")
list_scrollbar.config(command=tasks.yview)
list_scrollbar_x.config(command=tasks.xview)


def add_task():
    task = task_input.get().strip()

    if task:
        tasks.insert(tk.END, task)
        task_input.delete(0, tk.END)

def remove_task():
    selected = tasks.curselection()
    if selected:
        tasks.delete(selected[0])

def done_task():
    selected = tasks.curselection()
    if selected:
        index = selected[0]
        task = tasks.get(index)
        if not task.endswith("(done)"):
            tasks.delete(index)
            tasks.insert(index, task + " (done)")

def new_file():
    messagebox.showinfo("New", "This feature is under development")

def open_file():
    messagebox.showinfo("Open", "This feature is under development")

def sign_out():
    todo_frame.pack_forget()
    root.config(menu="")
    tasks.delete(0, tk.END)
    task_input.delete(0, tk.END)
    username_input.delete(0, tk.END)
    password_input.delete(0, tk.END)
    label.config(text="signed out")
    login_frame.pack(fill="both", expand=True)

def show_about():
    messagebox.showinfo("About", "This app is develop by first year IT student for their final project in programming one, this project involves user log in, sign up, storing multiple data and put it on a list box and sign out. This project is develop by us to practice our knowlegde and skills in programming.")

task_input.bind("<Return>", lambda event: add_task())

add_btn=tk.Button(todo_frame, text="Add Task", command=add_task)
add_btn.place(relx=0.86, rely=0.22, anchor=tk.CENTER)

tk.Button(
    todo_frame, text="Done",
    command=done_task
).place(relx=0.4, rely=0.31, anchor=tk.CENTER)

tk.Button(
    todo_frame, text="Remove",
    command=remove_task
).place(relx=0.6, rely=0.31, anchor=tk.CENTER)

menu_bar = tk.Menu(todo_frame)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Sign out", command=sign_out)
menu_bar.add_cascade(label="File", menu=file_menu)

tools_menu = tk.Menu(menu_bar, tearoff=0)
tools_menu.add_command(
    label="Show Message",
    command=lambda: messagebox.showinfo(
        "Tools", "This feature is under development"
    )
)
menu_bar.add_cascade(label="Tools", menu=tools_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
