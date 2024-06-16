import subprocess
import re
import tkinter as tk
from tkinter import messagebox

def get_ipv4_address():
    # Run the ipconfig command and capture the output
    result = subprocess.run(["ipconfig"], capture_output=True, text=True)

    # Use a regular expression to find the IPv4 address
    ipv4_regex = re.compile(r'IPv4 Address[^\:]*\: (\d+\.\d+\.\d+\.\d+)')
    match = ipv4_regex.search(result.stdout)
    
    if match:
        return match.group(1)
    else:
        return "No IPv4 address found."

def show_ip_address():
    ipv4_address = get_ipv4_address()
    messagebox.showinfo("IPv4 Address", f"Your IPv4 address is: {ipv4_address}")

# Create the main Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show the IPv4 address dialog immediately
show_ip_address()

# Close the Tkinter main window after showing the message box
root.destroy()
