import os
import tkinter as tk
from PIL import Image, ImageTk

def toggle_selection(image_index):
    # Toggle the selection status of the image at the specified index
    selected_images[image_index] = not selected_images[image_index]

def submit(password_entry, auth_label):
    # Check if the first and second images are selected and if the password is correct
    if selected_images[0] and selected_images[1] and password_entry.get() == "password":
        auth_label.config(text="User Authenticated")
    else:
        auth_label.config(text="Incorrect Password or Images not selected")

def display_images():
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Image Password Authentication")
    current_dir =os.path.dirname(__file__);
    assetsipa_dir=os.path.join(current_dir,"assetsipa");

    # Specify the file names of images
    file_names = ["images.jpeg", "Isaiah 60 22 (copy).jpeg", "image2.jpeg", "image3.jpg","todo.jpg"]

    # Initialize a list to keep track of the selection status of each image
    global selected_images
    selected_images = [False] * len(file_names)

    # Create a frame for the grid of images
    image_frame = tk.Frame(root)
    image_frame.pack(pady=(10, 0))

    # Create a grid to display images with checkboxes
    for i, file_name in enumerate(file_names):
        # Construct the full path to the image file
        image_path = os.path.join(assetsipa_dir, file_name)

        # Open the image file
        image = Image.open(image_path)

        # Resize the image if needed (adjust size as necessary)
        image = image.resize((100, 100), Image.ANTIALIAS)

        # Create a Tkinter-compatible photo image
        photo = ImageTk.PhotoImage(image)

        # Create a label with the image
        label = tk.Label(image_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.grid(row=i // 5, column=i % 5, padx=5, pady=5)

        # Create a checkbox for the image
        checkbox = tk.Checkbutton(image_frame, command=lambda i=i: toggle_selection(i))
        checkbox.grid(row=(i // 5) + 1, column=i % 5, sticky="nw")

    # Create a frame for the text box, button, and authentication label
    input_frame = tk.Frame(root)
    input_frame.pack(pady=(10, 0))

    # Create a label for "Enter Password"
    password_label = tk.Label(input_frame, text="Enter Password:")
    password_label.grid(row=0, column=0, pady=(0, 5))

    # Create a text box
    password_entry = tk.Entry(input_frame, width=30)
    password_entry.grid(row=1, column=0, pady=(0, 5))

    # Create a button for submitting
    submit_button = tk.Button(input_frame, text="Submit", command=lambda: submit(password_entry, auth_label))
    submit_button.grid(row=2, column=0)

    # Create a label for authentication result
    auth_label = tk.Label(root, text="")
    auth_label.pack()

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    display_images()
