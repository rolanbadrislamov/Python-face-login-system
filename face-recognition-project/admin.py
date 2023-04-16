import tkinter.filedialog as filedialog
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os
import sys

def main():
    global image_data
    image_data = None

    def on_enter(event):
        if usernameEntry.get() == '      Username':
            usernameEntry.delete(0, END)

    def on_enter2(event):
        if passwordEntry.get() == '      Password':
            passwordEntry.delete(0, END)

    def get_image():
        global image_data
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'rb') as image_file:
                image_data = image_file.read()

    def register():
        global image_data
        if image_data == None:
            messagebox.showerror('Error', 'Please choose an image')
            return
        if not os.path.exists('users.txt'):
            with open('users.txt', 'w') as file:
                file.write('')

        password = passwordEntry.get()
        username = usernameEntry.get()

        if password and usernameEntry.get():
            if usernameEntry.get() == '' or passwordEntry.get() == '':
                messagebox.showerror('Error', 'Every field required')

            elif usernameEntry.get() == 'admin':
                messagebox.showerror('Error', 'Username is already taken')

            elif usernameEntry.get() == '      Username' or passwordEntry.get() == '      Password':
                messagebox.showerror('Error', 'Every field required')

            with open('users.txt', 'r') as file:
                if username in file.read():
                    messagebox.showerror('Error', 'USERNAME IS ALREADY TAKEN')
                    return
                else:
                    with open('users.txt', 'a') as file:
                        file.write(
                            f'{usernameEntry.get()},{password}\n')

            with open(f"pics/{usernameEntry.get() + '.jpg'}", "wb") as file:
                file.write(image_data)
            messagebox.showinfo('Successful', 'Registration successful')
            usernameEntry.delete(0, END)
            passwordEntry.delete(0, END)
            image_data = None

    login = Tk()
    login.title("Registration")
    login.resizable(False, False)
    login.geometry('600x600+300+50')
    bg = ImageTk.PhotoImage(file='images/admin_bg.png')
    bgLabel = Label(login, image=bg)
    bgLabel.place(x=-2, y=0)
    heading = Label(login, text='USER REGISTRATION', font=("Cascadia code", 23, 'bold'),
                    bg='#E7A1A1')
    heading.place(x=150, y=170)

    buttonBiomety = Button(login, bd=1, bg='#ed8a9a', cursor='hand2', width=15, height=1,
                           text=" CHOOSE IMAGE",
                           command=get_image, font=("Copperplate Gothic", 15, 'bold'))
    buttonBiomety.place(x=208, y=230)

    usernameEntry = Entry(login, width=20, font=("Cascadia code", 16, 'bold'),
                          bg='#EDBFBF')

    usernameEntry.place(x=180, y=300)
    usernameEntry.insert(0, '      Username')
    usernameEntry.bind("<FocusIn>", on_enter)

    passwordEntry = Entry(login, width=20, font=("Cascadia code", 16, 'bold'),
                          bg='#EDBFBF')
    passwordEntry.place(x=180, y=360)
    passwordEntry.insert(0, '      Password')
    passwordEntry.bind("<FocusIn>", on_enter2)

    Frame(login, width=243, height=2, bg='black').place(x=180, y=330)
    Frame(login, width=243, height=2, bg='black').place(x=180, y=391)

    copyright = Label(login, text='©Rolan Badrislamov', font=("Copperplate Gothic", 18, 'bold'),
                      bg='#E7A1A1', fg='#FFF2F2')
    copyright.place(x=45, y=540)

    buttonLogin = Button(login, bd=1, bg='#ed8a9a', cursor='hand2', width=15, height=1,
                         text=" REGISTER",
                         command=register, font=(
                             "Copperplate Gothic", 15, 'bold')
                         )
    buttonLogin.place(x=208, y=436)

    def on_closing():
        sys.exit()

    login.protocol("WM_DELETE_WINDOW", on_closing)

    login.mainloop()


if __name__ == '__main__':
    main()
