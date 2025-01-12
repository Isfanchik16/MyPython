from tkinter import *
from tkinter.ttk import *
from time import strftime

# Create the main window
root = Tk()
root.title("Enhanced Clock")
root.resizable(True, True)
root.geometry("600x400")  # Set a default size for the window
root.attributes('-alpha', 0.95)  # Slightly transparent background

# Function to update the time and date
def update_time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%A, %B %d, %Y')
    label_time.config(text=current_time)
    label_date.config(text=current_date)
    label_time.after(1000, update_time)

# Function to change themes
def change_theme(color):
    label_time.config(background=color)
    label_date.config(background=color)
    label_greeting.config(background=color)

# Function to display a greeting based on the time of day
def get_greeting():
    hour = int(strftime('%H'))
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

# Clock display
label_time = Label(root, font=("ds-digital", 80), background='black', foreground='cyan')
label_time.pack(anchor='center', pady=10)

# Date display
label_date = Label(root, font=("ds-digital", 30), background='black', foreground='cyan')
label_date.pack(anchor='center')

# Greeting display
label_greeting = Label(root, text=get_greeting(), font=("Arial", 20), background='black', foreground='yellow')
label_greeting.pack(anchor='center', pady=10)

# Theme buttons
theme_frame = Frame(root)
theme_frame.pack(pady=20)

Button(theme_frame, text="Black Theme", command=lambda: change_theme("black")).pack(side=LEFT, padx=10)
Button(theme_frame, text="Blue Theme", command=lambda: change_theme("blue")).pack(side=LEFT, padx=10)
Button(theme_frame, text="Green Theme", command=lambda: change_theme("green")).pack(side=LEFT, padx=10)

# Exit button
Button(root, text="Exit", command=root.destroy).pack(pady=20)

# Start the clock
update_time()
root.mainloop()
