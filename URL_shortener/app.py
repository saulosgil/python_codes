# URL Shortener
# Libraries
import pyshorteners
import tkinter as tk

# function to short URL
def shorten_url():
    url = url_entry.get()
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    shortened_url_label.config(text=shortened_url)

# GUI
root = tk.Tk()
root.title("ENCURTADOR DE URL")
root.geometry("600x150")

url_label = tk.Label(root, text="Insira a URL")
url_label.pack()
url_label.config(font=("Arial", 12))

url_entry = tk.Entry(root)
url_entry.config(width=75, borderwidth=2)
url_entry.pack()

shorten_button = tk.Button(root, text="Encurte", command=shorten_url)
shorten_button.config(font=("Arial", 12))   
shorten_button.pack()

shortened_url_label = tk.Label(root, text="")
shortened_url_label.config(font=("Arial", 12))  
shortened_url_label.pack()

root.mainloop()