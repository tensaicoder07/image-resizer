import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter
from tkinter import simpledialog

# Username and password for authentication
users = {
    "Junaid_03": "JuNrViTm03",
    "Chandramadi_12": "cHaNdRuRvitM12",
    "Sriram_04": "SrIrViTm04",
    "123":"123"
}


# Global variables
original_image = None
resized_image = None

# Function for authentication
def authenticate():
    global original_image
    global resized_image

    # Ask for the username and password
    username = simpledialog.askstring("Authentication", "Enter username:")
    password = simpledialog.askstring("Authentication", "Enter password:", show='*')
    

    # Check if the provided username and password match
    if username in users:
        stored_password = users[username]

        # Check if the entered password matches the stored password
        if password == stored_password:
            # Enable widgets and continue with the application
            browse_button.config(state=tk.NORMAL)
            width_entry.config(state=tk.NORMAL)
            height_entry.config(state=tk.NORMAL)
            resize_button.config(state=tk.NORMAL)
            download_button.config(state=tk.DISABLED)
            result_label.config(text="")
        else:
            result_label.config(text="Authentication failed. Incorrect password.")
    
        
    else:
        # Incorrect credentials, show an error message
        result_label.config(text="Authentication failed. User not found.")

# Function to browse and display the image
def browse_image():
    global original_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg")])
    if file_path:
        image = Image.open(file_path)
        img_preview = ImageTk.PhotoImage(image)
        img_label.config(image=img_preview)
        img_label.image = img_preview
        original_image = image

# Function to resize the image
def resize_image():
    global resized_image
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        resized_image = original_image.resize((width, height), Image.BILINEAR)
        download_button.config(state=tk.NORMAL)
    except ValueError:
        result_label.config(text="Please enter valid dimensions")

# Function to download the resized image
def download_resized_image():
    if resized_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if file_path:
            resized_image.save(file_path)

# Create the main window
root = tk.Tk()
root.title("Image Resizer")

# Create and configure widgets
authenticate_button = tk.Button(root, text="Authenticate", command=authenticate)
browse_button = tk.Button(root, text="Upload Image", command=browse_image, state=tk.DISABLED)
width_label = tk.Label(root, text="Width:")
height_label = tk.Label(root, text="Height:")
width_entry = tk.Entry(root, state=tk.DISABLED)
height_entry = tk.Entry(root, state=tk.DISABLED)
resize_button = tk.Button(root, text="Resize", command=resize_image, state=tk.DISABLED)
img_label = tk.Label(root)
download_button = tk.Button(root, text="Download Resized Image", command=download_resized_image, state=tk.DISABLED)
result_label = tk.Label(root, text="")

# Place widgets on the grid


authenticate_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
browse_button.grid(row=1, column=0, padx=10, pady=10)
width_label.grid(row=2, column=0, padx=10, pady=10)
height_label.grid(row=3, column=0, padx=10, pady=10)
width_entry.grid(row=2, column=1, padx=10, pady=10)
height_entry.grid(row=3, column=1, padx=10, pady=10)
resize_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
img_label.grid(row=5, column=0, columnspan=2)
download_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=7, column=0, columnspan=2)




root.mainloop()
