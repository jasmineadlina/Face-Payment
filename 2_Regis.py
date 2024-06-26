
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    720.0,
    1024.0,
    fill="#D9D9D9",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    360.0,
    500.0,
    image=image_image_1
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    850.0,
    450.0,
    image=image_image_3
)

# image_image_2 = PhotoImage(
#     file=relative_to_assets("image_2.png"))
# image_2 = canvas.create_image(
#     1122.0,
#     350.0,
#     image=image_image_2
# )

canvas.create_rectangle(
    640.0,
    0.0,
    800.0,
    1024.0,
    fill="#000000",
    outline="")

canvas.create_text(
    988.0,
    180.0,
    anchor="nw",
    text="Registration",
    fill="#FFFFFF",
    font=("OpenSansHebrewCondensed Bold", 48 * -1)
)

# entry_image_1 = PhotoImage(
#     file=relative_to_assets("entry_1.png"))
# entry_bg_1 = canvas.create_image(
#     1128.0,
#     502.5,
#     image=entry_image_1
# )

entry_1 = Entry(
    bd=0,
    bg="#000000",
    fg="#FFFFFF",
    highlightthickness=0,
    insertbackground="#FFFFFF",
)
entry_1.place(
    x=988.0,
    y=486.0,
    width=280.0,
    height=30.0
)

# entry_image_2 = PhotoImage(
#     file=relative_to_assets("entry_2.png"))
# entry_bg_2 = canvas.create_image(
#     1128.0,
#     566.5,
#     image=entry_image_2
# )
entry_2 = Entry(
    bd=0,
    bg="#000000",
    fg="#FFFFFF",
    highlightthickness=0,
    insertbackground="#FFFFFF"
)
entry_2.place(
    x=988.0,
    y=550.0,
    width=280.0,
    height=30.0
)

entry_3 = Entry(
    bd=0,
    bg="#000000",
    fg="#FFFFFF",
    highlightthickness=0,
    insertbackground="#FFFFFF",
)
entry_3.place(
    x=988.0,
    y=415.0,
    width=280.0,
    height=30.0
)

text_username = canvas.create_text(
    958.0,
    465.0,
    anchor="nw",
    text="    Username",
    fill="#FFFFFF",  
    font=("OpenSansHebrewCondensed Bold", 24 * -1)
)

text_password = canvas.create_text(
    985.0,
    525.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("OpenSansHebrewCondensed Bold", 24 * -1),
)

text_name = canvas.create_text(
    985.0,
    392.0,
    anchor="nw",
    text="Name",
    fill="#FFFFFF",
    font=("OpenSansHebrewCondensed Bold", 24 * -1),
)

canvas.create_text(
    1010.0,
    750,
    anchor="nw",
    text="Already have an account? ",
    fill="#FFFFFF",
    font=("OpenSansHebrewCondensed Bold", 16 * -1)
)

text_login = canvas.create_text(
    1190.0,
    750.0,
    anchor="nw",
    text="Login",
    fill="#44AF0F",
    font=("OpenSansHebrewCondensed Bold", 14 * -1)
)

register= canvas.create_rectangle(
    988.0,
    630.0,
    1268.0,
    680.0,
    fill="#12480E",
    outline="")

canvas.create_text(
    990.0,
    640.0,
    anchor="nw",
    text="         Register Your Face",
    fill="#FFFFFF",
    font=("OpenSansHebrewCondensed Bold", 20 * -1)
)

# Binding event handler untuk teks Forget password?
canvas.tag_bind(text_login, "<Button-1>", lambda event: handle_login_click())
canvas.tag_bind(register, "<Button-1>", lambda event: handle_register_click())
# canvas.tag_bind(image_2, "<Button-1>", lambda event: handle_image_click())


def handle_login_click():
    # Logika untuk menangani klik pada tombol Registration
    window.quit()
    window.destroy()
    subprocess.run(["python", "C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\1_Login.py"]) 

def handle_register_click():
    # Logika untuk menangani klik pada tombol Login
    name = entry_3.get()
    username = entry_1.get()
    password = entry_2.get()

    if name and username and password:
        regis(name, username, password)
        window.quit()
        window.destroy()
        subprocess.run(["python", "C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\3_Angle1.py"]) 
    else:
        print("Please fill in all the fields")
    
# def handle_image_click():
#     window.quit()
#     window.destroy()
#     subprocess.run(["python", "C:\\Users\\jasmi\\OneDrive\\Documents\\Python\\Tugas Akhir_Viskom\\3_Angle1.py"]) 
    
def on_enter_reg(event):
    canvas.itemconfig(text_login, fill="#FFFFFF")

def on_enter_login(event):
    canvas.itemconfig(register, fill="#0D350A")

def on_leave_reg(event):
  canvas.itemconfig(text_login, fill="#44AF0F")
  
def on_leave_login(event):
  canvas.itemconfig(register, fill="#12480E")

canvas.tag_bind(text_login, "<Enter>", on_enter_reg)
canvas.tag_bind(text_login, "<Leave>", on_leave_reg)
canvas.tag_bind(register, "<Enter>", on_enter_login)
canvas.tag_bind(register, "<Leave>", on_leave_login)

canvas.create_rectangle(
    987.0,
    518.0,
    1268.0000138282758,
    519.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    988.0,
    583.0,
    1268.0000138282758,
    583.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    988.0,
    450.0,
    1268.0000138282758,
    450.0,
    fill="#FFFFFF",
    outline="")

# canvas.create_rectangle(
#     988.0,
#     630.0,
#     1268.0,
#     680.0,
#     fill="#12480E",
#     outline="")

# canvas.create_text(
#     988.0,
#     640.0,
#     anchor="nw",
#     text="                  Login",
#     fill="#FFFFFF",
#     font=("OpenSansHebrewCondensed Bold", 20 * -1)
# )

def regis(name, username, password):
    with open("C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\logindatabase.txt", "a") as file:
        file.write("\n" + name + "," + username + "," + password)
        
window.resizable(False, False)
window.mainloop()