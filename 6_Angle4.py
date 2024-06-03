
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import cv2
import tkinter as tk
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\assets\\frame4"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Kamera tidak dapat diakses")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 280)
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def update():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)

            canvas.img = img
            canvas.create_image(750, 280, anchor=tk.NW, image=img)

        window.after(10, update)

    update()

def handle_done():
    username = None
    with open("C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\logindatabase.txt", "r") as file:
        lines = file.readlines()
        if lines:
            username = lines[-1].strip()

    if username:
        folder_path = "C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\"
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Kamera tidak dapat diakses")
            return

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 280)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while True:
            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                if len(faces) == 1:
                    x, y, w, h = faces[0]  # Ambil koordinat wajah yang terdeteksi
                    cropped_face = frame[y:y+h, x:x+w]  # Crop bagian wajah

                    # Simpan wajah yang di-crop
                    filename = f"{folder_path}{username}_angle4.jpg"
                    cv2.imwrite(filename, cropped_face)
                    print(f"Wajah yang terdeteksi disimpan sebagai {filename}")
                    break

            cv2.waitKey(10)

        cap.release()
        cv2.destroyAllWindows()

        window.quit()
        window.destroy()
        subprocess.run(["python", "C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\1_Login.py"])

def on_enter_ang(event):
  canvas.itemconfig(done, fill="#0D350A")
  
def on_leave_ang(event):
  canvas.itemconfig(done, fill="#12480E")

window = Tk()
window.geometry("1440x1024")
window.configure(bg="#000000")

canvas = Canvas(window, width=400, height=400)
canvas.pack()

open_webcam()

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


done = canvas.create_rectangle(
    970.0,
    669.0,
    1200.0,
    719.0,
    fill="#12480E",
    outline="")

canvas.create_text(
    1060.0,
    680.0,
    anchor="nw",
    text="Done ",
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
    715.0,
    240.0,
    820.0,
    245.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kiri atas ver
    710.0,
    240.0,
    715.0,
    355.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kiri bawah vert
    710.0,
    550.0,
    715.0,
    675.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kiri bawah hor
    715,
    670,
    820,
    675,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kanan bawah hor
    1320,
    670,
    1430.0,
    675,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kanan bawah ver
    1425,
    560.0,
    1430,
    670.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kanan atas ver
    1425.0,
    250,
    1430,
    350,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle( #kanan atas hor
    1320.0,
    250,
    1430.0,
    255,
    fill="#FFFFFF",
    outline="")

canvas.tag_bind(done, "<Button-1>", lambda event: handle_done())    
canvas.tag_bind(done, "<Enter>", on_enter_ang)
canvas.tag_bind(done, "<Leave>", on_leave_ang)

window.resizable(False, False)
window.mainloop()
