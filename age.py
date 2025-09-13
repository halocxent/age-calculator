import tkinter as tk
def start_calculation():
    age = age_entry.get()
    if age.isdigit():
        age_entry.config(state='disabled')
        calculate_button.config(state='disabled')
        animate_label(0, age, "")
    else:
        tk.messagebox.showerror("Error", "Please enter a valid number.")
def animate_label(dot_count, age, text):
    dots = '.' * (dot_count % 4)
    result_label.config(text=f"Calculating{dots}")
    
    if dot_count < 8:
        root.after(250, animate_label, dot_count + 1, age, text)
    else:
        result_label.config(text=f"Your age is: {age}")
        age_entry.config(state='normal')
        calculate_button.config(state='normal')
root = tk.Tk()
root.title("Full-Screen Age Calculator")
root.attributes("-fullscreen", True)
root.config(bg="#1e1e1e")
label = tk.Label(root, text="Enter your age:", font=("Arial", 30), bg="#1e1e1e", fg="white")
label.pack(pady=40)
age_entry = tk.Entry(root, font=("Arial", 25), justify='center')
age_entry.pack(pady=20)
calculate_button = tk.Button(root, text="Calculate Age", font=("Arial", 25), command=start_calculation)
calculate_button.pack(pady=30)
result_label = tk.Label(root, text="", font=("Arial", 35), bg="#1e1e1e", fg="#00ff00")
result_label.pack(pady=50)
root.bind("<Escape>", lambda e: root.destroy())
root.mainloop()
