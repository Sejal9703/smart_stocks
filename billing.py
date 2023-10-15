from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="#F9F5F6")
        #====title=====
        #self.icon_title=Image.open("logo1.png")
        title=Label(self.root,text="Smart Stocks",font=("times new roman",40,"bold"),bg="#FFD0D0",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        #====btn=====
        btn_logout=Button(self.root,text="Logout",font=("times new roman",20,"bold"),bg="white",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #====CLK===
        self.lbl_clock=Label(self.root,text="Welcome to SMART STOCKS",font=("times new roman",15),bg="#9BABB8")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #===Product_Frame====
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)
        
        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90) 
        
        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=("Times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)     
        
        lbl_search=Label(ProductFrame2,text="Product Name",font=("Times new roman",15,"bold"),bg="white").place(x=5,y=45) 
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("Times new roman",15),bg="light yellow").place(x=128,y=47,width=150,height=22) 
        btn_search=Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
        
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(ProductFrame3,columns=("PID","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("PID",text="PID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="qty")
        self.product_table.heading("status",text="status")

        self.product_table["show"]="headings"
        
        self.product_table.column("PID",width=90)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=100)
        self.product_table.pack(fill=BOTH,expand=1)
        # self.product_table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note_=Label(ProductFrame1,text="Note:'Enter 0 quantity to remove product from the cart' ",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #===customer frame========
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame1.place(x=420,y=110,width=530,height=70)
        
        cTitle=Label(CustomerFrame1,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame1,text="Name",font=("Times new roman",15),bg="white").place(x=4,y=30) 
        txt_name=Entry(CustomerFrame1,textvariable=self.var_cname,font=("Times new roman",13),bg="light yellow").place(x=80,y=35,width=180) 
        lbl_contact=Label(CustomerFrame1,text="Contact No.",font=("Times new roman",15,),bg="white").place(x=270,y=30) 
        txt_name=Entry(CustomerFrame1,textvariable=self.var_contact,font=("Times new roman",13),bg="light yellow").place(x=380,y=35,width=140) 
        
        #===cal_cart_frame====
        cal_cart_Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        cal_cart_Frame1.place(x=420,y=190,width=530,height=360)
        
        #====cal_frame=======
        self.var_cal_input=StringVar()
        cal_Frame1=Frame(cal_cart_Frame1,bd=9,relief=RIDGE,bg="white")
        cal_Frame1.place(x=5,y=10,width=270,height=340)
        
        
        self.txt_cal_input=Entry(cal_Frame1,textvariable=self.var_cal_input,font=("arial",15,'bold'),width=21,bd=10,relief=GROOVE,state="readonly",justify="right")
        self.txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(cal_Frame1,text="7",font=("arial",15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(cal_Frame1,text="8",font=("arial",15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(cal_Frame1,text="9",font=("arial",15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(cal_Frame1,text="+",font=("arial",15,'bold'),command=lambda:self.get_input("+"),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
        
        btn_4=Button(cal_Frame1,text="4",font=("arial",15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(cal_Frame1,text="5",font=("arial",15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(cal_Frame1,text="6",font=("arial",15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(cal_Frame1,text="-",font=("arial",15,'bold'),command=lambda:self.get_input("-"),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
        
        btn_1=Button(cal_Frame1,text="1",font=("arial",15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(cal_Frame1,text="2",font=("arial",15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(cal_Frame1,text="3",font=("arial",15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(cal_Frame1,text="*",font=("arial",15,'bold'),command=lambda:self.get_input("*"),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
        
        btn_0=Button(cal_Frame1,text="0",font=("arial",15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_clr=Button(cal_Frame1,text="clear",font=("arial",15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)
        btn_equal=Button(cal_Frame1,text="=",font=("arial",15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(cal_Frame1,text="/",font=("arial",15,'bold'),command=lambda:self.get_input("/"),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        
        
        
        
        
        
        
        
        
        
        
        #====cart frame===
        cart_frame=Frame(cal_cart_Frame1,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)
        cart_Title=Label(cart_frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.Carttable=ttk.Treeview(cart_frame,columns=("PID","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Carttable.xview)
        scrolly.config(command=self.Carttable.yview)

        self.Carttable.heading("PID",text="PID")
        self.Carttable.heading("name",text="Name")
        self.Carttable.heading("price",text="Price")
        self.Carttable.heading("qty",text="qty")
        self.Carttable.heading("status",text="status")

        self.Carttable["show"]="headings"
        
        self.Carttable.column("PID",width=40)
        self.Carttable.column("name",width=100)
        self.Carttable.column("price",width=90)
        self.Carttable.column("qty",width=40)
        self.Carttable.column("status",width=90)
        self.Carttable.pack(fill=BOTH,expand=1)
        # self.Carttable_table.bind("<ButtonRelease-1>",self.get_data)
        
        #==add cart widgets frame====
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        
        add_cart_widgets_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        add_cart_widgets_frame.place(x=420,y=550,width=530,height=110)
        
        lbl_p_name=Label(add_cart_widgets_frame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(add_cart_widgets_frame,textvariable=self.var_pname,font=("times new roman",15),bg="light yellow",state="readonly").place(x=5,y=35,width=190,height=22)
        
        lbl_p_price=Label(add_cart_widgets_frame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_q_price=Entry(add_cart_widgets_frame,textvariable=self.var_price,font=("times new roman",15),bg="light yellow",state="readonly").place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty=Label(add_cart_widgets_frame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_q_qty=Entry(add_cart_widgets_frame,textvariable=self.var_qty,font=("times new roman",15),bg="light yellow").place(x=390,y=35,width=120,height=22)
        
        self.lbl_inStock=Label(add_cart_widgets_frame,text="In Stock [9999]",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        
        btn_clear_cart=Button(add_cart_widgets_frame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(add_cart_widgets_frame,text="Add | Update Cart",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
        #====billing area=======
        billframe=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billframe.place(x=953,y=110,width=410,height=410)
        
        BTitle=Label(billframe,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="white",fg="black").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billframe,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billframe,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #===billimg buttons====
        billmenuframe=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billmenuframe.place(x=953,y=520,width=410,height=140)
        
        self.lbl_amt=Label(billmenuframe,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg='#3f51b5',fg='white')
        self.lbl_amt.place(x=2,y=5,width=120,height=70)
        
        self.lbl_discount=Label(billmenuframe,text="Discount\n[5%]",font=("goudy old style",15,"bold"),bg='#8bc34a',fg='white')
        self.lbl_discount.place(x=124,y=5,width=120,height=70)
        
        self.lbl_net_pay=Label(billmenuframe,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg='#607d8b',fg='white')
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)
        
        btn_print=Button(billmenuframe,text="Print",cursor="hand2",font=("goudy old style",15,"bold"),bg='lightgreen',fg='white')
        btn_print.place(x=2,y=80,width=120,height=50)
        
        btn_clear_all=Button(billmenuframe,text="Clear All",cursor="hand2",font=("goudy old style",15,"bold"),bg='gray',fg='white')
        btn_clear_all.place(x=124,y=80,width=120,height=50)
        
        btn_generate=Button(billmenuframe,text="Generate/Save Bill",cursor="hand2",font=("goudy old style",14,"bold"),bg='#009688',fg='white')
        btn_generate.place(x=246,y=80,width=160,height=50)
        
        
        #====footer=======
        footer=Label(self.root,text='IMS-Inventory Management System',font=("times new roman",11),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        



        
        
        
        
        
        
        #====all functions=======
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set('')
         
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
        
        
    
        
        
if __name__=="__main__":  
    root=Tk()
    obj=BillClass(root)
    root.mainloop()