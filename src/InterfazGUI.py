import tkinter as tk
from tkinter import simpledialog, messagebox

class InterfazGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

    def mostrarMensaje(self, mensaje):
        messagebox.showinfo("SCAPE ROOM SUBTERRANEO", mensaje)

    def solicitarString(self, mensaje):
        hilera = simpledialog.askstring("Input", mensaje)
        return hilera

    def solicitarDouble(self, mensaje):
        hilera = simpledialog.askstring("Input", mensaje)
        try:
            valor = float(hilera)
            return valor
        except ValueError:
            return 0.0

    def solicitarLong(self, mensaje):
        hilera = simpledialog.askstring("Input", mensaje)
        try:
            valor = int(hilera)
            return valor
        except ValueError:
            return 0

    def solicitarBoolean(self, mensaje):
        hilera = simpledialog.askstring("Input", mensaje)
        return hilera.lower() == "true"

    def solicitarInt(self, mensaje):
        hilera = simpledialog.askstring("Input", mensaje)
        try:
            valor = int(hilera)
            return valor
        except ValueError:
            return 0

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = InterfazGUI()
    mensaje = "This is a sample message."
    gui.mostrarMensaje(mensaje)
    hilera = gui.solicitarString("Enter a string:")
    print(f"String entered: {hilera}")
    valor_double = gui.solicitarDouble("Enter a double:")
    print(f"Double entered: {valor_double}")
    valor_long = gui.solicitarLong("Enter a long:")
    print(f"Long entered: {valor_long}")
    valor_boolean = gui.solicitarBoolean("Enter a boolean (true or false):")
    print(f"Boolean entered: {valor_boolean}")
    valor_int = gui.solicitarInt("Enter an integer:")
    print(f"Integer entered: {valor_int}")
    gui.run()