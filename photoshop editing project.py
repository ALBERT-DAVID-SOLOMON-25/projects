from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance, ImageFilter

root = Tk()
root.title("Mini Photoshop - Python")
root.geometry("900x600")
root.config(bg="#2c2c2c")
img = None
img_display = None
file_path = None

def open_image():
    global img, img_display, file_path
    file_path = filedialog.askopenfilename(
        title="Open Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        show_image(img)

def show_image(im):
    global img_display
    im.thumbnail((400, 400))
    tk_img = ImageTk.PhotoImage(im)
    lbl_image.config(image=tk_img)
    lbl_image.image = tk_img

def save_image():
    global img
    if img:
        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("All files", "*.*")]
        )
        if save_path:
            img.save(save_path)
            messagebox.showinfo("Saved", "Image saved successfully!")
    else:
        messagebox.showwarning("Warning", "No image to save!")

def rotate_left():
    global img
    if img:
        img = img.rotate(90, expand=True)
        show_image(img)

def rotate_right():
    global img
    if img:
        img = img.rotate(-90, expand=True)
        show_image(img)

def blur_image():
    global img
    if img:
        img = img.filter(ImageFilter.BLUR)
        show_image(img)

def brighten():
    global img
    if img:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.5)
        show_image(img)

def darken():
    global img
    if img:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0.5)
        show_image(img)

def grayscale():
    global img
    if img:
        img = img.convert("L")
        show_image(img)


Label(root, text="Mini Photoshop", fg="white", bg="#2c2c2c", font=("Arial", 22, "bold")).pack(pady=10)

frame = Frame(root, bg="#2c2c2c")
frame.pack()

lbl_image = Label(frame, bg="#1e1e1e")
lbl_image.pack(padx=20, pady=20)

btn_frame = Frame(root, bg="#2c2c2c")
btn_frame.pack(pady=10)

Button(btn_frame, text="Open", width=10, command=open_image).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Save", width=10, command=save_image).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Rotate ⬅️", width=10, command=rotate_left).grid(row=0, column=2, padx=5)
Button(btn_frame, text="Rotate ➡️", width=10, command=rotate_right).grid(row=0, column=3, padx=5)
Button(btn_frame, text="Blur", width=10, command=blur_image).grid(row=0, column=4, padx=5)
Button(btn_frame, text="Brighten", width=10, command=brighten).grid(row=0, column=5, padx=5)
Button(btn_frame, text="Darken", width=10, command=darken).grid(row=0, column=6, padx=5)
Button(btn_frame, text="Grayscale", width=10, command=grayscale).grid(row=0, column=7, padx=5)

root.mainloop()
