from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Form')
        self.root.geometry('400x550')
        self.root.configure(bg='#0096DC')

        # Set icon using PNG
        try:
            self.icon = PhotoImage(file='TheBackStory.png')
            self.root.iconphoto(False, self.icon)
        except Exception as e:
            print("Icon load failed:", e)

        self.valid_users = {
            'abhimakulshrestha2004@gmail.com': '1234',
            'user@example.com': 'password'
        }

        self.build_ui()

    def build_ui(self):
        # Frame for centering
        frame = Frame(self.root, bg='#0096DC')
        frame.pack(expand=True)

        # Logo Image
        try:
            img = Image.open('TheBackStory.png')
            img = img.resize((80, 80))
            self.logo = ImageTk.PhotoImage(img)
            logo_label = Label(frame, image=self.logo, bg='#0096DC')
            logo_label.pack(pady=(10, 5))
        except Exception as e:
            print("Logo load failed:", e)

        # Title
        title = Label(frame, text="TheBackStory", font=('Verdana', 22, 'bold'), bg='#0096DC', fg='white')
        title.pack(pady=(0, 30))

        # Email Label + Input
        email_label = Label(frame, text="Enter Email", font=('Verdana', 12), bg='#0096DC', fg='white')
        email_label.pack(anchor='w', padx=50)
        self.email_input = ttk.Entry(frame, width=30)
        self.email_input.pack(pady=(0, 20))

        # Password Label + Input
        password_label = Label(frame, text="Enter Password", font=('Verdana', 12), bg='#0096DC', fg='white')
        password_label.pack(anchor='w', padx=50)
        self.password_input = ttk.Entry(frame, width=30, show='*')
        self.password_input.pack(pady=(0, 30))

        # Login Button
        login_btn = Button(frame, text="Login", font=('Verdana', 11), bg='white', fg='black',
                           width=20, height=2, command=self.handle_login)
        login_btn.pack()

    def handle_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        if email in self.valid_users and self.valid_users[email] == password:
            messagebox.showinfo('Success', f'Welcome, {email}!')
        else:
            messagebox.showerror('Error', 'Invalid email or password')


if __name__ == "__main__":
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
