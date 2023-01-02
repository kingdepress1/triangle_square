import math
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Triangle Area Calculator")

def calculate_triangle_area():
    # Get the base and height of the triangle from the input fields
    base = base_entry.get()
    height = height_entry.get()
    hypotenuse = hypotenuse_entry.get()
    summ = [base, height, hypotenuse]
    tech = True




    base = float(base)
    height = float(height)
    hypotenuse = float(hypotenuse)




    p = (base + height + hypotenuse)/2
    area = math.sqrt(p*(p-base)*(p-height)*(p-hypotenuse))
    result_label.config(text=f"Triangle Area Is: {area:.2f} \n ")



frame = tk.Frame(master=window, width=150, height=120)
frame.pack(fill=tk.Y, side=tk.LEFT)

frame1 = tk.Frame(master=window, width=150, height=120, bg="white")
frame1.pack(fill=tk.Y, side=tk.LEFT)


img= (Image.open("triangle.png"))
resized_image= img.resize((300,250), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)


label_img = Label(frame1, image = new_image)
label_img.pack()

result_label = tk.Label(frame1, text="", bg = "white")
result_label.place(x=120, y=10)

instruct_label = tk.Label(text="put in empty two fields a \n  triangles anytwo sides size")
instruct_label.place(x=5, y=5)


base_label = tk.Label(text="Base:")
base_label.place(x=5, y=40)
base_entry = tk.Entry(width=10)
base_entry.place(x=80, y=40)

height_label = tk.Label(text="Height:")
height_label.place(x=5, y=70)
height_entry = tk.Entry(width=10)
height_entry.place(x=80, y=70)

hypotenuse_label = tk.Label(text="hypotenuse:")
hypotenuse_label.place(x=5, y=100)
hypotenuse_entry = tk.Entry(width=10)
hypotenuse_entry.place(x=80, y=100)

calculate_button = tk.Button(text="Calculate", command=calculate_triangle_area)
calculate_button.place(x=40, y=130)





window.mainloop()