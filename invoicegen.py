from tkinter import *
from tkinter import messagebox
import psycopg2



root=Tk()

custom_font = ('Helvetica', 20)




#connect to database

conn = psycopg2.connect(
   database="management", user='postgres', password='pgadmin4', host='127.0.0.1', port= '5432')
cur=conn.cursor()

conn.autocommit = True

#admin login function



        



    


#admin function

def adminfun():



    def clear_window(admin1):
        # Destroy all widgets in the window
        for widget in admin1.winfo_children():
             widget.destroy()

    def addproductfun():
             clear_window(admin) 
             productlabelframe=LabelFrame(admin,text="ADD Product",font=custom_font,padx=25,pady=10)
             productlabelframe.pack(pady=60)
             namelabel=Label(productlabelframe, text="Name: ").grid(row=1,column=0,padx=5)  
             nameinput=Entry(productlabelframe).grid(row=1,column=1,padx=5,pady=10)
             catagorylabel=Label(productlabelframe, text="Catagory: ").grid(row=2, column=0)
             catagoryinput=Entry(productlabelframe).grid(row=2, column=1)
             priceLabel=Label(productlabelframe, text="Price($):").grid(row=3,column=0)
             priceInput=Entry(productlabelframe).grid(row=3,column=1,pady=10)
             stocklabel=Label(productlabelframe,text="Stock Quantity:")
             stocklabel.grid(row=4,column=0)
             stockentry=Entry(productlabelframe).grid(row=4,column=1)





    




    def loginfun():
       

        adminusername=uname_input_admin.get()
        adminpass=pass_input_admin.get()
    

        if adminusername=="admin" and adminpass=="admin" :
             
             clear_window(admin)
             messagebox.showinfo("Successful login","You are loged in as "+adminusername)
             #add prodrct

             addproductbtn=Button(admin,text="Add product", command=addproductfun).pack()
             


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

    loginbtn=Button(admin_login_frame,text="Login",command=loginfun).pack(pady=10)
    
       








######### print_inv function



def prnt_inv():
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



    


    ###submit button function


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



# buttons of invoice window
    submitbtn=Button(invoicelabelframe,text="Submit",command=submitbtnfun)
    showrecordbtn=Button(invoicelabelframe,text="Show record",command=showrec)
    showrecordbtn.grid(row=4,columnspan=2)

    submitbtn.grid(row=3,columnspan=2)









#buttons of root window
loginadmin=Button(root,text="Login",command=adminfun).pack()

prntinvoice=Button(root,text="Print Invoice",command=prnt_inv).pack()
exitbutton=Button(root,text="exit",command=root.quit).pack()



root.mainloop()