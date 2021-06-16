from tkinter import *
from PIL import ImageTk, Image
from os.path import isfile, exists, join, dirname

root = Tk()
root.title("Image Viewer ORG")
temp_image = Image.open(join(dirname(__file__), "previous.png"))
new_height = 4
new_width = int(new_height / temp_image.height * temp_image.width)
print(str(new_width) + " / " + str(new_height))
temp_out = temp_image.resize((new_width, new_height))
back_image = ImageTk.PhotoImage(temp_out)
button_back = Button(root, text="<<", image=back_image)
button_back.grid(row=1, column=0)
root.mainloop()
