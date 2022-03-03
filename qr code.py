from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.title("QR Generator")
        self.root.geometry('900x500')
        self.root.resizable(False,False)
        title=Label(self.root,text="QR code Generator",bg="blue",fg="black",font=("times new roman",40)).place(x=0,y=0,relwidth=1)
        #employee details
#         variables
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()
        
        
        emp_frame=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        emp_frame.place(x=50,y=100,width=455,height=350)
        emp_title=Label(emp_frame,text="Employee Details",bg="blue",fg="black",font=("times new roman",20)).place(x=0,y=0,relwidth=1)
        label1=Label(emp_frame,text="Employee ID",bg="white",fg="black",font=("times new roman",15,"bold")).place(x=25,y=50)
        label2=Label(emp_frame,text="Employee name",bg="white",fg="black",font=("times new roman",15,"bold")).place(x=25,y=90)
        label3=Label(emp_frame,text="Department",bg="white",fg="black",font=("times new roman",15,"bold")).place(x=25,y=130)
        label4=Label(emp_frame,text="Designation",bg="white",fg="black",font=("times new roman",15,"bold")).place(x=25,y=170)
        
        text1=Entry(emp_frame,bg="light yellow",fg="black",textvariable=self.var_id,font=("times new roman",15)).place(x=200,y=50)
        text2=Entry(emp_frame,bg="light yellow",fg="black",textvariable=self.var_name,font=("times new roman",15)).place(x=200,y=90)
        text3=Entry(emp_frame,bg="light yellow",fg="black",textvariable=self.var_department,font=("times new roman",15)).place(x=200,y=130)
        text4=Entry(emp_frame,bg="light yellow",fg="black",textvariable=self.var_designation,font=("times new roman",15)).place(x=200,y=170)
        
        btn1=Button(emp_frame,bg="grey",text="QR Generator",command=self.generate,font=("times new roman",20,"bold")).place(x=25,y=230,width=200,height=50)
        btn1=Button(emp_frame,bg="grey",text="Clear",command=self.clear,font=("times new roman",20,"bold")).place(x=250,y=230,width=150,height=50)
        
        self.msg=""
        self.msg1=Label(emp_frame,text=self.msg,bg="white",fg="green",font=("times new roman",17,"bold"))
        self.msg1.place(x=10,y=300,relwidth=1)
        
        emp_code=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        emp_code.place(x=555,y=100,width=300,height=347)
        emp_title=Label(emp_code,text="Employee QR Code",bg="blue",fg="black",font=("times new roman",20)).place(x=0,y=0,relwidth=1)
        
        self.qr=Label(emp_code,text="QR Code \n Not Available",bd=5,bg="light blue",fg="green",font=("times new roman",13))
        self.qr.place(x=20,y=70,height=250,width=250)

    def generate(self):
        if(self.var_id.get()=="" or self.var_name.get()=="" or self.var_department.get()=="" or self.var_designation.get()=="" ): 
            self.msg=" All Fields Required!!!"
            self.msg1.config(text=self.msg,fg="red")
            
        else:
            qr_data=(f"Employee ID:{self.var_id.get()} \n Employee name:{self.var_name.get()} \n Department:{self.var_department.get()} \n Designation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[250,250])
            qr_code.save("Employee_QR/Emp_"+ str(self.var_id.get())+'.png')
            self.im=ImageTk.PhotoImage(file="Employee_QR/Emp_"+ str(self.var_id.get())+'.png')
            self.qr.config(image=self.im)
            print(qr_code)
            self.msg=" QR Generated Successfully!!!"
            self.msg1.config(text=self.msg,fg="green")
            
    def clear(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_designation.set("")
        self.msg=""
        self.msg1.config(text=self.msg)
        self.qr.config(image="")
        
        
              
        
root=Tk()
obj=Qr_Generator(root)

root.mainloop()