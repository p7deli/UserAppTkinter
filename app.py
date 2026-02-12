import tkinter as tk
from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFrame, CTkImage, CTkComboBox
from tkinter import filedialog, messagebox
from PIL import Image
from shamsicalendar import ShamsiCalendar
from tkinter.ttk import Treeview
from database_ import add_member, show_members, create_table, delete_user_db, update_user_db
import ast


WIDTH = 650
HEIGHT = 500


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.x = ((self.winfo_screenwidth() // 2) - (WIDTH // 2))
        self.y = ((self.winfo_screenheight() // 2) - (HEIGHT // 2))

        self.title('Add Member App')
        self.geometry(f'{WIDTH}x{HEIGHT}+{self.x}+{self.y}')
        self.resizable(False, False)
        self.config(bg='#f0f0f0')

        # ---------------- Var
        self.pic_path = None
        # -----------------

        self.frame_pic = CTkFrame(self, width=200, height=200, border_width=2, border_color='#b5b5b5',
                                  fg_color='gray', corner_radius=10)
        self.frame_pic.place(x=20, y=20)

        self.lbl_pic_ = CTkLabel(self.frame_pic, text='Select pic', width=190, height=190, fg_color='gray',
                                 corner_radius=10)
        self.lbl_pic_.place(x=5, y=5)

        CTkButton(self, text='انتخاب عکس', width=190, height=40, corner_radius=10, fg_color='#666768', border_width=2,
                  border_color='#8B8B8B', text_color='white', font=('B Titr', 15), hover_color='#8B8B8B',
                  command=self.select_pic).place(x=25, y=227)

        # ---------------------------------------------------------------------
        self.frame_inputs = CTkFrame(self, width=400, height=200, border_width=2, border_color='#b5b5b5',
                                  fg_color='#f0f0f0', corner_radius=10)
        self.frame_inputs.place(x=225, y=20)

        CTkLabel(self.frame_inputs, text='نام     ', width=350, height=40, corner_radius=10, fg_color='#cfcdcd',
                 font=('B Titr', 15), anchor='e', text_color='black').place(x=20, y=10)
        self.txt_fname = CTkEntry(self.frame_inputs, width=220, height=30, bg_color='#cfcdcd', fg_color='white',
                                  text_color='black', justify='center')
        self.txt_fname.place(x=35, y=15)

        CTkLabel(self.frame_inputs, text='نام خانوادگی     ', width=350, height=40, corner_radius=10, fg_color='#cfcdcd',
                 font=('B Titr', 15), anchor='e', text_color='black').place(x=20, y=55)
        self.txt_lname = CTkEntry(self.frame_inputs, width=220, height=30, bg_color='#cfcdcd', fg_color='white',
                                  text_color='black', justify='center')
        self.txt_lname.place(x=35, y=60)

        CTkLabel(self.frame_inputs, text='جنسیت     ', width=350, height=40, corner_radius=10, fg_color='#cfcdcd',
                 font=('B Titr', 15), anchor='e', text_color='black').place(x=20, y=100)
        self.txt_gender = CTkComboBox(self.frame_inputs, values=['مرد', 'زن'], width=220, height=30, bg_color='#cfcdcd', fg_color='white',
                                  text_color='black', justify='center', font=('B Titr', 15))
        self.txt_gender.place(x=35, y=105)

        CTkLabel(self.frame_inputs, text='تاریخ تولد     ', width=350, height=40, corner_radius=10, fg_color='#cfcdcd',
                 font=('B Titr', 15), anchor='e', text_color='black').place(x=20, y=150)
        self.txt_birthdate = ShamsiCalendar.ShamsiDateEntry(self.frame_inputs, width_entry=27)
        self.txt_birthdate.place(x=35, y=157)
    
        self.btn_add = CTkButton(self, text='اضافه کردن عضو', width=390, height=40, corner_radius=10, fg_color='#666768', border_width=2,
                  border_color='#8B8B8B', text_color='white', font=('B Titr', 15), hover_color='#8B8B8B', command=self.add_members_)
        self.btn_add.place(x=230, y=227)

        self.btn_edit = CTkButton(self, text='ویرایش کردن عضو', width=390, height=40, corner_radius=10, fg_color="#6EB5FC", border_width=2,
                  border_color="#208EFC", text_color='white', font=('B Titr', 15), hover_color='#208EFC', command=self.update_user)
        self.btn_edit.place_forget()
        # --------------------------------------------------------------------
        self.frame_table = CTkFrame(self, width=605, height=200, border_width=2, border_color='#b5b5b5',
                                    fg_color='#f0f0f0', corner_radius=10)
        self.frame_table.place(x=20, y=275)

        self.scrollbar = tk.Scrollbar(self.frame_table)

        self.columns = ['آیدی', 'نام', 'نام خانوادگی', 'جنسیت', 'تاریخ تولد']
        self.table = Treeview(self.frame_table, columns=self.columns, height=8, show='headings', yscrollcommand=self.scrollbar.set)
        self.table.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.Y)
        self.scrollbar.config(command=self.table.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)

        for column in self.columns:
            self.table.column(column, width=111, anchor='center')
            self.table.heading(column, text=column, anchor='center')
        
        # ------------------------------------------------- Context Menu
        self.menu = tk.Menu(self, tearoff=0)

        self.menu.add_command(label='View', command=self.view_user)
        self.menu.add_command(label='Delete', command=self.delete_user)
        self.menu.add_command(label='Edit', command=self.select_user_for_edit)

        self.table.bind('<Button-3>', self.show_menu)

    def select_pic(self):
        filetypes = [
            ("Image files", ("*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif", "*.tiff")),
            ("All files", "*.*")
        ]
        path_ = filedialog.askopenfilename(title='یک عکس انتخاب کنید', filetypes=filetypes)
        if not path_:
            messagebox.showinfo('انتخاب عکس', 'شما هیچ عکسی انتخاب نکردید')
            return

        self.pic_path = path_
        img_ = Image.open(path_)
        ph_img = CTkImage(img_, size=(170, 170))
        self.lbl_pic_.configure(image=ph_img)
        self.lbl_pic_.configure(text='')
    
    def update_table(self):
        self.table.delete(*self.table.get_children())
        members = show_members()
        
        for member in members:
            self.table.insert('', tk.END, values=member)
    
    def update_txt(self):
        self.txt_fname.delete('0', tk.END)
        self.txt_lname.delete('0', tk.END)
        self.lbl_pic_.configure(image=None, text='SELECT PIC')
        self.pic_path = None

    def add_members_(self):

        fname = self.txt_fname.get()
        lname = self.txt_lname.get()
        gender = self.txt_gender.get()
        birthdate = self.txt_birthdate.get()
        photo = self.pic_path

        if fname != '' and lname != '' and photo != None:
            add_member(fname, lname, gender, str(birthdate), photo)
            messagebox.showinfo('افزودن کاربر', 'کاربر با موفقیت اضافه شد')
            self.update_table()
            self.update_txt()
        else:
            messagebox.showerror('Error', 'لطفا موارد خواسته شده را وارد کنید')
    
    def show_menu(self, event):
        item = self.table.identify_row(event.y)

        if item:
            self.table.selection_set(item)
            self.menu.post(event.x_root, event.y_root)
        else:
            self.table.selection_remove(self.table.selection())
    
    def view_user(self):
        item = self.table.item(self.table.selection())['values']
        img_binary = ast.literal_eval(item[-1])

        with open('outputimg.png', 'wb') as fl:
            fl.write(img_binary)
        
        fname = item[1]
        lname = item[2]
        gender = item[3]
        birthdate = item[4].replace('-', '/')
        img = Image.open('outputimg.png')
        ph = CTkImage(img, size=(100, 100))

        window = tk.Toplevel(self)

        x, y = ((window.winfo_screenwidth()//2)-(350//2)), ((window.winfo_screenheight()//2)-(300//2))
        window.resizable(False, False)
        window.geometry(f'350x300+{x}+{y}')
        window.config(bg='gray')

        CTkLabel(window, text='', image=ph, width=110, height=110, fg_color='white', corner_radius=5).place(x=125, y=10)
        CTkLabel(window, text=fname, width=300, height=30, fg_color='white', text_color='black',
                font=('B Nazanin', 15, 'bold'), corner_radius=5).place(x=25, y=145)
        CTkLabel(window, text=lname, width=300, height=30, fg_color='white', text_color='black',
                font=('B Nazanin', 15, 'bold'), corner_radius=5).place(x=25, y=180)
        CTkLabel(window, text=gender, width=300, height=30, fg_color='white', text_color='black',
                font=('B Nazanin', 15, 'bold'), corner_radius=5).place(x=25, y=215)
        CTkLabel(window, text=birthdate, width=300, height=30, fg_color='white', text_color='black',
                font=('B Nazanin', 15, 'bold'), corner_radius=5).place(x=25, y=250)

        window.mainloop()
    
    def delete_user(self):
        item = self.table.selection()
        if item:
            ques = messagebox.askyesno('Ques', 'آیا از حذف این مورد مطمئنی؟')
            if ques:
                user_id = self.table.item(item)['values'][0]
                delete_user_db(user_id)
                messagebox.showinfo('Delete', 'کاربر با موفقیت حذف شد.')
                self.update_table()
    
    def select_user_for_edit(self):
        self.txt_fname.delete('0', tk.END)
        self.txt_lname.delete('0', tk.END)
        item = self.table.item(self.table.selection())['values']
        fname = item[1]
        lname = item[2]
        gender = item[3]
        birthdate = item[4]
        img_binary = ast.literal_eval(item[5])

        with open('outputimg.png', 'wb') as fl:
            fl.write(img_binary)
        self.pic_path = 'outputimg.png'

        img_ = Image.open(self.pic_path)
        ph_img = CTkImage(img_, size=(170, 170))
        self.lbl_pic_.configure(image=ph_img)
        self.lbl_pic_.configure(text='')

        self.txt_fname.insert('0', fname)
        self.txt_lname.insert('0', lname)
        self.txt_gender.set(gender)
        self.txt_birthdate.set_date(birthdate)

        self.btn_edit.place(x=230, y=227)
        self.btn_add.place_forget()
    
    def update_user(self):
        user_id = self.table.item(self.table.selection())['values'][0]
        fname = self.txt_fname.get()
        lname = self.txt_lname.get()
        gender = self.txt_gender.get()
        birthdate = self.txt_birthdate.get()
        photo = self.pic_path

        if fname != '' and lname != '' and photo != None:
            update_user_db(fname, lname, gender, str(birthdate), photo, user_id)
            messagebox.showinfo('ویرایش کاربر', 'کاربر با موفقیت ویرایش شد')
            self.update_table()
            self.update_txt()
            self.btn_edit.place_forget()
            self.btn_add.place(x=230, y=227)
        else:
            messagebox.showerror('Error', 'لطفا موارد خواسته شده را وارد کنید')


if __name__ == '__main__':
    create_table()

    app = App()
    app.update_table()
    app.mainloop()