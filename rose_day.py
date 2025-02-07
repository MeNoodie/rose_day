
import tkinter as tk
from tkinter import Label, Button, Toplevel
from PIL import Image, ImageTk, ImageDraw
import cv2
import os

# Create main window using Tkinter
root = tk.Tk()
root.title("Happy Rose Day 🌹")
root.geometry("600x700")
root.resizable(False, False)
root.configure(bg="#ffebee")  # Light pink background 

# here i add background image 
bg_img = Image.open(r"C:\Users\piyus\Downloads\Festival Backdrops Valentine Day Backdrops Inexpensive Photo Backdrops.jpg")
bg_img = bg_img.resize((600, 700), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Full-screen background

# Load Video
video_path = r"C:\Users\piyus\Downloads\jump-bear.mp4"
cap = cv2.VideoCapture(video_path)

# Video Display Label
video_label = Label(root, bg="black", bd=5, relief="ridge")
video_label.pack(pady=20)

# Function to play the video
def play_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (250, 250))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(img)
        video_label.config(image=img_tk)
        video_label.image = img_tk
        root.after(100, play_video)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        root.after(30, play_video)

# create a Message Section and add some text with emojis 
message_label = Label(root, text="🌹 Happy Rose Day! 🌹",
                      font=("Comic Sans MS", 20, "bold"), bg="white", fg="red", pady=10, bd=5, relief="solid")
message_label.pack(pady=10)

sub_message = Label(root, text="I wonder, do you still have the delicate flower I plucked just for you? ❤️",
                    font=("Arial", 14, "italic"), bg="white", fg="black", wraplength=500)
sub_message.pack(pady=5)

# Create a Heart Icon ( i took help from internet to draw this heart shape)
heart_size = (80, 80)
red_heart = Image.new("RGBA", heart_size, (255, 255, 255, 0))
draw = ImageDraw.Draw(red_heart)

# Draw a heart shape
heart_points = [(40, 20), (20, 10), (10, 20), (10, 40), (40, 70), (70, 40), (70, 20), (60, 10), (40, 20)]
draw.polygon(heart_points, fill="red")
red_heart = ImageTk.PhotoImage(red_heart)

# Create a second heart (gray)
gray_heart = Image.new("RGBA", heart_size, (255, 255, 255, 0))
draw = ImageDraw.Draw(gray_heart)
draw.polygon(heart_points, fill="gray")
gray_heart = ImageTk.PhotoImage(gray_heart)

# Heart Click Event
heart_clicked = False
def toggle_heart():
    global heart_clicked
    heart_clicked = not heart_clicked
    heart_label.config(image=red_heart if heart_clicked else gray_heart)

# Heart Button
heart_label = Label(root, image=gray_heart, bg="#ffebee", cursor="hand2")
heart_label.pack(pady=10)
heart_label.bind("<Button-1>", lambda e: toggle_heart())

# Here I Add video of rose
rose_video_path = r"C:\Users\piyus\Downloads\red-rose.mp4"
rose_cap = cv2.VideoCapture(rose_video_path)
rose_video_label = None

# Function to play rose video in second popup
def play_rose_video():
    global rose_video_label
    ret, frame = rose_cap.read()
    if ret:
        frame = cv2.resize(frame, (300, 300))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(img)
        rose_video_label.config(image=img_tk)
        rose_video_label.image = img_tk
        rose_video_label.after(50, play_rose_video)
    else:
        rose_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        rose_video_label.after(50, play_rose_video)

# Function for second popup
def show_second_popup():
    global rose_video_label
    second_popup = Toplevel(root)
    second_popup.title("🌹 Happy Rose Day! 🌹")
    second_popup.geometry("500x500")
    second_popup.configure(bg="pink")

    # Video Label
    rose_video_label = Label(second_popup, bg="black", bd=5, relief="ridge")
    rose_video_label.pack(pady=10)

    # Start Video
    play_rose_video()

    # Text
    text_label = Label(second_popup, text="🌹 Happy Rose Day! 🌹", 
                       font=("Comic Sans MS", 16, "bold"), bg="white", fg="red", pady=10, bd=5, relief="solid")
    text_label.pack(pady=20)

    # Close Button
    close_btn = Button(second_popup, text="Close", command=second_popup.destroy,
                       font=("Arial", 12, "bold"), bg="red", fg="white", padx=10, pady=5, bd=3, relief="raised")
    close_btn.pack(pady=10)

# Function for first popup
def show_surprise():
    popup = Toplevel(root)
    popup.title("💖 A Special Message for You! 💖")
    popup.geometry("500x300")
    popup.configure(bg="pink")

    msg_label = Label(popup, text="My world turned upside down the moment I met you🌷💖", 
                      font=("Comic Sans MS", 14, "bold"), bg="white", fg="red", wraplength=350, bd=5, relief="solid")
    msg_label.pack(pady=20)

    # Close Button opens second popup
    close_btn = Button(popup, text="💗 BAKA 💗", command=lambda: [popup.destroy(), show_second_popup()],
                       font=("Arial", 12, "bold"), bg="#ff4d4d", fg="white", padx=10, pady=5, bd=3, relief="raised")
    close_btn.pack(pady=10)

# Fancy Button
btn = Button(root, text="💖 Click for a Special Message 💖", command=show_surprise,
             font=("Arial", 14, "bold"), bg="#ff1744", fg="white", padx=10, pady=5, bd=3, relief="raised")
btn.pack(pady=20)

# Run the video function
play_video()

# Run the application
root.mainloop()

# Release video capture when app is closed
cap.release()
rose_cap.release()
