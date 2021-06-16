# Import Modules
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from os.path import isfile, exists, join, dirname
from os import listdir


# All Function
# Show Image
def show_image():
    global load_image
    global out_image
    # global current_image_number
    # global images_path
    # Create Image Path And Load Image Before Used
    load_image = ImageTk.PhotoImage(Image.open(join(images_path, filenames[current_image_number])))
    out_image.grid_forget()
    out_image = Label(image=load_image, width=1000, height=600)
    out_image.grid(row=0, column=0, columnspan=3)


# On Click Back Button
def back_button():
    # Get Access Of Global Variable
    global current_image_number
    if current_image_number == 0:  # If CIN Is 0
        current_image_number = len(filenames) - 1  # Show From Last
    else:
        current_image_number = current_image_number - 1  # Show Previous Image
    show_image()  # Call Show Image


# On Click Forward Button
def forward_button():
    # Get Access Of Global Variable
    global current_image_number
    if current_image_number == len(filenames) - 1:  # If CIN Is == Total Files
        current_image_number = 0  # Show From Start
    else:
        current_image_number = current_image_number + 1  # Show Next Image
    show_image()  # Call Show Image


# Select Directory
# Open Explorer And Chose Directory To View Images
def select_dir():
    return filedialog.askdirectory()


# Get All Image Files From A Folder
def get_all_image_files():
    # Get Access Of Global Variable
    global images_path
    # Loop Until Get Proper Directory
    # temp = 1
    # while temp:
    if exists(images_path):  # Is Directory Exists
        for file in listdir(images_path):  # Fetch All
            if file.endswith(".png") or file.endswith(".jpg"):  # Filter File Type
                filenames.append(file)  # Push Into 'filenames'

    else:
        # Load Empty Icon
        images_path = dirname(__file__)
        filenames.append("assets/images/empty.png")
        # images_path = select_dir()  # Again Fetch Directory


def open_button():
    # Get Access Of Global Variable
    global images_path
    global filenames
    global current_image_number
    current_image_number = 0  # Show From Start
    temp_var = select_dir()
    if temp_var:
        images_path = temp_var  # Get Images Path
        filenames = []  # Clean List For New Files
        get_all_image_files()
        show_image()


# Auto Center Window
def auto_center():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root_width = 1000
    root_height = 630
    x_position = int(screen_width / 2) - int(root_width / 2)
    y_position = int(screen_height / 2) - int(root_height / 2)
    return str(root_width) + "x" + str(root_height) + "+" + str(x_position) + "+" + str(y_position)


# Windows SetUp
root = Tk()
root.title("Image Viewer 16-06-2021")
# Get Geometry
root_geometry = auto_center()
# parent_window.geometry("width_size x height_size + x_position + y_position")
root.geometry(root_geometry)
root.resizable(0, 0)
if isfile("icon.ico"):
    root.iconbitmap("icon.ico")

# All Global Variable
images_path = select_dir()  # Get Images Path
current_image_number = 0  # Current Showing Image Number
filenames = []  # To Store All Image Files
get_all_image_files()  # Get All Image From Image Folder

# UI Designing
# Create Image Path And Load Image Before Used
load_image = ImageTk.PhotoImage(Image.open(join(images_path, filenames[current_image_number])))  # Default Image
out_image = Label(image=load_image, width=1000, height=600)  # Set Image To Label
if images_path:
    show_image()
else:
    out_image.grid(row=0, column=0, columnspan=4)

# Get All Icon For Buttons
temp_image = Image.open(join(dirname(__file__), "assets/images/previous.png"))
back_image = ImageTk.PhotoImage(temp_image.resize((30, 20)))

temp_image = Image.open(join(dirname(__file__), "assets/images/open.png"))
open_image = ImageTk.PhotoImage(temp_image.resize((30, 20)))

temp_image = Image.open(join(dirname(__file__), "assets/images/next.png"))
forward_image = ImageTk.PhotoImage(temp_image.resize((30, 20)))

# Define Buttons
button_back = Button(root, text="<<", image=back_image, command=back_button)
# button_exit = Button(root, text="EXIT", command=root.quit)
button_open = Button(root, text="OPEN", image=open_image, command=open_button)
button_forward = Button(root, text=">>", image=forward_image, command=forward_button)

# Put Buttons On Screen
button_back.grid(row=1, column=0)
# button_exit.grid(row=1, column=1)
button_open.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()

# sticky = N+S+E+W can stretched the widgets
# Anchor = N/S/E/W
