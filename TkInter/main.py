import tkinter as tk
from tkinter import messagebox


class MyGUI:
    
    def __init__(self):
        self.root = tk.Tk()
        
        # Create Menu Bar
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close', command=self.on_closing)
        self.filemenu.add_command(label='Force Close', command=exit)
        
        self.menubar.add_cascade(menu=self.filemenu, label='Configuration')
        self.root.config(menu=self.menubar)
        
        self.root.geometry('720x480')
        self.root.title('First GUI')
        
        self.label = tk.Label(self.root, text='Your Message', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind('<KeyPress>', self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text='Check Message', font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        self.clear = tk.Button(self.root, text='Clear', font=('Arial', 18), command=self.clear_message)
        self.clear.pack(padx=10, pady=10)
        
        # Create Exit App Button Condition
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Run The App
        self.root.mainloop()
        
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))
    
    def shortcut(self, event):
        if event.state == 12 and event.keysym == 'Return':
            self.show_message()
    
    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Want to Quit?'):
            self.root.destroy()
    
    def clear_message(self):
        self.textbox.delete('1.0', tk.END)

MyGUI()
