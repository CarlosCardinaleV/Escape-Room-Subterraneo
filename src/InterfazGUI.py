import tkinter as tk
from tkinter import simpledialog, messagebox

class EscapeRoomGUI:
    def __init__(self):
        # Initialize the hidden main window
        self.root = tk.Tk()
        self.root.withdraw()
        self.root.title("Underground Escape Room")

    def show_message(self, message):
        """Displays an information message box."""
        messagebox.showinfo("ESCAPE ROOM", message)

    def ask_string(self, prompt):
        """Requests a text string from the user."""
        return simpledialog.askstring("Input", prompt, parent=self.root)

    def ask_float(self, prompt):
        """Requests a decimal number (double/float) with built-in validation."""
        return simpledialog.askfloat("Input", prompt, parent=self.root)

    def ask_int(self, prompt):
        """Requests an integer with built-in validation."""
        return simpledialog.askinteger("Input", prompt, parent=self.root)

    def ask_boolean(self, prompt):
        """Displays a Yes/No dialog for boolean input."""
        return messagebox.askyesno("Selection", prompt, parent=self.root)

    def close(self):
        """Properly closes the GUI resources."""
        self.root.destroy()

# --- Main Application Logic ---
if __name__ == "__main__":
    gui = EscapeRoomGUI()

    # Introduction
    gui.show_message("Welcome to the Underground Escape Room!")

    # Collecting Data
    user_name = gui.ask_string("Enter your character's name:")
    
    # Using float for 'Double' logic
    item_weight = gui.ask_float("Enter the weight of the golden idol (decimal):")
    
    # Using int for 'Long' or 'Int' logic
    room_code = gui.ask_int("Enter the 4-digit security code:")
    
    is_ready = gui.ask_boolean("Are you ready to begin the challenge?")

    # Outputting results to console
    print("--- Game Session Started ---")
    print(f"Player: {user_name}")
    print(f"Idol Weight: {item_weight}")
    print(f"Entered Code: {room_code}")
    print(f"Ready Status: {is_ready}")

    gui.show_message("Setup finished. The door is locking behind you...")
    
    gui.close()