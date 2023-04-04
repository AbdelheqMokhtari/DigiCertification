from tkinter import *

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == 'admin' and password == 'password':
        login_label.config(text='Login successful!', fg='green')
    else:
        login_label.config(text='Login failed. Please try again.', fg='red')

# Create the window
window = Tk()
window.title('Login')

# Create the labels and entries
username_label = Label(window, text='Username:')
username_label.grid(row=0, column=0)

username_entry = Entry(window)
username_entry.grid(row=0, column=1)

password_label = Label(window, text='Password:')
password_label.grid(row=1, column=0)

password_entry = Entry(window, show='*')
password_entry.grid(row=1, column=1)

# Create the login button
login_button = Button(window, text='Login', command=login)
login_button.grid(row=2, column=1)

# Create the login label
login_label = Label(window, text='')
login_label.grid(row=3, column=1)

# Run the window
window.mainloop()
