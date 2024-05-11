from tkinter import *
from tkinter import messagebox
import psycopg2
from tkinter import filedialog
from PIL import ImageTk
import customtkinter
from customtkinter import *
from PIL import Image,ImageTk
import datetime
root=customtkinter.CTk()


width = 800
height = 600

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position of the window
x = (screen_width - width) // 2  # Center horizontally
y = (screen_height - height) // 2  # Center vertically

# Set the geometry of the window
root.geometry(f"{width}x{height}+{x}+{y}")





heading_font = ("Arial", 12, "bold")

custom_font = ('Helvetica', 20)

#connect to database

conn = psycopg2.connect(
   database="management", user='postgres', password='pgadmin4', host='127.0.0.1', port= '5432')
cur=conn.cursor()

conn.autocommit = True

#admin login function
product_list=[]
product_labels = []
widget_layout={}

def disable_widgets():
   
    global widget_layout
    widget_layout = {widget: widget.place_info() for widget in root.winfo_children() if widget.winfo_manager()}
    for widget in root.winfo_children():
        widget.place_forget()






def customer_details_destroy():
     
     return





    
customerfont=("Arial", 15)


def restore_widgets():
    global widget_layout
    for widget, place_info in widget_layout.items():
        widget.place_configure(**place_info)


def submit_details_fun(bill):
     restore_widgets()
     name=customer_name_entry.get()
     phno=customer_phno_entry.get()
     phno=int(phno)
     print(name,phno)
     current_date = datetime.date.today()
     
     
     cur.execute("""

        insert into customer (customer_name ,customer_phno,total_bill,date_col) values(%s,%s,%s,%s)
          
                        """,(name,phno,bill,current_date))
     
     


def checkout():
    global total_bil
    total_bil=0
    for b in product_list:
         total_bil=total_bil+b[4]

         

         
         
    disable_widgets()
    global customer_name_entry,customer_phno_entry
    customer_frame=LabelFrame(root,text="Customer Information",font=custom_font,padx=30,pady=30)
    customer_frame.place(x=330,y=250)
    customer_name_label=Label(customer_frame,text="Name",font=customerfont)
    customer_name_entry=customtkinter.CTkEntry(customer_frame)
    customer_name_label.grid(row=0,column=0,padx=10,pady=10)
    customer_name_entry.grid(row=0,column=1)
    customer_phno=Label(customer_frame,text="Ph NO",font=customerfont)
    customer_phno_entry=customtkinter.CTkEntry(customer_frame)
    customer_phno.grid(row=1,column=0,pady=15)
    customer_phno_entry.grid(row=1,column=1)

    submit_customer_details_btn=customtkinter.CTkButton(customer_frame,text="Submit",command=lambda:submit_details_fun(total_bil))
    submit_customer_details_btn.grid(row=2,column=1)




     
    


    

     

     
     
     










nt=350
xpr=450
xp=250
ypr=350
def product_picker(choice):
     
     global product_frame,ypr,xpr,nt,xp
     product_frame=None
     
     
     if not product_frame:  
        product_frame = LabelFrame(root, borderwidth=0)
        product_frame.place(x=xp, y=nt)
        price_label_frame=LabelFrame(root,borderwidth=0)
        price_label_frame.place(x=xpr,y=ypr)

        
     
     
     

     
    

     product_list.append(choice)
     
     
     

     label=Label(product_frame,text=choice[1])
     product_labels.append(label)
     label.pack()
     pricelabel=Label(price_label_frame,text=choice[4])
     pricelabel.pack()



     ypr=ypr+40
     nt=nt+40

     
     
     
     
     
     
     
     

def employee_view():
         cur.execute("""


                select * from product


                        """)
         data=cur.fetchall()
         data1=["a","b","v"]
         selected_product=StringVar()
         selected_product.set("Select product")
         

         drop_product_menu=OptionMenu(root, selected_product,*data,command=product_picker)
         drop_product_menu.place(x=550,y=200)
         
         
         
         productlabel_frame=Frame(root,width=30,borderwidth=300)
         
         productlabel_frame.place(x=350,y=200)
         product_name_label=Label(root,text="Product",font=heading_font)
         product_name_label.place(x=250,y=300)
         price_label=Label(root,text="Price",font=heading_font)
         price_label.place(x=450,y=300)
         product_option=Label(root,text="Option",font=heading_font)
         product_option.place(x=650,y=300)
         checkout_btn=customtkinter.CTkButton(root,text="Checkout",command=checkout)
         checkout_btn.place(x=500,y=500)


         
              
         

         

         

         

         #addproductbrn_list=customtkinter.CTkButton(root,text="ADD")
         #addproductbrn_list.pack()

              
              







#admin function

def adminfun():



    def clear_window(admin1):
        # Destroy all widgets in the window
        for widget in admin1.winfo_children():
             widget.destroy()

    def productsubmitfun(name,size,catagory,price,stock):                                                    #product submit fun 
        
        cur.execute("""

            INSERT INTO product (product_id,prduct_name,size,catagory,price,stock) 
                     VALUES (%s, %s,%s,%s,%s,%s)
                    """, ("1",name,int(size),catagory,int(price),int(stock)))
        

    def addproductfun():                                                                                    #add product function
             clear_window(admin) 
             productlabelframe=LabelFrame(admin,text="ADD Product",font=custom_font,padx=25,pady=10)
             productlabelframe.pack(pady=60)
             namelabel=Label(productlabelframe, text="Name: ")
             namelabel.grid(row=1,column=0,padx=5)  
             nameinput=Entry(productlabelframe)
             nameinput.grid(row=1,column=1,padx=5,pady=10)
             catagorylabel=Label(productlabelframe, text="Catagory: ").grid(row=2, column=0)
             catagoryinput=Entry(productlabelframe)
             catagoryinput.grid(row=2, column=1)
             priceLabel=Label(productlabelframe, text="Price($):").grid(row=3,column=0)
             priceInput=Entry(productlabelframe)
             priceInput.grid(row=3,column=1,pady=10)
             stocklabel=Label(productlabelframe,text="Stock Quantity:")
             stocklabel.grid(row=4,column=0)
             stockentry=Entry(productlabelframe)
             stockentry.grid(row=4,column=1)
             sizelabel=Label(productlabelframe,text="Size").grid(row=5,column=0)
             sizeentry=Entry(productlabelframe)
             sizeentry.grid(row=5,column=1,pady=10)
             imagebtn=customtkinter.CTkButton(productlabelframe,text="Upload Image").grid(row=6,column=1)
             
             
            
             productsubmitbtn=customtkinter.CTkButton(productlabelframe,text="Submit",command=lambda:productsubmitfun(nameinput.get(),sizeentry.get(),catagoryinput.get(),priceInput.get(),stockentry.get()))
             productsubmitbtn.grid(row=7,columnspan=2,pady=10)



    def print_sales_report():                                                                               #print sales report function
         



         return
    


    
         
         
    


    def loginfun():
       

        adminusername=uname_input_admin.get()
        adminpass=pass_input_admin.get()
    

        if adminusername=="admin" and adminpass=="admin" :
             
             clear_window(admin)
             messagebox.showinfo("Successful login","You are loged in as "+adminusername)
             #add prodrct

             addproductbtn=customtkinter.CTkButton(admin,text="Add product", command=addproductfun)
             addproductbtn.place(x=400,y=500)
             admin_print_sales_repot=customtkinter.CTkButton(admin,text="Print today sales report",command=print_sales_report).pack()

             


        else:
             messagebox.showerror("Error", "Invalid username or  password")





    admin=Toplevel()
    admin.iconbitmap('featured-image.ico')
    admin.title("Admin Pannel")
    admin.geometry("1600x800")
    
    admin_login_frame=LabelFrame(admin,padx=50,pady=40)
    admin_login_frame.pack(pady=260)




    #input labels 
    uname_admin=Label(admin_login_frame,text="Username:")
    pass_admin=Label(admin_login_frame,text="Password:")



    #login inputs
    global uname_input_admin
    uname_input_admin=Entry(admin_login_frame)
    global pass_input_admin
    pass_input_admin=Entry(admin_login_frame)


    #pack all the wogets of admin
    uname_admin.pack()
    uname_input_admin.pack()
    pass_admin.pack()
    pass_input_admin.pack()
    

    loginbtn=customtkinter.CTkButton(admin_login_frame,text="Login",command=loginfun).pack(pady=10)
    
       


                                                                                                    



def prnt_inv():                                                                 ######### print_inv function
    invoice=Toplevel()
    invoice.title("Generate invoice")
    invoice.iconbitmap('featured-image.ico')
    invoice.geometry("700x700")

###### show record


    def showrec():
        cur.execute("""

                select * from login
                    """)
        records=cur.fetchall()
        inte=len(records)
        counter=0
        showlabellist=[]
        while(counter<inte):
            #inte=str(inte)
            showlabels=Label(invoice,text=records[counter])
            showlabellist.append(showlabels)
            counter=counter+1

        
        for showlabel in showlabellist:
            showlabel.pack()


 

    invoicelabelframe=LabelFrame(invoice,text="")
    
    invoicelabelframe.pack()
    


    first_namelabel=Label(invoicelabelframe,text="Enter first_name:")
    first_name=Entry(invoicelabelframe)
    phnolabel=Label(invoicelabelframe,text="Enter your ph no:")
    phno=Entry(invoicelabelframe)

    passlabel=Label(invoicelabelframe,text="Enter last_name:")

    last_name=Entry(invoicelabelframe)
    first_name.grid(row=0,column=1)
    first_namelabel.grid(row=0,column=0)
    passlabel.grid(row=1,column=0)
    last_name.grid(row=1,column=1)
    phnolabel.grid(row=2,column=0)
    phno.grid(row=2,column=1)



    


    ###submit customtkinter.CTkButton function


    def submitbtnfun():
        f_name=first_name.get()
        l_name=last_name.get()
        ph_no=phno.get()


        cur.execute("""
                    INSERT INTO login (username, password,phno) 
                     VALUES (%s, %s,%s)
                    """, (f_name, l_name,ph_no))

        first_name.delete(0,END)
        last_name.delete(0,END)
        phno.delete(0,END)



# customtkinter.CTkButtons of invoice window
    submitbtn=customtkinter.CTkButton(invoicelabelframe,text="Submit",command=submitbtnfun)
    showrecordbtn=customtkinter.CTkButton(invoicelabelframe,text="Show record",command=showrec)
    showrecordbtn.grid(row=4,columnspan=2)

    submitbtn.grid(row=3,columnspan=2)

    

employee_view()
















#customtkinter.CTkButtons of root window
loginadmin=customtkinter.CTkButton(root,text="Login",command=adminfun).pack()

prntinvoice=customtkinter.CTkButton(root,text="Print Invoice",command=prnt_inv).pack()
exitbutton=customtkinter.CTkButton(root,text="exit",command=root.quit).pack()



root.mainloop()