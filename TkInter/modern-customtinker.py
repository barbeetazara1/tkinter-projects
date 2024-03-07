import customtkinter as ck
import tkinter as tk


# customtkinter.enable_macos_darkmode()
# customtkinter.set_appearance_mode('System')
# customtkinter.set_default_color_theme('dark-blue')

# root = customtkinter.CTk()
root = tk.Tk()
root.title('Modern GUI')
root.geometry('270x350')

def button_function():
    print('Button Pressed')
    
def login():
    print('Test')

frame = ck.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = ck.CTkLabel(master=frame, text='Login System', text_font=('Arial', 12))
label.pack(pady=12, padx=10)

entry1 = ck.CTkEntry(master=frame)
entry1.pack(pady=12, padx=10)

entry2 = ck.CTkEntry(master=frame, show='*')
entry2.pack(pady=12, padx=10)

button = ck.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

# checkbox = ck.CTkCheckBox(master=frame, text='Remeber Me')
# checkbox.pack(pady=12, padx=10)


root.mainloop()