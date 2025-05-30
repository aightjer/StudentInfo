from customtkinter import * 
import customtkinter as ct 
from CTkMessagebox import CTkMessagebox 
from tkinter import ttk 
from PIL import Image 
from tkinter import messagebox 

ct.set_appearance_mode('dark') 

class Login(): 
    def __init__(self): 
        self.logWindow = CTk() 
        self.logWindow.geometry('800x600') 
        self.logWindow.resizable(False,False) 
        self.logWindow.title("Admin Login Account") 

        self.bg = CTkFrame(self.logWindow, fg_color= '#111212', height=800, width=800) 
        self.bg.place(x=0, y = 0) 

        self.sms = CTkLabel(self.logWindow, 
                            text = 'STUDENT\nMANAGEMENT\nSYSTEM', 
                            text_color= '#7f5af0', 
                            font = ('Verdana', 45, 'bold'), 
                            fg_color= '#111212') 
        self.sms.place(x = 220, y = 45) 

        self.loginFrame = CTkFrame(self.bg, height= 330, width= 275, corner_radius= 35, border_width=2, fg_color= '#1c1c1c', border_color= '#333332') 
        self.loginFrame.place(x = 260, y = 240) 

        self.Userlabel = CTkLabel(self.loginFrame, text = "Username: ", text_color= '#fffffe') 
        self.Userlabel.place(x = 45, y = 85) 

        self.usern = CTkEntry(self.loginFrame, 
                    placeholder_text="Enter your Username", 
                    placeholder_text_color='#c7c7c7', 
                    text_color="#fffffe", 
                    border_width= 1, 
                    border_color='#333332', 
                    fg_color='#333332',   
                    font=('MS Sans Serif', 12,'bold'), 
                    height=40, 
                    width=200, 
                    corner_radius=10)   
        self.usern.place(x=40, y=110) 

        self.Passlabel = CTkLabel(self.loginFrame, text = "Password: ", text_color= '#fffffe') 
        self.Passlabel.place(x  = 45, y = 155) 
        self.passw = CTkEntry(self.loginFrame, 
                    placeholder_text="Enter your Password", 
                    placeholder_text_color='#c7c7c7', 
                    text_color="#fffffe", 
                    border_width=1, 
                    border_color='#333332', 
                    fg_color='#333332', 
                    height=40, 
                    width=200, 
                    font=('MS Sans Serif', 12,'bold'), 
                    show='*', 
                    corner_radius=10)   
        self.passw.place(x=40, y=180) 

        self.loginbtn = CTkButton(self.loginFrame, 
                                text = "Sign In", 
                                text_color='#ccc7b8', 
                                command = self.login, 
                                border_width=2, 
                                border_color='#333332', 
                                fg_color='#1c1c1c', 
                                hover_color='#4b46bc', 
                                font=('MS Sans Serif', 15,'bold'), 
                                height=35 
                                ) 
        self.loginbtn.place(x = 70,y = 250) 
 
    def login(self): 
        username = "123" 
        password = "123" 
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
        self.mainWindow.geometry('950x580') 
        self.mainWindow.resizable(False, False) 
        self.mainWindow.title("Student Management System") 
        #functions 
        self.mainbg = CTkFrame(self.mainWindow, fg_color= '#1C1C1D', height=950, width=1000) 
        self.mainbg.place(x=0, y = 0) 

        fonts = ('MS Sans Serif', 15, ) 

        headerframe = CTkFrame(self.mainbg, height=60, width=175, corner_radius= 30, border_color= '#4b46bc', border_width= 1 ,fg_color= '#4b46bc') 
        headerframe.place(x=65, y=15) 

        student = CTkLabel(headerframe, text = 'sMs', font = ('Verdana', 50, 'bold'), text_color= '#e0dede') 
        student.place(x = 35, y = -3) 

        infoframe = CTkFrame(self.mainbg, height=460, width=260, corner_radius=30,border_color= '#333332',border_width= 1, fg_color= '#2A2A2A') 
        infoframe.place(x=25, y=90) 

        gandamoframe = CTkFrame(self.mainbg, height=460, width=620, corner_radius=30, border_color= '#333332', border_width= 1 ,fg_color='#2A2A2A') 
        gandamoframe.place(x=303, y=90) 

        sms = CTkLabel(infoframe, text = 'STUDENT\nINFORMATION', font = ('Verdana', 25, 'bold'), text_color= '#9896a3') 
        sms.place(x = 25, y = 15) 

        #Top Frame 
        CreateBtn = CTkButton(self.mainbg, 
                            text='New Student', 
                            height=40, 
                            width=80, 
                            corner_radius= 30, 
                            border_width=2, 
                            border_color= '#333332', 
                            hover_color= '#4b46bc', 
                            fg_color= '#1c1c1c', 
                            text_color= '#e0dede') 
        CreateBtn.place(x= 360, y=25) 
        UpdateBtn = CTkButton(self.mainbg, 
                            text='Update Student', 
                            height=40, 
                            width=80, 
                            corner_radius= 30, 
                            border_color= '#333332', 
                            border_width=2, 
                            hover_color= '#4b46bc', 
                            fg_color='#1c1c1c', 
                            text_color= '#e0dede') 
        UpdateBtn.place(x= 493, y=25) 
        DeleteBtn = CTkButton(self.mainbg, 
                            text='Delete Student', 
                            height=40, 
                            width=80, 
                            corner_radius= 30, 
                            border_color= '#333332', 
                            border_width=2, 
                            hover_color= '#4b46bc', 
                            fg_color='#1c1c1c', 
                            text_color= '#e0dede') 
        DeleteBtn.place(x= 640, y=25) 
        DeleteAllBtn = CTkButton(self.mainbg, 
                            text='Delete All Student', 
                            height=40, 
                            width=70, 
                            corner_radius= 30, 
                            border_color= '#333332', 
                            border_width=2, 
                            hover_color= '#4b46bc', 
                            fg_color='#1c1c1c', 
                            text_color= '#e0dede') 
        DeleteAllBtn.place(x= 780, y=25) 

        #Left Frame 
        studentLabel = CTkLabel(infoframe, text='Student Id: ', font=fonts, text_color= '#e0dede') 
        studentLabel.place(x=25, y=90) 
        stuEntry = CTkEntry(infoframe, 
                            placeholder_text= 'Enter your student id', 
                            placeholder_text_color= '#8a8888', 
                            fg_color =  '#333332', 
                            text_color= '#e0dede', 
                            border_color= '#333332', 
                            border_width= 2, 
                            font=('Arial', 15), 
                            corner_radius= 12, 
                            height = 35, 
                            width= 220) 
        stuEntry.place(x = 20, y = 120) 

        nameLabel = CTkLabel(infoframe, text='Full Name: ', font=fonts, text_color= '#e0dede') 
        nameLabel.place(x=25, y=160) 
        nameEntry = CTkEntry(infoframe, 
                            placeholder_text= 'Enter your name', 
                            placeholder_text_color= '#8a8888', 
                            fg_color =  '#333332', 
                            text_color= '#e0dede', 
                            border_color= '#333332', 
                            border_width= 2, 
                            font=('Arial', 15), 
                            corner_radius= 12, 
                            height = 35, 
                            width= 220) 
        nameEntry.place(x = 20, y = 190) 

        DOBLabel = CTkLabel(infoframe, text='Enter Date of Birth(mm/dd/yyyy):', font=fonts, text_color= '#e0dede') 
        DOBLabel.place(x=25, y=230) 
        DOBEntry = CTkEntry(infoframe, 
                            placeholder_text= 'Enter your date of birth ', 
                            placeholder_text_color= '#8a8888', 
                            fg_color =  '#333332', 
                            text_color= '#e0dede', 
                            border_color= '#333332', 
                            border_width= 2, 
                            font=('Arial', 15), 
                            corner_radius= 12, 
                            height = 35, 
                            width= 220) 
        DOBEntry.place(x = 20, y = 260) 

        GenderLabel = CTkLabel(infoframe, text='Gender: ', font=fonts, text_color= '#e0dede') 
        GenderLabel.place(x=25, y=300) 
        GenderOption = ['Male','Female'] 
        genderBox = CTkComboBox(infoframe, 
                            values = GenderOption, 
                            fg_color =  '#333332', 
                            text_color= '#e0dede', 
                            border_color= '#333332', 
                            border_width= 2, 
                            button_color = '#333332', 
                            font=('Arial', 15), 
                            corner_radius= 12, 
                            height = 35, 
                            width= 220) 
        genderBox.place(x = 20, y = 330) 

        ProgramLabel = CTkLabel(infoframe, text='Program: ', font=fonts, text_color= '#e0dede') 
        ProgramLabel.place(x=25, y=370) 
        ProgramOption = ['Information Technology', 'Computer Engineering', 'Office Administration', 'Hospitality Management'] 
        programBox = CTkComboBox(infoframe, 
                                values = ProgramOption, 
                                font= fonts, 
                                corner_radius=12, 
                                text_color= '#e0dede', 
                                border_color= '#333332', 
                                border_width= 2, 
                                fg_color =  '#333332', 
                                button_color = '#333332', 
                                height=35, 
                                width=220, 
                                ) 
        programBox.place(x = 20, y = 400) 

        #Right Frame 
        searchEntry = CTkEntry(gandamoframe, 
                            height=40, 
                            width=250, 
                            corner_radius=45, 
                            fg_color='#525252', 
                            text_color= '#e0dede', 
                            border_color= '#333332', 
                            border_width= 2, 
                            placeholder_text = 'Search', 
                            placeholder_text_color = '#e6e1e1') 
        searchEntry.place(x=20, y=10) 

        searchBtn = CTkButton(gandamoframe, 
                            height=40, 
                            width=150, 
                            border_width=2, 
                            border_color= '#333332', 
                            hover_color= '#4b46bc', 
                            fg_color='#1c1c1c', 
                            corner_radius= 45, 
                            text = "Search", 
                            text_color= '#e0dede') 
        searchBtn.place(x = 290, y =10) 

        showallBtn = CTkButton(gandamoframe, 
                            height=40, 
                            width=150, 
                            corner_radius= 45, 
                            border_width=2, 
                            border_color= '#333332', 
                            hover_color= '#4b46bc', 
                            fg_color='#1c1c1c', 
                            text = "Show All", 
                            text_color= '#e0dede') 
        showallBtn.place(x=450, y=10) 
        
        tree = ttk.Treeview(gandamoframe) 
        tree.place(x = 20, y = 60) 

        tree['columns'] = ('Student Id', 'Name', 'Date of Birth', 'Gender', 'Department Alloted') 

        tree.column("#0", width=0, stretch=NO) 
        tree.column("Student Id", anchor= W, width=150, stretch=NO) 
        tree.column("Name", width=150, stretch=NO) 
        tree.column("Date of Birth",  width=120, stretch= NO) 
        tree.column("Gender",  width=140, stretch=NO) 
        tree.column("Department Alloted", width=160, stretch=NO) 

        tree.heading('Student Id', text='Student Id') 
        tree.heading('Name', text='Name') 
        tree.heading('Date of Birth', text='Date of Birth') 
        tree.heading('Gender', text='Gender') 
        tree.heading('Department Alloted', text='Department Alloted') 

        tree.place(x = 20, y = 80, width= 730, height=470) 

        style = ttk.Style() 
        style.configure('Treeview.Heading', font = ('MS Sans Serif', 20, 'bold')) 
        
        scroll = ttk.Scrollbar(gandamoframe, orient = VERTICAL) 
        scroll.place(x= 728, y = 82, height= 465) 

        self.logWindow.destroy() 
        self.mainWindow.mainloop() 
    def run(self): 
        self.logWindow.mainloop() 

if __name__ == "__main__": 
    app = Login() 
    app.run() 
