from customtkinter import *
import customtkinter as ct
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
from tkinter import messagebox
import database
from PIL import Image

ct.set_appearance_mode('light')

class Login():
    def __init__(self):
        self.logWindow = CTk()
        self.logWindow.geometry('500x650')
        self.logWindow.resizable(False,False)
        self.logWindow.title("Admin Login Account")
        self.logWindow.iconbitmap("Images/puplogo_UmD_icon.ico")

        self.bg = CTkFrame(self.logWindow, fg_color='#F8FAFF', height=1000, width=1000) 
        self.bg.place(x=0, y = 0) 

        self.wcb = CTkLabel(self.bg, 
                        text = 'Welcome Back, Admin!',
                        text_color= '#5B21B6',
                        font = ('Inter', 35, 'bold'),
                        fg_color= '#F8FAFF')
        self.wcb.place(x = 60, y = 90)

        self.rightpanel = CTkFrame(self.bg, height= 650, width= 80, corner_radius= 23, border_width=1, fg_color= '#5B21B6', border_color= '#7f5af0')
        self.rightpanel.place(x = -60, y = 0)

        self.leftpanel = CTkFrame(self.bg, height= 650, width= 80, corner_radius= 23, border_width=1, fg_color= '#5B21B6', border_color= '#7f5af0')
        self.leftpanel.place(x = 485, y = 0)

        # self.student = CTkLabel(self.logWindow, 
        #                     text = 'STUDENT\nMANAGEMENT\nSYSTEM', 
        #                     text_color= "#FCFAFE",
        #                     font = ('Verdana', 43, 'bold'),
        #                     fg_color= '#5B21B6')
        # self.student.place(x = 45, y = 45)

        # self.management = CTkLabel(self.logWindow, 
        #                     text = '"The secret is not to find the meaning of life, but to\n use your life  to make things that are meaningful."', 
        #                     text_color= '#F8FAFF',
        #                     font = ('Inter', 15),
        #                     fg_color= '#5B21B6')
        # self.management.place(x = 50, y = 525)

        # self.system = CTkLabel(self.logWindow, 
        #                     text = '- James Clear', 
        #                     text_color= '#F8FAFF',
        #                     font = ('Inter', 13),
        #                     fg_color= '#5B21B6')
        # self.system.place(x = 185, y = 565)

        self.loginFrame = CTkFrame(self.bg, height= 330, width= 325, corner_radius= 35, border_width=2, fg_color= '#F8FAFF', border_color= '#7f5af0')
        self.loginFrame.place(x = 95, y = 270)

        # self.logo = CTkImage(Image.open("Images/2011.png"),size = (250,250))
        # self.logolabel = CTkLabel(self.logframe, image = self.logo, text = "")
        # self.logolabel.place(x = 290, y = 225)


        self.persuade = CTkLabel(self.bg, 
                        text = 'Please sign in to your Admin Account',
                        text_color= '#5B21B6',
                        font = ('Inter', 13, 'bold'),
                        fg_color= '#F8FAFF')
        self.persuade.place(x = 145, y = 125)

        self.Userlabel = CTkLabel(self.loginFrame, text = "Username: ", text_color= '#1F2937')
        self.Userlabel.place(x = 45, y = 75)
        
        self.usern = CTkEntry(self.loginFrame, 
                    placeholder_text="Enter your Username",
                    placeholder_text_color='#9CA3AF',
                    text_color="#1F2937",
                    border_width= 2,
                    border_color='#C4B5FD',
                    fg_color='#F9FAFB',  
                    font=('Inter', 12),
                    height=50,
                    width=245,
                    corner_radius=10)  
        self.usern.place(x=40, y=100)

        self.Passlabel = CTkLabel(self.loginFrame, text = "Password: ", text_color= '#1F2937')
        self.Passlabel.place(x  = 45, y = 155)
        self.passw = CTkEntry(self.loginFrame, 
                    placeholder_text="Enter your Password",
                    placeholder_text_color='#9CA3AF',
                    text_color="#1F2937",
                    border_width=2,
                    border_color='#C4B5FD',
                    fg_color='#F9FAFB',
                    height=50,
                    width=245,
                    font=('Inter', 12),
                    show='*',
                    corner_radius=10)  
        self.passw.place(x=40, y=180)

        self.loginbtn = CTkButton(self.loginFrame, 
                                text = "Sign In", 
                                text_color='#FFFFFF', 
                                command = self.login,
                                border_width=2,
                                border_color='#7f5af0',
                                fg_color='#8B5CF6',
                                hover_color="#7C3AED",
                                font=('MS Sans Serif', 15,'bold'),
                                corner_radius= 10,
                                width=245,
                                height=50
                                )
        self.loginbtn.place(x = 40,y = 250)

    def login(self):
        username = "admin123"
        password = "admin123"
        if self.usern.get() == username and self.passw.get() == password:
            CTkMessagebox(title="Success", message="Login Successfully", icon="check", height=70, width=80)
            self.logWindow.after(500, self.show_main_page)
        elif self.usern.get() == "" or self.passw.get() == "":
            CTkMessagebox(title="Warning", message="All fields are required", icon="warning", height=70, width=80)
        else:
            CTkMessagebox(title="Error", message="Invalid Credentials", icon="cancel", height=70, width=80)

    #Main Page
    def show_main_page(self):
        self.mainWindow = CTk()
        self.mainWindow.geometry('1025x650')
        self.mainWindow.resizable(False, False)
        self.mainWindow.title("Student Management System - Dashboard")

        
        def delete_all():
            delete = messagebox.askyesno('Confirm delete', 'Are you sure you want to delete all this data?')
            if delete:
                database.delete_all_students()
                tree.delete(*tree.get_children()) 
                messagebox.showinfo('Deleted', 'All student records have been deleted.')
            else:
                pass

        def show_all():
            treeview_data()
            searchEntry.delete(0, END)
            searchbox.set('Search by')

        def search_student():
            if searchEntry.get() == '':
                messagebox.showerror('Error', 'Please enter a value')
            elif searchbox.get() == 'Search by':
                messagebox.showerror('Error', 'Please select an option')
            else:
                search_data = database.search(searchbox.get(), searchEntry.get().strip())
                tree.delete(*tree.get_children())
                for student in search_data:
                    tree.insert('', END, values = student)

        def delete_student():
            selected_student = tree.selection()
            if not selected_student:
                messagebox.showerror('Error', 'Select data to delete.') 
            else:
                database.delete(stuEntry.get())
                treeview_data()
                clear()
                messagebox.showinfo('Deleted', 'Data has been deleted successfully')

        def update():
            selected_student = tree.selection()
            if not selected_student:
                messagebox.showerror('Error','Select data to update.')
            else:
                database.update(stuEntry.get(),nameEntry.get(),DOBEntry.get(),genderBox.get(),programBox.get(), statusBox.get(), EnrolledBox.get())
                treeview_data()
                clear()
                messagebox.showinfo('Successful','Data has been updated successfully.')

        def select(receiver):
            selected_student = tree.selection()
            if selected_student:
                row = tree.item(selected_student)['values']
                clear()
                stuEntry.insert(0, row [0])
                nameEntry.insert(0, row[1])
                DOBEntry.insert(0, row[2])
                genderBox.set(row[3])
                programBox.set(row[4])

        def clear():
            stuEntry.delete(0, END)
            nameEntry.delete(0, END)
            DOBEntry.delete(0, END)
            genderBox.set('Male')
            programBox.set('Information Technology')

        def treeview_data():
            students = database.fetch_students()
            tree.delete(*tree.get_children())
            for student in students:
                tree.insert('', END, values = student)

        def add_student():
            if stuEntry.get() == '' or nameEntry.get() == '' or DOBEntry.get() == '' or genderBox.get() =='' or programBox.get() == '' or statusBox.get() == '' or EnrolledBox.get() == '':
                messagebox.showerror('Warning!', 'All fields are required.')
            elif database.id_exist(stuEntry.get()):
                messagebox.showerror('Warning!', 'Id already exist.')
            else: 
                database.insert(stuEntry.get(), nameEntry.get(), DOBEntry.get(), genderBox.get(), programBox.get(), statusBox.get(), EnrolledBox.get())
                treeview_data()
                clear()
                messagebox.showinfo('Success!', 'New student added!')

        self.mainbg = CTkFrame(self.mainWindow, fg_color= "#FEFDFE", height=1150, width=1050)
        self.mainbg.place(x=0, y = 0)

        headerframe = CTkFrame(self.mainbg, height=60, width=175, corner_radius= 30, border_color= '#B7A6FA', border_width= 1 ,fg_color= '#8B5CF6')
        headerframe.place(x=65, y=20)

        student = CTkLabel(headerframe, text = 'sMs', font = ('Verdana', 50, 'bold'), text_color= '#FFFFFF')
        student.place(x = 35, y = -3)

        infoframe = CTkFrame(self.mainbg, height=550, width=270, corner_radius=15,border_color= "#B7A6FA",border_width= 2, fg_color= "#FFFFFF")
        infoframe.place(x=15, y=90)

        gandamoframe = CTkFrame(self.mainbg, height=550, width=710, corner_radius=15, border_color= '#B7A6FA', border_width= 2,fg_color="#FFFFFF")
        gandamoframe.place(x=303, y=90)

        header = CTkFrame(self.mainbg, height=60, width=605, corner_radius= 15, border_color= "#2A2A2C", border_width= 1 ,fg_color= "#EDEBEB")
        header.place(x=350, y=20)
        
        sms_frame = CTkFrame(infoframe, height=80, width=245, corner_radius=10, border_color= '#B7A6FA',fg_color="#8B5CF6")
        sms_frame.place(x=13, y=10)

        sms = CTkLabel(sms_frame, text = 'STUDENT\nINFORMATION', font = ('Inter', 25, 'bold'), text_color= '#FFFFFF')
        sms.place(x = 30, y = 10)

        #Top Frame
        CreateBtn = CTkButton(header, 
                            text=' New Student', 
                            height=40,
                            width=80, 
                            corner_radius= 13,
                            border_width=0,
                            border_color= '#4b46bc',
                            hover_color= '#4b46bc', 
                            fg_color= "#2AD14E",
                            font = ('Inter', 15, ),
                            text_color= "#ffffff",command= add_student)
        CreateBtn.place(x= 16, y=9.5)
        UpdateBtn = CTkButton(header, 
                            text='Update Student', 
                            height=40,
                            width=80, 
                            corner_radius= 13,
                            border_color= '#4b46bc',
                            border_width=0,
                            hover_color= '#4b46bc', 
                            fg_color="#5C23E3", 
                            font = ('Inter', 15, ),
                            text_color= "#ffffff",command= update)
        UpdateBtn.place(x= 145, y=9.5)
        DeleteBtn = CTkButton(header, 
                            text='Delete Student', 
                            height=40,
                            width=80, 
                            corner_radius= 13,
                            border_color= '#4b46bc',
                            border_width=0,
                            hover_color= '#4b46bc', 
                            fg_color='#B93E3E',
                            font = ('Inter', 15),
                            text_color= "#FFFFFF", command= delete_student)
        DeleteBtn.place(x= 288, y=9.5)
        DeleteAllBtn = CTkButton(header, 
                            text='Delete All Student', 
                            height=40,
                            width=70, 
                            corner_radius= 13,
                            border_color= '#4b46bc',
                            border_width=0,
                            hover_color= '#4b46bc', 
                            fg_color="#FF0000",
                            font = ('Inter', 15),
                            text_color= "#FFFFFF", command=delete_all)
        DeleteAllBtn.place(x= 435, y=9.5)

        #Left Frame
        studentLabel = CTkLabel(infoframe, text='Student Id: ', font= ('Inter', 13, ), text_color= '#374151')
        studentLabel.place(x=25, y=105)
        stuEntry = CTkEntry(infoframe, 
                            placeholder_text= 'Enter your student id',
                            placeholder_text_color= '#9CA3AF',
                            fg_color = 	'#F9FAFB',
                            text_color= '#1F2937',
                            border_color= '#C4B5FD',
                            border_width= 2,
                            font=('Inter', 13),
                            corner_radius= 8,
                            height = 40,
                            width= 230)
        stuEntry.place(x = 20, y = 130)

        nameLabel = CTkLabel(infoframe, text='Full Name: ', font= ('Inter', 13, ), text_color= '#374151')
        nameLabel.place(x=25, y=175)
        nameEntry = CTkEntry(infoframe, 
                            placeholder_text= 'Enter your name',
                            placeholder_text_color= '#9CA3AF',
                            fg_color = 	'#F9FAFB',
                            text_color= '#1F2937',
                            border_color= '#C4B5FD',
                            border_width= 2,
                            font=('Inter', 13),
                            corner_radius= 8,
                            height = 40,
                            width= 230)
        nameEntry.place(x = 20, y = 200)

        DOBLabel = CTkLabel(infoframe, text='Date of Birth:', font= ('Inter', 13, ), text_color= '#374151')
        DOBLabel.place(x=25, y=246)
        DOBEntry = CTkEntry(infoframe, 
                            placeholder_text= 'Enter your date of birth(mm/dd/yyyy)',
                            placeholder_text_color= '#9CA3AF',
                            fg_color = 	'#F9FAFB',
                            text_color= '#1F2937',
                            border_color= '#C4B5FD',
                            border_width= 2,
                            font=('Inter', 13),
                            corner_radius= 8,
                            height = 40,
                            width= 230)
        DOBEntry.place(x = 20, y = 273)

        GenderLabel = CTkLabel(infoframe, text='Gender: ', font= ('Inter', 13, ), text_color= '#374151')
        GenderLabel.place(x=25, y=318)
        GenderOption = ['Male','Female']
        genderBox = CTkComboBox(infoframe, 
                            values = GenderOption,
                            fg_color = 	'#F9FAFB',
                            text_color= '#1F2937',
                            border_color= '#C4B5FD',
                            border_width= 2,
                            button_color = '#C4B5FD',
                            button_hover_color= '#8B5CF6',
                            font=('Arial', 13),
                            corner_radius= 8,
                            height = 40,
                            width= 230,
                            state = "readonly")
        genderBox.place(x = 20, y = 345)

        ProgramLabel = CTkLabel(infoframe, text='Program: ', font= ('Inter', 13, ), text_color= '#374151')
        ProgramLabel.place(x=25, y=390)
        ProgramOption = ['Information Technology', 'Computer Engineering', 'Office Administration', 'Hospitality Management']
        programBox = CTkComboBox(infoframe, 
                                values = ProgramOption,
                                font=('Inter', 13, ),
                                corner_radius=12,
                                text_color= '#1F2937',
                                border_color= '#C4B5FD',
                                border_width= 2,
                                fg_color = 	'#F9FAFB',
                                button_color = '#C4B5FD',
                                button_hover_color= '#8B5CF6',
                                height=40,
                                width=230,
                                state = "readonly")
        programBox.place(x = 20, y = 417)

        StatusLabel = CTkLabel(infoframe, text='Status: ', font= ('Inter', 13, ), text_color= '#374151')
        StatusLabel.place(x=25, y=460)
        statusOption = ['Regular', 'Irregular']
        statusBox = CTkComboBox(infoframe, 
                                values = statusOption,
                                font=('Inter', 13, ),
                                corner_radius=12,
                                text_color= '#1F2937',
                                border_color= '#C4B5FD',
                                border_width= 2,
                                fg_color = 	'#F9FAFB',
                                button_color = '#C4B5FD',
                                button_hover_color= '#8B5CF6',
                                height=40,
                                width=115,
                                state = "readonly")
        statusBox.place(x = 20, y = 485)

        EnrolledLabel = CTkLabel(infoframe, text='Enrolled: ', font= ('Inter', 13, ), text_color= '#374151')
        EnrolledLabel.place(x=145, y=460)
        EnrolledOption = ['Official', 'Unofficial']
        EnrolledBox = CTkComboBox(infoframe, 
                                values = EnrolledOption,
                                font=('Inter', 13, ),
                                corner_radius=12,
                                text_color= '#1F2937',
                                border_color= '#C4B5FD',
                                border_width= 2,
                                fg_color = 	'#F9FAFB',
                                button_color = '#C4B5FD',
                                button_hover_color= '#8B5CF6',
                                height=40,
                                width=108,
                                state = "readonly")
        EnrolledBox.place(x = 140, y = 485)

        #Right Frame
        searchOption = ['Student Id', 'Name', 'Gender','Program', 'Status', 'Enrolled']
        searchbox = CTkComboBox(gandamoframe,
                                values = searchOption,
                                state='readonly',
                                corner_radius=13,
                                text_color= "#ffffff",
                                border_color= '#B7A6FA',
                                border_width= 1,
                                fg_color = 	'#8B5CF6',
                                button_color = '#B7A6FA',
                                button_hover_color= '#8B5CF6',
                                height=40,
                                )
        searchbox.place(x = 20, y = 10)
        searchbox.set('Search by:')

        searchEntry = CTkEntry(gandamoframe, 
                            height=40, 
                            width=200, 
                            corner_radius=13,
                            fg_color='#F9FAFB',
                            text_color= "#1F2937",
                            border_color= '#B7A6FA',
                            border_width= 2,
                            placeholder_text = 'Search', 
                            placeholder_text_color = '#9CA3AF')
        searchEntry.place(x=175, y=10)

        searchBtn = CTkButton(gandamoframe, 
                            height=40, 
                            width=100, 
                            border_width=1,
                            border_color= '#B7A6FA',
                            hover_color= '#B7A6FA', 
                            fg_color='#8B5CF6', 
                            corner_radius= 13, 
                            text = "Search",
                            text_color= "#FFFFFF", command = search_student)
        searchBtn.place(x = 480, y =10)

        showallBtn = CTkButton(gandamoframe,
                            height=40,
                            width=100, 
                            corner_radius= 13,
                            border_width=1,
                            border_color= '#B7A6FA',
                            hover_color= '#B7A6FA', 
                            fg_color='#8B5CF6', 
                            text = "Show All",
                            text_color= "#ffffff", command= show_all)
        showallBtn.place(x=585, y=10)
        tree = ttk.Treeview(gandamoframe)
        tree.place(x = 20, y = 60)

        tree['columns'] = ('Student Id', 'Name', 'Date of Birth', 'Gender', 'Department Alloted', 'Status', 'Enrolled')

        tree.column("#0", width=0, stretch=NO)
        tree.column("Student Id", anchor= W, width=130, stretch=NO)
        tree.column("Name", width=150, stretch=NO)
        tree.column("Date of Birth",  width=100, stretch= NO)
        tree.column("Gender",  width=70, stretch=NO)
        tree.column("Department Alloted", width=190, stretch=NO)
        tree.column("Status", width=90, stretch=NO)
        tree.column("Enrolled", width=80, stretch=NO)

        tree.heading('Student Id', text='Student Id')
        tree.heading('Name', text='Name')
        tree.heading('Date of Birth', text='Date of Birth')
        tree.heading('Gender', text='Gender')
        tree.heading('Department Alloted', text='Department Alloted')
        tree.heading('Status', text='Status')
        tree.heading('Enrolled', text='Enrolled')
        tree.place(x = 28, y = 80, width= 830, height=580)

        style = ttk.Style()
        style.configure('Treeview.Heading', font = ('MS Sans Serif', 20, 'bold'))
        
        scroll = ttk.Scrollbar(gandamoframe, orient = VERTICAL, command=tree.yview)
        scroll.place(x= 835, y = 82, height= 575)

        treeview_data()
        self.mainWindow.bind('<ButtonRelease>', select)

        self.logWindow.destroy()
        self.mainWindow.mainloop()
    def run(self):
        self.logWindow.mainloop()

if __name__ == "__main__":
    app = Login()
    app.run()