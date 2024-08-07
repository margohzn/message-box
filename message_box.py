import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Information", "This will contain information message")

def show_warning():
    messagebox.showwarning("Warning", "This will conatin warning message")

def show_error():
    messagebox.showerror("Erorr", "This will conatin erorr message")

def ask_question():
    result = messagebox.askquestion("Question", "Do you want to proceed")
    messagebox.showinfo("Response", f"your response: {result}")

def ask_yes_no():
    result = messagebox.askyesno("Question", "Do  you agree?")
    if result:
        messagebox.showinfo("Agreement", "you agreed")
    else:
        messagebox.showinfo("Disagreemnet", "you disagreed")

def yes_no_cancel():
    result = messagebox.askyesnocancel("Question", "Do you want to save the chnages?")
    if result is True:
        messagebox.showinfo("Save", "Your changes will be saves!")
    elif result is False:
        messagebox.showinfo("Not Save", "Your chnages will not be saved")
    else:
        messagebox.showinfo("canceled", "Opperation canceled")



window = tk.Tk()
window.geometry("300x500")
window.title("Tkinter message box exmaples")

info_button = tk.Button(window, text = "Show info", command = show_info).pack(pady = 30)
warning_button = tk.Button(window, text = "Show warning", command = show_warning).pack()
error_button = tk.Button(window, text = "Show error", command = show_error).pack(pady = 30)
question_button = tk.Button(window, text = "Ask question", command = ask_question).pack()
yes_no_button = tk.Button(window, text = "Ask yes/no", command = ask_yes_no).pack(pady = 30)
yes_no_cancel_button = tk.Button(window, text = "Ask yes/no/cancel", command = yes_no_cancel).pack()
retry_cancel_button = tk.Button(window, text = "Ask retry/cancel").pack(pady = 30)
ok_canel_button = tk.Button(window, text = "Ask ok camcel").pack()

window.mainloop()