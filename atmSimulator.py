import tkinter as tk
from tkinter import messagebox

# Initialize the balance
balance = 5000
password = 1234

def check_pin():
    try:
        entered_pin = int(pin_entry.get())
        if entered_pin == password:
            show_options()
        else:
            messagebox.showerror("Error", "Wrong PIN. Please try again.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid PIN (numeric).")

def show_options():
    main_window.destroy()
    options_window = tk.Tk()
    options_window.title("ATM Options")
    options_window.geometry("400x300")  # Set a larger window size

    def check_balance():
        messagebox.showinfo("Balance", f"Your current balance is {balance}")

    def withdraw():
        try:
            withdraw_amount = int(withdraw_entry.get())
            global balance
            if withdraw_amount > balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                balance -= withdraw_amount
                messagebox.showinfo("Success", f"{withdraw_amount} debited from your account successfully.")
                messagebox.showinfo("Balance", f"Your remaining balance is {balance}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount (numeric).")

    def deposit():
        try:
            deposit_amount = int(deposit_entry.get())
            global balance
            balance += deposit_amount
            messagebox.showinfo("Success", f"{deposit_amount} credited to your account successfully.")
            messagebox.showinfo("Balance", f"Your total balance is {balance}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount (numeric).")

    balance_button = tk.Button(options_window, text="Check Balance", command=check_balance)
    withdraw_entry = tk.Entry(options_window)
    withdraw_button = tk.Button(options_window, text="Withdraw", command=withdraw)
    deposit_entry = tk.Entry(options_window)
    deposit_button = tk.Button(options_window, text="Deposit", command=deposit)

    balance_button.pack(pady=10)
    withdraw_entry.pack(pady=10)
    withdraw_button.pack(pady=10)
    deposit_entry.pack(pady=10)
    deposit_button.pack(pady=10)

    options_window.mainloop()

# Create the main window
main_window = tk.Tk()
main_window.title("ATM Simulator")

pin_label = tk.Label(main_window, text="Enter your ATM PIN:")
pin_entry = tk.Entry(main_window, show="*")
pin_button = tk.Button(main_window, text="Submit", command=check_pin)

pin_label.pack(pady=10)
pin_entry.pack(pady=10)
pin_button.pack(pady=10)

main_window.mainloop()
