import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Function to download video
def download_video():
    url = entry.get()  # Get URL from the input box
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return

    try:
        # Download video
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        video.download()  # Download the video
        messagebox.showinfo("Success", f"Downloaded: {yt.title}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Create the GUI
root = tk.Tk()
root.title("YouTube Video Downloader")

# Input Label
label = tk.Label(root, text="Enter YouTube URL:")
label.pack(pady=10)

# URL Input
entry = tk.Entry(root, width=50)
entry.pack(padx=10)

# Download Button
button = tk.Button(root, text="Download", command=download_video)
button.pack(pady=20)

# Run the GUI
root.mainloop()
