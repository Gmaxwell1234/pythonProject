import random
import tkinter as tk

# Global variables
counter = 0

# Function to flip the coin and display the result
def flip_coin():
    global counter
    result = random.choice(["Heads", "Tails"])
    counter += 1
    result_label.config(text="Result: " + result)
    counter_label.config(text="Number of flips: " + str(counter))

# Create a tkinter window
window = tk.Tk()
window.title("Coin Flip")
window.geometry("300x250")

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=10)

# Create a label to display the counter
counter_label = tk.Label(window, text="Number of flips: " + str(counter))
counter_label.pack(pady=10)

# Create a button to flip the coin
flip_button = tk.Button(window, text="Flip Coin", command=flip_coin)
flip_button.pack(pady=10)

# Create a button to reset the counter
reset_button = tk.Button(window, text="Reset Counter", command=lambda: reset_counter())
reset_button.pack(pady=10)

# Function to reset the counter
def reset_counter():
    global counter
    counter = 0
    counter_label.config(text="Number of flips: " + str(counter))

# Start the tkinter mainloop
window.mainloop()
