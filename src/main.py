# Import Modules
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from os.path import isfile, exists, join, dirname
from os import listdir


# #######   All Function    #######
# Show Image
def show_image():
    global load_image
    global out_image
    global temp_image
    global out_image_width
    global out_image_height
    # print(images_path)  # Only For Dev
    temp_image = Image.open(join(images_path, filenames[current_image_number]))  # Open Current Image
    # Image Resize
    if temp_image.width < temp_image.height:
        # image Is Portrait
        new_width = (temp_image.width / temp_image.height) * out_image_height
        new_height = out_image_height
        # print("Portrait OLD : " + str(temp_image.width) + " / " + str(temp_image.height))  # Only For Dev
        # print("Portrait NEW : " + str(new_width) + " / " + str(new_height))  # Only For Dev
    else:
        # image Is Landscape
        if (temp_image.width / temp_image.height) < (out_image_width / out_image_height):
            new_width = (temp_image.width / temp_image.height) * out_image_height
            new_height = out_image_height
        else:
            new_width = out_image_width
            new_height = (temp_image.height / temp_image.width) * out_image_width
        # print("Landscape OLD : " + str(temp_image.width) + " / " + str(temp_image.height))  # Only For Dev
        # print("Landscape NEW : " + str(new_width) + " / " + str(new_height))  # Only For Dev
    load_image = ImageTk.PhotoImage(temp_image.resize((int(new_width), int(new_height))))  # Load Image
    out_image.grid_forget()  # Remove Old Label
    out_image = Label(image=load_image)  # Set Image To Label
    # Get Auto Padding For 'X' & 'Y' Axis
    lable_pady = (out_image_height - new_height) / 2
    lable_padx = (out_image_width - new_width) / 2
    out_image.grid(row=0, column=0, columnspan=3, padx=lable_padx, pady=lable_pady)  # Show Label
    # enter the padding value at the specified position, and leave the remaining as zero.
    # It will give the padding to a widget from one side only,
    # grid(padx=(padding from left side, padding from right side), pady=(padding from top, padding from bottom))


# On Click Back Button
def back_button():
    global current_image_number
    if current_image_number == 0:  # If CIN Is 0
        current_image_number = len(filenames) - 1  # Show From Last
    else:
        current_image_number = current_image_number - 1  # Show Previous Image
    show_image()  # Call Show Image


# On Click Forward Button
def forward_button():
    global current_image_number
    if current_image_number == len(filenames) - 1:  # If CIN Is == Total Image Files
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
    global images_path
    if exists(images_path):  # Is Directory Exists
        for file in listdir(images_path):  # Fetch All
            if file.endswith(".png") or file.endswith(".jpg"):  # Filter Image File Type
                filenames.append(file)  # Push Into 'filenames'


def open_button():
    global images_path
    global filenames
    global current_image_number
    current_image_number = 0  # Show From Start
    temp_var = select_dir()  # Open File Explorer & Get Folder Select By User
    if temp_var:
        images_path = temp_var  # Set Images Path
        filenames = []  # Clean List For New Files
        get_all_image_files()
        show_image()


# Auto Center Window
def auto_center():
    global root_width
    global root_height
    # Get Screen Width & Height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Get 'X' & 'Y' Position Of Window
    x_position = int(screen_width / 2) - int(root_width / 2)
    y_position = int(screen_height / 2) - int(root_height / 2)
    # Return Calculated Center Geometry
    return str(root_width) + "x" + str(root_height) + "+" + str(x_position) + "+" + str(y_position)


# Windows SetUp
root = Tk()
root.title("Image Viewer 17-06-2021")  # Set Title Of Window
# Set Root Window Width & Height
root_width = 1000
root_height = 630
# Get Geometry
root_geometry = auto_center()
# parent_window.geometry("width_size x height_size + x_position + y_position")
root.geometry(root_geometry)  # Set Window Geometry
root.resizable(0, 0)  # Stop Resize The Window

# If ICON Available
if isfile("assets/icon.ico"):
    root.iconbitmap("assets/icon.ico")  # Set Window ICON

# All Global Variable
out_image_width = 990  # Out Image Width
out_image_height = 600  # Out Image Height
images_path = select_dir()  # Get Images Path
current_image_number = 0  # Current Showing Image Number
filenames = []  # To Store All Image Files
get_all_image_files()  # Get All Image From Image Folder

# UI Designing
# Create Image Path And Load Image Before Used
base_path = dirname(__file__)  # Get Software Base Path
load_image = ImageTk.PhotoImage(Image.open(join(base_path, "assets/images/empty.png")))  # Get Image
out_image = Label(image=load_image, width=1000, height=600)  # Set Image To Label
out_image.grid(row=0, column=0, columnspan=3)

# If User Select Any folder
if images_path:
    show_image()  # Call Show Image

# Get All Icon For Buttons
temp_image = Image.open(join(dirname(__file__), "assets/images/previous.png"))  # Get Image
back_image = ImageTk.PhotoImage(temp_image.resize((30, 20)))  # Resize And Set Image To Button

temp_image = Image.open(join(dirname(__file__), "assets/images/open.png"))  # Get Image
open_image = ImageTk.PhotoImage(temp_image.resize((30, 20)))  # Resize And Set Image To Button

temp_image = Image.open(join(dirname(__file__), "assets/images/next.png"))  # Get Image
forward_image = ImageTk.PhotoImage(temp_image.resize((30, 20)))  # Resize And Set Image To Button

# Define Buttons
button_back = Button(root, text="<<", image=back_image, command=back_button)  # Define Back Button
button_open = Button(root, text="OPEN", image=open_image, command=open_button)  # Define Open Button
button_forward = Button(root, text=">>", image=forward_image, command=forward_button)  # Define Forward Button

# Put Buttons On Screen
button_back.grid(row=1, column=0, padx="149")  # Show Back
button_open.grid(row=1, column=1, padx="149")  # Show Open
button_forward.grid(row=1, column=2, padx="149")  # Show Forward

root.mainloop()
