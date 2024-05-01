import tkinter
import threading
import customtkinter
from pytube import YouTube

# Constants
url_var = ""
download_thread = None

# Functions


def download():
    global download_thread
    download_label.configure(text="downloading...", text_color="white")
    try:
        url = link.get()
        if download_thread is None or not download_thread.is_alive():
            download_thread = threading.Thread(
                target=download_video, args=(url,))
            download_thread.start()
        else:
            download_label.configure(
                text="Download already in progress", text_color="orange")
    except Exception as e:
        download_label.configure(text=e, text_color="red")


def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        download_label.configure(
            text="Download Completed!", text_color="green")
        title.configure(text=f"Video: - {yt.title} - Successfully downloaded.", text_color="green")
    except Exception as e:
        download_label.configure(text=e, text_color="red")



# system settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("700x350")

# UI Elements
# Title
title = customtkinter.CTkLabel(
    app, text="JAM WebDev YouTube Downloader", font=("Arial", 24))
title.pack(pady=40)

# Search input
link = customtkinter.CTkEntry(
    app, placeholder_text="Paste YouTube Link Here", width=500, height=25, textvariable=url_var)
link.pack(pady=20)

# Download status text
download_label = customtkinter.CTkLabel(app, text="", font=("Arial", 14))
download_label.pack()

# Download button
download_button = customtkinter.CTkButton(
    app, text="Download", command=download)
download_button.pack(pady=20)


# Run app
app.mainloop()
