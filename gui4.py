
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\jasmi\Downloads\VISKOM VSCODE\UAS\main\assets\frame4")


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

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    850.0,
    450.0,
    image=image_image_2
)

canvas.create_rectangle(
    640.0,
    0.0,
    800.0,
    1024.0,
    fill="#000000",
    outline="")

canvas.create_text(
    945.0,
    130.0,
    anchor="nw",
    text="Regis Your Face",
    fill="#FFFFFF",
    font=("OpenSansHebrewCondensed Bold", 50 * -1)
)

canvas.create_rectangle(
    988.0,
    534.0,
    1268.0,
    567.0,
    fill="#000000",
    outline="")


text_next_ang = canvas.create_rectangle(
    988.0,
    669.0,
    1268.0,
    719.0,
    fill="#12480E",
    outline="")

canvas.create_text(
    1080.0,
    680.0,
    anchor="nw",
    text="     Next ",
    fill="#FFFFFF",
    font=("OpenSansHebrewCondensed Bold", 20 * -1)
)

canvas.create_rectangle(
    1230.0,
    365.0,
    1267.5,
    402.5,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1105.0,
    599.0,
    1155.0,
    649.0,
    fill="#000000",
    outline="")

canvas.create_rectangle( #kiri atas hori
    911.0,
    250.0,
    996.0,
    255.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kiri atas ver
    911.0,
    250.0,
    916.0,
    350.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kiri bawah vert
    915.9162877723575,
    550.0,
    921.0,
    650.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kiri bawah hor
    916,
    650,
    996.9999570846558,
    655,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kanan bawah hor
    1255.0000095367432,
    650,
    1340.0,
    655,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kanan bawah ver
    1334.9620094355196,
    550.0,
    1340.001953125,
    650.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kanan atas ver
    1335.0,
    250,
    1340.0011952585191,
    350,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kanan atas hor
    1254.0,
    250,
    1339.0,
    255,
    fill="#FFFFFF",
    outline="")

canvas.tag_bind(text_next_ang, "<Button-1>", lambda event: handle_next_angle())

def handle_next_angle():
    # Logika untuk menangani klik pada tombol Registration
    print("Navigating to registration page")
    window.quit()
    window.destroy()
    subprocess.run(["python", "C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\gui5.py"])
    
def on_enter_ang(event):
  canvas.itemconfig(text_next_ang, fill="#0D350A")
  
def on_leave_ang(event):
  canvas.itemconfig(text_next_ang, fill="#12480E")
    
canvas.tag_bind(text_next_ang, "<Enter>", on_enter_ang)
canvas.tag_bind(text_next_ang, "<Leave>", on_leave_ang)

window.resizable(False, False)
window.mainloop()
