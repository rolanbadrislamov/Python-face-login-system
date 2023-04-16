from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import ath
import os
import sys
import admin
from PIL import Image, ImageTk


def main():

    def check_main():

        root = Tk()
        root.title("Verified")
        root.geometry('280x280')

        gif_image = Image.open('images/check.gif')

        global frames
        global tk_frames
        frames = []
        try:
            while True:
                frames.append(gif_image.copy())
                gif_image.seek(len(frames))
        except EOFError:
            pass

            tk_frames = [ImageTk.PhotoImage(frame) for frame in frames]

        label = Label(root, image=tk_frames[0])
        label.frames = tk_frames
        label.pack()

        def animate(frame_index):
            label.configure(image=tk_frames[frame_index])
            root.after(50, animate, (frame_index + 1) % len(tk_frames))

        animate(0)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - 150
        y = (screen_height // 2) - 150

        root.geometry(f"280x280+{x}+{y}")

        def on_closing():
            sys.exit()

        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()

    gif_image = Image.open('images/check.gif')
    gif_image2 = Image.open('images/cross.gif')

    if not os.path.exists('users.txt'):
        with open('users.txt', 'w') as file:
            file.write('')

    if not os.path.exists('pics'):
        os.makedirs('pics')

    def on_enter(event):
        if usernameEntry.get() == '      Username':
            usernameEntry.delete(0, END)

    def on_enter2(event):
        if passwordEntry.get() == '      Password':
            passwordEntry.delete(0, END)

    def hide():
        openEye.config(file='images/close-eye.png')
        passwordEntry.config(show="*")
        buttonEye.config(command=show)

    def show():
        openEye.config(file="images/eye-open.png")
        passwordEntry.config(show="")
        buttonEye.config(command=hide)

    def login_function():
        filename = usernameEntry.get()
        foldername = "pics"
        filename = foldername + f"/{filename}" + ".jpg"
        # Open the text file containing usernames and passwords
        if usernameEntry.get() == 'admin' and passwordEntry.get() == '12345':
            login.destroy()
            admin.main()

        with open('users.txt', 'r') as file:
            for line in file:

                user, pw = line.strip().split(',')

                if user == usernameEntry.get() and pw == passwordEntry.get():
                    login.destroy()
                    ath.main()

            messagebox.showerror('Error', 'NO USER FOUND')

    if not os.path.exists('users.txt'):
        with open('users.txt', 'w') as file:
            file.write('')

    login = Tk()
    login.title("Login")
    login.resizable(False, False)
    login.geometry('600x600+300+50')
    bg = ImageTk.PhotoImage(file='images/bg.png')
    bgLabel = Label(login, image=bg)
    bgLabel.place(x=-2, y=0)
    heading = Label(login, text='USER LOGIN', font=("Cascadia code", 23, 'bold'),
                    bg='#e7a1a1')
    heading.place(x=208, y=170)

    usernameEntry = Entry(login, width=20, font=("Cascadia code", 16, 'bold'),
                          bg='#EDBFBF')

    usernameEntry.place(x=180, y=300)
    usernameEntry.insert(0, '      Username')
    usernameEntry.bind("<FocusIn>", on_enter)

    passwordEntry = Entry(login, width=20, font=("Cascadia code", 16, 'bold'),
                          bg='#EDBFBF')
    passwordEntry.place(x=180, y=360)
    passwordEntry.insert(0, '')
    passwordEntry.bind("<FocusIn>", on_enter2)

    Frame(login, width=243, height=2, bg='black').place(x=180, y=330)
    Frame(login, width=243, height=2, bg='black').place(x=180, y=391)

    copyright = Label(login, text='©Rolan Badrislamov', font=("Copperplate Gothic", 18, 'bold'),
                          bg='#e7a1a1', fg='#FFF2F2')
    copyright.place(x=45, y=540)

    openEye = PhotoImage(file='images/eye-open.png')
    buttonEye = Button(login, image=openEye, bd=0, bg='#EDBFBF',
                       cursor='hand2', command=hide)
    buttonEye.place(x=395, y=363)
    openEye.config(file='images/close-eye.png')
    passwordEntry.config(show="*")
    buttonEye.config(command=show)

    buttonLogin = Button(login, bd=1, bg='#ed8a9a', cursor='hand2', width=15, height=1,
                         text=" LOGIN",
                         command=login_function, font=("Copperplate Gothic", 15, 'bold'))
    buttonLogin.place(x=208, y=436)

    def on_closing():
        sys.exit()

    login.protocol("WM_DELETE_WINDOW", on_closing)

    login.mainloop()


if __name__ == "__main__":
    main()
