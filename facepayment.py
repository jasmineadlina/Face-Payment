
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import json
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\jasmi\Downloads\VISKOM VSCODE\UAS\main\assets\frame10")

match_found = False  # Variabel flag untuk menandai kecocokan gambar
user_data = None  # Define user_data as a global variable
matching_images_count = 0

def read_user_data():
    global user_data
    try:
        with open("userdata.json", "r") as user_file:
            user_data = json.load(user_file)
            if user_data:
                print(f"Yang sedang login adalah {user_data[0]},{user_data[1]},{user_data[2]}.")
            else:
                print("Data pengguna kosong.")
    except FileNotFoundError:
        print("File userdata.json tidak ditemukan.")
        
read_user_data()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_webcam():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  # Use DirectShow as the backend
    if not cap.isOpened():
        print("Camera not accessible")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 20)
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def update():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)

            canvas.img = img
            canvas.create_image(390, 220, anchor=tk.NW, image=img)

        window.after(10, update)

    update()

def compare_images():
    global user_data, match_found, matching_images_count

    # Load Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Get paths for 4 image files to be compared
    file_names = [f"C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\{user_data[0]},{user_data[1]},{user_data[2]}_angle{i}.jpg" for i in range(1, 5)]

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Use DirectShow as the backend
    ret, frame = cap.read()
    if not ret:
        print("Camera not accessible")
        return

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("No faces detected in the captured frame.")
        return

    # Extract the first detected face
    x, y, w, h = faces[0]

    for file_name in file_names:
        saved_image = cv2.imread(file_name)
        saved_image_gray = cv2.cvtColor(saved_image, cv2.COLOR_BGR2GRAY)

        # Resize the saved image to match the dimensions of the webcam frame
        saved_image_gray = cv2.resize(saved_image_gray, (w, h))

        # Detect faces in the resized saved image
        saved_faces = face_cascade.detectMultiScale(saved_image_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(saved_faces) == 0:
            print(f"No faces detected in the saved image: {file_name}")
            continue

        # Calculate structural similarity
        similarity_index, _ = compare_ssim(gray_frame[y:y+h, x:x+w], saved_image_gray, full=True)

        print(f"Similarity index for {file_name}: {similarity_index}")

        # Set threshold for similarity
        if similarity_index > 0.2:  # Adjust threshold as needed
            print(f"Match found with {file_name}")
            matching_images_count += 1
            if matching_images_count >= 4:  # Change to greater than or equal to
                match_found = True
                break  # Break immediately when a match is found

    if match_found:
        print("Face recognition successful!")
    else:
        print("Face recognition failed. Please try again.")
        open_webcam()

window = Tk()
window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")

canvas = Canvas(window, width=10, height=20)
canvas.pack()    
open_webcam()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    500.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    749.0,
    1459.0,
    1024.0,
    fill="#000000",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    720.0,
    410.0,
    image=image_image_2
)

canvas.create_text(
    590.0,
    125.0,
    anchor="nw",
    text="Scan Here",
    fill="#FFFFFF",
    font=("OpenSansHebrewCondensed Bold", 50 * -1)
)

scan = canvas.create_rectangle(
    560.0,
    635.0,
    860.0,
    685.0,
    fill="#12480E",
    outline="")

canvas.tag_bind(scan, "<Button-1>", lambda event: handle_scan_click())


def handle_scan_click():
    global user_data, match_found
    if user_data:  # Check if user_data is populated
        compare_images()  # Remove the 'user_data' argument here
        if match_found:
            print("Face recognition successful!")
            window.quit()
            window.destroy()
            subprocess.run(["python", "C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\7_HomePage copy.py"])
        else:
            print("Face recognition failed. Please try again.")
            open_webcam()
    else:
        print("User data is not available.")
        
def on_enter_scan(event):
    canvas.itemconfig(scan, fill="#0D350A")

def on_leave_scan(event):
  canvas.itemconfig(scan, fill="#12480E")
  
canvas.tag_bind(scan, "<Enter>", on_enter_scan)
canvas.tag_bind(scan, "<Leave>", on_leave_scan)

canvas.create_text(
    680.0,
    648.0,
    anchor="nw",
    text=" Scan",
    fill="#FFFFFF",
    font=("OpenSansHebrewCondensed Bold", 20 * -1)
)

move_to_cart = canvas.create_rectangle(
    1305.0,
    56.0,
    1368.0,
    112.0,
    fill="#000000",
    outline="")

canvas.tag_bind(move_to_cart, "<Button-1>", lambda event: handle_move_to_cart_click())

def handle_move_to_cart_click():
    # Logika untuk menangani klik pada tombol Registration
    print("Navigating to registration page")
    window.quit()
    window.destroy()
    subprocess.run(["python", "C:\\Users\\jasmi\\Downloads\\VISKOM VSCODE\\UAS\\main\\cart.py"])
    
def on_enter_move_to_cart(event):
    canvas.itemconfig(move_to_cart, fill="#0D350A")

def on_leave_move_to_cart(event):
  canvas.itemconfig(move_to_cart, fill="#000000")
  
canvas.tag_bind(move_to_cart, "<Enter>", on_enter_move_to_cart)
canvas.tag_bind(move_to_cart, "<Leave>", on_leave_move_to_cart)

canvas.create_rectangle(
    0.0,
    50.0,
    100.0,
    100.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    75.0,
    50.0,
    125.0,
    100.0,
    fill="#000000",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1337.0,
    84.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    55.0,
    75.0,
    image=image_image_5
)

# image_image_6 = PhotoImage(
#     file=relative_to_assets("image_6.png"))
# image_6 = canvas.create_image(
#     720.0,
#     402.0,
#     image=image_image_6
# )
    
window.resizable(False, False)
window.mainloop()
