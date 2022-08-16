from tkinter import *
from tkinter import ttk
class Employee:
    
    def __init__(self, root):
        self.root = root
        self.root.title("EMPLOYEE MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")
        #=================== MENU BAR PLACE AND FEATURES================================
        my_menu=Menu(root)
        root.config(menu=my_menu)
        #=====================click commmand========
        def our_command():
            pass
        #====================file menu bar ===================================
        file_menu=Menu(my_menu)
        my_menu.add_cascade(label="FILE",menu=file_menu)
        file_menu.add_command(label="IMPORT EXCEL",command=our_command)
        file_menu.add_separator()
        file_menu.add_command(label="EXPORT EXCEL",command=our_command)
        file_menu.add_separator()
        file_menu.add_command(label="SAVE",command=our_command)
        file_menu.add_separator()
        file_menu.add_command(label="SAVE AS",command=our_command)
        file_menu.add_separator()
        file_menu.add_command(label="SAVE COPY AS",command=our_command)
        file_menu.add_separator()
        file_menu.add_command(label="PRINT",command=our_command)
        file_menu.add_separator()
        file_menu.add_command(label="EXIT",command=root.quit)
       
        
        #====================Edit menu bar ===================================
        edit_menu=Menu(my_menu)
        my_menu.add_cascade(label=" EDIT ",menu=edit_menu)
        edit_menu.add_command(label="UNDO",command=our_command)
        edit_menu.add_separator()
        edit_menu.add_command(label="REDO",command=our_command)
        edit_menu.add_separator()
        edit_menu.add_command(label="COPY",command=our_command)
        edit_menu.add_separator()
        edit_menu.add_command(label="CUT",command=our_command)
        edit_menu.add_separator()
        edit_menu.add_command(label="PASTE",command=our_command)
        edit_menu.add_separator()
        edit_menu.add_command(label="SELECT ALL",command=our_command)
        edit_menu.add_separator()
        edit_menu.add_command(label="FIND",command=our_command)

        

        #=================tab======================
        my_notebook=ttk.Notebook(root)
        my_notebook.pack(pady=0)
        my_Tab1=Frame(my_notebook,width=1380,height=2000,bg="light blue")
     
        my_Tab2=Frame(my_notebook,width=1380,height=2000,bg="light blue")
        my_Tab3=Frame(my_notebook,width=1380,height=2000,bg="light blue")
      
        my_Tab1.pack(fill="both",expand=1)
        my_Tab2.pack(fill="both",expand=1)
        my_Tab3.pack(fill="both",expand=1)
        my_notebook.add(my_Tab1,text="  TAB 1  ")
        my_notebook.add(my_Tab2,text="  TAB 2  ")
        my_notebook.add(my_Tab3,text="  TAB 3  ")





        #---------------------------------------------------------------------tab 1----------------------------------------------------------------------------------
        # ================= main left frame 1 property======================
        Frame1 = Frame(my_Tab1, bd=4, relief=RIDGE, bg="light blue")
        Frame1.place(x=5, y=2, width=494, height=655)
        # =================MACHINE frame1==========================
        lb1_mch = Label(Frame1, text="MACHINE : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_mch.grid(row=0, column=0, pady=1, padx=3, sticky="W")
         # ================= text machine drop down frame 1=====================
        combo_mch = ttk.Combobox(Frame1, font=("times new roman", 13, "bold"), state='randomly')
        combo_mch['value'] = ("POLLY_PREPARATION", "POLL_MAKING", "CY_PREPARATION", "CY_MAKING", "WEFT", "SHOW ALL")
        combo_mch.grid(row=0, column=1, padx=5, pady=10)
        
        # =====================DATE frame1======================
        lb1_date = Label(Frame1, text="DATE : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_date.grid(row=1, column=0, pady=1, padx=3, sticky="W")
        #========================TXT SPACE FRAME 1 DATE=========================
        txt_date= Entry(Frame1, font=("times new roman", 14, "bold"),bd=2)
        txt_date.grid(row=1, column=1, pady=2, padx=5, sticky="w")
        
        # =====================order no frame 1======================
        lb1_orderno = Label(Frame1, text="ORDER NO : ", bg="light blue", fg="black", font=("times new roman",14, "bold"))
        lb1_orderno.grid(row=2, column=0, pady=10, padx=5, sticky="W")
        #========================TXT SPACE order no frame 1========================
        txt_orderno = Entry(Frame1, font=("times new roman", 14, "bold"),bd=3,relief=GROOVE)
        txt_orderno.grid(row=2, column=1, pady=10, padx=5, sticky="w")
        # =====================ITEAM frame 1======================
        lb1_item = Label(Frame1, text="ITEM : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_item.grid(row=3, column=0, pady=10, padx=5, sticky="W")
         #========================TXT SPACE  ITEM frame1=========================
        txt_item = Entry(Frame1, font=("times new roman", 14, "bold"),bd=3,relief=GROOVE)
        txt_item.grid(row=3, column=1, pady=10, padx=5, sticky="w")
        # =====================QUANTITY frame1======================
        lb1_Quantity = Label(Frame1, text="QUANTITY : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_Quantity.grid(row=4, column=0, pady=10, padx=5, sticky="W")
        #========================TXT SPACE FRAME 1 Quantity=========================
        txt_Quantity = Entry(Frame1, font=("times new roman", 14, "bold"),bd=3,relief=GROOVE)
        txt_Quantity.grid(row=4, column=1, pady=10, padx=5, sticky="w")
         # =====================TASK frame1======================
        lb1_task = Label(Frame1, text="TASK : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_task.grid(row=5, column=0, pady=10, padx=5, sticky="W")
         # =================TASK drop down frame 1=====================
        combo_task = ttk.Combobox(Frame1, font=("times new roman", 13, "bold"))
        combo_task['value'] = ("POLLY_PREPARATION", "POLL_MAKING", "CY_PREPARATION", "CY_MAKING", "WEFT")
        combo_task.grid(row=5, column=1, padx=5, pady=10)
         # =====================TIME REQUIRED frame 1=====================
        lb1_mch = Label(Frame1, text="REQUIRED TIME : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_mch.grid(row=6, column=0, pady=10, padx=5, sticky="W")
        #========================TXT SPACE time required frame 1=========================
        txt_search = Entry(Frame1, font=("times new roman", 14, "bold"),bd=3,relief=GROOVE)
        txt_search.grid(row=6, column=1, pady=10, padx=5, sticky="w")
         # ============ btn3 ADD AND INSERT==========
        btn3_Frame = Frame(Frame1, bd=4, relief=RIDGE, bg="light blue")
        btn3_Frame.place(x=1, y=345, width=483, height=150)
        # =================search btn3_ frame==========================
        lb1_mch = Label(btn3_Frame, text="SEARCH : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_mch.grid(row=0, column=0, pady=1, padx=3, sticky="W")
         # ================= text search drop down frame 1=====================
        combo_mch = ttk.Combobox(btn3_Frame, font=("times new roman", 13, "bold"), state='randomly')
        combo_mch['value'] = ("DATE", "ORDER NO", "ITEM NAME","QUANTITY","TASK", "SHOW ALL")
        combo_mch.grid(row=0, column=1, padx=85, pady=10)
        # ===============lable value txt area===============================
        txt_search = Entry(btn3_Frame, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=2, column=1, pady=10, padx=85, sticky="w")
        # ========================submit value to SEARCH====================
        submitsearch = Button(btn3_Frame, bd=4, text="SEARCH", width=14)
        submitsearch.grid(row=3, column=1, padx=15, pady=1)
        # ============ btn4 FILTER==========================================
        btn5_Frame = Frame(Frame1, bd=4, relief=RIDGE, bg="light blue")
        btn5_Frame.place(x=1, y=495, width=483, height=153)
        # =================search btn3_ frame==========================
        lb1_mch = Label(btn5_Frame, text="FILTER : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_mch.grid(row=0, column=0, pady=1, padx=3, sticky="W")
         # ================= text FILTER drop down frame 1=====================
        combo_mch = ttk.Combobox(btn5_Frame, font=("times new roman", 13, "bold"), state='randomly')
        combo_mch['value'] = ("DATE", "ORDER NO", "ITEM NAME","QUANTITY", "TASK", "SHOW ALL")
        combo_mch.grid(row=0, column=1, padx=85, pady=10)
        # ===============lable value txt area===============================
        txt_search = Entry(btn5_Frame, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=2, column=1, pady=10, padx=85, sticky="w")
        # ========================submit value to SEARCH====================
        submitsearch = Button(btn5_Frame, bd=4, text="FILTER", width=14)
        submitsearch.grid(row=3, column=1, padx=15, pady=1)
        
        #=====================================main right frame 2 property=====================================================================================
        # ====================frame 2=========================
        Frame2 = Frame(my_Tab1, bd=4, relief=RIDGE, bg="sky blue")
        Frame2.place(x=498, y=2, width=860, height=655) 
        # =================frame2 BTN2===========================
        btn1_Frame = Frame(Frame2, bd=5, relief=RIDGE, bg="light blue")
        btn1_Frame.place(x=3, y=580, width=848)
        # ==================add button=============================
        Addbtn = Button(btn1_Frame, bd=4, text="ADD", width=14)
        Addbtn.grid(row=0, column=0, padx=18, pady=10)
        # =========================insert=========================
        Insertbtn = Button(btn1_Frame, bd=4, text="INSERT", width=14)
        Insertbtn.grid(row=0, column=1, padx=10, pady=10)
        # =====================update=============
        updatebtn = Button(btn1_Frame, bd=4, text="UPDATE", width=14)
        updatebtn.grid(row=0, column=2, padx=10, pady=10)
        # ==================delete==================
        Deletebtn = Button(btn1_Frame,bd=4, text="DELETE", width=14)
        Deletebtn.grid(row=0, column=3, padx=10, pady=10)
        # ===============priority========================
        sortbtn = Button(btn1_Frame, bd=4, text="SORT", width=14)
        sortbtn.grid(row=0, column=4, padx=10, pady=13)
        # ================PRINT======================
        Printbtn = Button(btn1_Frame, bd=4, text="PRINT", width=14)
        Printbtn.grid(row=0, column=5, padx=10, pady=10)
        # ======================table frame=============
        Table_Frame = Frame(Frame2, bd=4, relief=RIDGE, bg="light blue")
        Table_Frame.place(x=3, y=50, width=848, height=525)
         # =======================SCROLE BAR=====================
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        Employee_table = ttk.Treeview(Table_Frame, columns=("DATE","ORDER NO","ITEM","QUANTITY","TASK","TIME REQUIRED"), xscrollcommand=scroll_x,
                                      yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Employee_table.xview)
        scroll_y.config(command=Employee_table.yview)
        Employee_table.heading("DATE", text="DATE")
        Employee_table.heading("ORDER NO", text="ORDER NO")
        Employee_table.heading("ITEM", text="ITEM")
        Employee_table.heading("QUANTITY", text="QUANTITY")
        Employee_table.heading("TASK", text="TASK")
        Employee_table.heading("TIME REQUIRED", text="TIME REQUIRED")

        Employee_table['show'] = 'headings'
        Employee_table.column("DATE", width=50)
        Employee_table.column("ORDER NO", width=50)
        Employee_table.column("ITEM", width=100)
        Employee_table.column("QUANTITY", width=50)
        Employee_table.column("TASK", width=100)
        Employee_table.column("TIME REQUIRED", width=100)
        
        Employee_table.pack(fill=BOTH, expand=1)
      
        


        #------------------------------------------------------------------------tab2----------------------------------------------------------------------------


         # ================= main left frame 1 property======================
        Frame6 = Frame(my_Tab2, bd=4, relief=RIDGE, bg="light blue")
        Frame6.place(x=5, y=2, width=494, height=655)
        # =================ORDER NO frame1==========================
        lb1_mch = Label(Frame6, text="ORDER NO : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_mch.grid(row=0, column=0, pady=1, padx=3, sticky="W")
        # ===============lable value ORDER NO===============================
        txt_addvalueemp = Entry(Frame6, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueemp.grid(row=0, column=1, pady=10, padx=5, sticky="w")
         # ==============add value PENDING TASK=================
        lbl_addvalueavg = Label(Frame6, text="PENDING TASK :", bg="LIGHT BLUE", fg="BLACK", font=("times new roman", 15, "bold"))
        lbl_addvalueavg.grid(row=1, column=0, pady=10, padx=5, sticky="w")
        # ==============lable value PENDING TASK===================
        txt_addvalueavg = Entry(Frame6, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueavg.grid(row=1, column=1, pady=10, padx=5, sticky="w")
        # =============  add value(START TIME)==================================
        lbl_addvalueemp = Label(Frame6, text="START TIME :", bg="LIGHT BLUE", fg="BLACK",
                                font=("times new roman", 15, "bold"))
        lbl_addvalueemp.grid(row=2, column=0, pady=10, padx=5, sticky="w")
        #========================TXT SPACE START frame 1========================
        txt_orderno = Entry(Frame6 , font=("times new roman", 14, "bold"),bd=5,relief=GROOVE)
        txt_orderno.grid(row=2, column=1, pady=10, padx=5, sticky="w")
         # =============  add value(END TIME)==================================
        lbl_addvalueemp = Label(Frame6, text="END TIME :", bg="LIGHT BLUE", fg="BLACK",
                                font=("times new roman", 15, "bold"))
        lbl_addvalueemp.grid(row=3, column=0, pady=10, padx=5, sticky="w")
            # =============  add value MACHINE NUMBER==================================
        lbl_addvalueemp = Label(Frame6, text="MACHINE NUMBER :", bg="LIGHT BLUE", fg="BLACK",
                                font=("times new roman", 15, "bold"))
        lbl_addvalueemp.grid(row=4, column=0, pady=10, padx=5, sticky="w")
              # =============  add value(EMPLOYEE NAME)==================================
        lbl_addvalueemp = Label(Frame6, text="EMPLOYEE NAME :", bg="LIGHT BLUE", fg="BLACK",
                                font=("times new roman", 15, "bold"))
        lbl_addvalueemp.grid(row=5, column=0, pady=10, padx=5, sticky="w")
          # ===============lable value END TIME===============================
        txt_addvalueemp = Entry(Frame6, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueemp.grid(row=3, column=1, pady=10, padx=5, sticky="w")
         # ===============lable value MACHINE NUMBER===============================
        txt_addvalueemp = Entry(Frame6, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueemp.grid(row=4, column=1, pady=10, padx=5, sticky="w")
          # ===============lable value EMPLOYEE NAME===============================
        txt_addvalueemp = Entry(Frame6, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueemp.grid(row=5, column=1, pady=10, padx=5, sticky="w")
        # ============ btn3 search==========
        btn7_Frame = Frame(Frame6, bd=4, relief=RIDGE, bg="light blue")
        btn7_Frame.place(x=1, y=345, width=483, height=150)
        # =================search btn3_ frame==========================
        lb1_mch = Label(btn7_Frame, text="SEARCH : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_mch.grid(row=0, column=0, pady=1, padx=3, sticky="W")
         # ================= text search drop down frame 1=====================
        combo_mch = ttk.Combobox(btn7_Frame, font=("times new roman", 13, "bold"), state='randomly')
        combo_mch['value'] = ("ORDER NO","PENDING TASK","START","END","MACHINE NO","EMPLOYEE NAME")
        combo_mch.grid(row=0, column=1, padx=85, pady=10)
        # ===============lable value txt area===============================
        txt_search = Entry(btn7_Frame, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=2, column=1, pady=10, padx=85, sticky="w")
        # ========================submit value to SEARCH====================
        submitsearch = Button(btn7_Frame, bd=4, text="SEARCH", width=14)
        submitsearch.grid(row=3, column=1, padx=15, pady=1)
        # ============ btn4 FILTER==========================================
        btn8_Frame = Frame(Frame6, bd=4, relief=RIDGE, bg="light blue")
        btn8_Frame.place(x=1, y=495, width=483, height=153)
        # =================search btn3_ frame==========================
        lb1_mch = Label(btn8_Frame, text="FILTER : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_mch.grid(row=0, column=0, pady=1, padx=3, sticky="W")
         # ================= text FILTER drop down frame 1=====================
        combo_mch = ttk.Combobox(btn8_Frame, font=("times new roman", 13, "bold"), state='randomly')
        combo_mch['value'] = ("ORDER NO","PENDING TASK","START","END","MACHINE NO","EMPLOYEE NAME")
        combo_mch.grid(row=0, column=1, padx=85, pady=10)
        # ===============lable value txt area===============================
        txt_search = Entry(btn8_Frame, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=2, column=1, pady=10, padx=85, sticky="w")
        # ========================submit value to SEARCH====================
        submitsearch = Button(btn8_Frame, bd=4, text="FILTER", width=14)
        submitsearch.grid(row=3, column=1, padx=15, pady=1)
     
        # ====================main rigth frame 3========================================================================
        Frame3 = Frame(my_Tab2, bd=4, relief=RIDGE, bg="light blue")
        Frame3.place(x=498, y=2, width=860, height=655) 
        # =================frame5 BTN2===========================
        btn6_Frame = Frame(Frame3, bd=5, relief=RIDGE, bg="light blue")
        btn6_Frame.place(x=3, y=580, width=848)
        # ======================table2 frame=============
        Table4_Frame = Frame(Frame3, bd=4, relief=RIDGE, bg="light blue")
        Table4_Frame.place(x=3, y=50, width=845, height=525)
        # =======================SCROLE BAR FRAME2 TABLE2=====================
        scroll_x = Scrollbar(Table4_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table4_Frame, orient=VERTICAL)
        Employee_table = ttk.Treeview(Table4_Frame, columns=("ORDER NO","PENDING TASK","START","END","MACHINE NO","EMPLOYEE NAME"), xscrollcommand=scroll_x,
                                      yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Employee_table.xview)
        scroll_y.config(command=Employee_table.yview)
        Employee_table.heading("ORDER NO", text="ORDER NO")
        Employee_table.heading("PENDING TASK", text="PENDING TASK")
        Employee_table.heading("START", text="START TIME")
        Employee_table.heading("END", text="END TIME")
        Employee_table.heading("MACHINE NO", text="MACHINE NUMBER")
        Employee_table.heading("EMPLOYEE NAME", text="EMPLOYEE NAME")

        Employee_table['show'] = 'headings'
        Employee_table.column("ORDER NO", width=100)
        Employee_table.column("PENDING TASK", width=100)
        Employee_table.column("START", width=100)
        Employee_table.column("END", width=100)
        Employee_table.column("MACHINE NO", width=100)
        Employee_table.column("EMPLOYEE NAME", width=100)
               
    
        
        Employee_table.pack(fill=BOTH, expand=1)
        # =================frame4BTN2=========================
        btn2_Frame = Frame(Frame3, bd=5, relief=RIDGE, bg="light blue")
        btn2_Frame.place(x=3, y=580, width=848)
        # ==================add button=============================
        Addbtn = Button(btn2_Frame, bd=4, text="ADD", width=14)
        Addbtn.grid(row=0, column=0, padx=18, pady=10)
        # =========================insert=========================
        Insertbtn = Button(btn2_Frame, bd=4, text="INSERT", width=14)
        Insertbtn.grid(row=0, column=1, padx=10, pady=10)
        # =====================update=============
        updatebtn = Button(btn2_Frame, bd=4, text="UPDATE", width=14)
        updatebtn.grid(row=0, column=2, padx=10, pady=10)
        # ==================delete==================
        Deletebtn = Button(btn2_Frame, bd=4, text="DELETE", width=14)
        Deletebtn.grid(row=0, column=3, padx=10, pady=10)
        
        # ===============priority========================
        sortbtn = Button(btn2_Frame, bd=4, text="SORT", width=14)
        sortbtn.grid(row=0, column=4, padx=10, pady=13)
        # ================Print======================
        Printbtn = Button(btn2_Frame, bd=4, text="PRINT", width=14)
        Printbtn.grid(row=0, column=5, padx=10, pady=10)
        
        




        #----------------------------------------------------------------------------TAB3-----------------------------------------------------------------------



        # ================= main left frame 4 property======================
        Frame4= Frame(my_Tab3, bd=4, relief=RIDGE, bg="light blue")
        Frame4.place(x=5, y=2, width=494, height=655)
       
        # =============  add value(emp name)==================================
        lbl_addvalueemp = Label(Frame4, text="EMPLOYEE NAME :", bg="LIGHT BLUE", fg="BLACK",
                                font=("times new roman", 15, "bold"))
        lbl_addvalueemp.grid(row=0, column=0, pady=1, padx=3, sticky="W")
        # ==============add value(average)=================
        lbl_addvalueavg = Label(Frame4, text="AVERAGE :", bg="LIGHT BLUE", fg="BLACK", font=("times new roman", 15, "bold"))
        lbl_addvalueavg.grid(row=1, column=0, pady=10, padx=5, sticky="w")
        # =============  add value(TASK)==================================
        lbl_addvalueemp = Label(Frame4, text="TASK :", bg="LIGHT BLUE", fg="BLACK",
                                font=("times new roman", 15, "bold"))
        lbl_addvalueemp.grid(row=2, column=0, pady=10, padx=5, sticky="w")
         # =============  add value(START TIME)==================================
        lbl_addvalueemp = Label(Frame4, text="START TIME :", bg="LIGHT BLUE", fg="BLACK",
                                font=("times new roman", 15, "bold"))
        lbl_addvalueemp.grid(row=3, column=0, pady=10, padx=5, sticky="w")
            # =============  add value(END TIME)==================================
        lbl_addvalueemp = Label(Frame4, text="END TIME :", bg="LIGHT BLUE", fg="BLACK",
                                font=("times new roman", 15, "bold"))
        lbl_addvalueemp.grid(row=4, column=0, pady=10, padx=5, sticky="w")
              # =============  add value(AVAILBLE)==================================
        lbl_addvalueemp = Label(Frame4, text="AVAILBLE :", bg="LIGHT BLUE", fg="BLACK",
                                font=("times new roman", 15, "bold"))
        lbl_addvalueemp.grid(row=5, column=0, pady=10, padx=5, sticky="w")
          # ===============lable value employee name===============================
        txt_addvalueemp = Entry(Frame4, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueemp.grid(row=0, column=1, pady=10, padx=5, sticky="w")
          # ==============lable value average===================
        txt_addvalueavg = Entry(Frame4, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueavg.grid(row=1, column=1, pady=10, padx=5, sticky="w")
         # =================TASK drop down frame 1=====================
        combo_task = ttk.Combobox(Frame4, font=("times new roman", 13, "bold"))
        combo_task['value'] = ("POLLY_PREPARATION", "POLL_MAKING", "CY_PREPARATION", "CY_MAKING", "WEFT")
        combo_task.grid(row=2, column=1, padx=5, pady=10)
       # ===============lable value START TIME===============================
        txt_addvalueemp = Entry(Frame4, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueemp.grid(row=3, column=1, pady=10, padx=5, sticky="w")
         # ===============lable value END TIME===============================
        txt_addvalueemp = Entry(Frame4, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueemp.grid(row=4, column=1, pady=10, padx=5, sticky="w")
          # ===============lable value  AVAILABLE===============================
        txt_addvalueemp = Entry(Frame4, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_addvalueemp.grid(row=5, column=1, pady=10, padx=5, sticky="w")
          # ============ btn3 search==========
        btn4_Frame = Frame(Frame4, bd=4, relief=RIDGE, bg="light blue")
        btn4_Frame.place(x=1, y=345, width=483, height=150)
        # =================search btn3_ frame==========================
        lb1_mch = Label(btn4_Frame, text="SEARCH : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_mch.grid(row=0, column=0, pady=1, padx=3, sticky="W")
         # ================= text search drop down frame 1=====================
        combo_mch = ttk.Combobox(btn4_Frame, font=("times new roman", 13, "bold"), state='randomly')
        combo_mch['value'] = ("EMPLOYEE NAME", "AVERAGE", "TASK", "SHOW ALL")
        combo_mch.grid(row=0, column=1, padx=85, pady=10)
        # ===============lable value txt area===============================
        txt_search = Entry(btn4_Frame, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=2, column=1, pady=10, padx=85, sticky="w")
        # ========================submit value to SEARCH====================
        submitsearch = Button(btn4_Frame, bd=4, text="SEARCH", width=14)
        submitsearch.grid(row=3, column=1, padx=15, pady=1)
        # ============ btn4 FILTER==========================================
        btn5_Frame = Frame(Frame4, bd=4, relief=RIDGE, bg="light blue")
        btn5_Frame.place(x=1, y=495, width=483, height=153)
        # =================search btn3_ frame==========================
        lb1_mch = Label(btn5_Frame, text="FILTER : ", bg="light blue", fg="black", font=("times new roman", 14, "bold"))
        lb1_mch.grid(row=0, column=0, pady=1, padx=3, sticky="W")
         # ================= text FILTER drop down frame 1=====================
        combo_mch = ttk.Combobox(btn5_Frame, font=("times new roman", 13, "bold"), state='randomly')
        combo_mch['value'] = ("EMPLOYEE NAME", "AVERAGE", "TASK", "SHOW ALL")
        combo_mch.grid(row=0, column=1, padx=85, pady=10)
        # ===============lable value txt area===============================
        txt_search = Entry(btn5_Frame, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=2, column=1, pady=10, padx=85, sticky="w")
        # ========================submit value to SEARCH====================
        submitsearch = Button(btn5_Frame, bd=4, text="FILTER", width=14)
        submitsearch.grid(row=3, column=1, padx=15, pady=1)
        
        
    
      
       

        #-----------------------------------------------------------main right frame 5 property--------------------------------------------------------------------
        # ====================frame 5=========================
        Frame5 = Frame(my_Tab3, bd=4, relief=RIDGE, bg="light blue")
        Frame5.place(x=498, y=2, width=865, height=655)
         # ============ btn4 ADD AND INSERT==========
        table1_Frame = Frame(Frame5, bd=4, relief=RIDGE, bg="light blue")
        table1_Frame.place(x=3, y=50, width=850, height=525)
       
        # =======================SCROLE BAR=====================
        scroll_x = Scrollbar(table1_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table1_Frame, orient=VERTICAL)
        Employee_table = ttk.Treeview(table1_Frame, columns=("EMPLOYEE NAME", "AVERAGE","TASK","START TIME","END TIME","AVAILBLE"), xscrollcommand=scroll_x,
                                      yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Employee_table.xview)
        scroll_y.config(command=Employee_table.yview)
        Employee_table.heading("EMPLOYEE NAME", text="EMPLOYEE NAME")
        Employee_table.heading("AVERAGE", text="AVERAGE")
        Employee_table.heading("TASK", text="TASK")
        Employee_table.heading("START TIME", text="START TIME")
        Employee_table.heading("END TIME", text="END TIME")
        Employee_table.heading("AVAILBLE", text="AVAILBLE")

        Employee_table['show'] = 'headings'
        Employee_table.column("EMPLOYEE NAME", width=100)
        Employee_table.column("AVERAGE", width=100)
        Employee_table.column("TASK", width=100)
        Employee_table.column("START TIME", width=100)
        Employee_table.column("END TIME", width=100)
        Employee_table.column("AVAILBLE", width=100)
       
       
        Employee_table.pack(fill=BOTH, expand=1)
            
        
        # =================frame4BTN2=========================
        btn3_Frame = Frame(Frame5, bd=5, relief=RIDGE, bg="light blue")
        btn3_Frame.place(x=3, y=580, width=848)
        # ==================add button=============================
        Addbtn = Button(btn3_Frame, bd=4, text="ADD", width=14)
        Addbtn.grid(row=0, column=0, padx=18, pady=10)
        # =========================insert=========================
        Insertbtn = Button(btn3_Frame, bd=4, text="INSERT", width=14)
        Insertbtn.grid(row=0, column=1, padx=10, pady=10)
        # =====================update=============
        updatebtn = Button(btn3_Frame, bd=4, text="UPDATE", width=14)
        updatebtn.grid(row=0, column=2, padx=10, pady=10)
        # ==================delete==================
        Deletebtn = Button(btn3_Frame, bd=4, text="DELETE", width=14)
        Deletebtn.grid(row=0, column=3, padx=10, pady=10)
         # ================PRINT======================
        Printbtn = Button(btn3_Frame, bd=4, text="PRINT", width=14)
        Printbtn.grid(row=0, column=5, padx=10, pady=10)
     
       
        # ===============priority========================
        sortbtn = Button(btn3_Frame, bd=4, text="SORT", width=14)
        sortbtn.grid(row=0, column=4, padx=10, pady=13)
        
       
       

        







        
root = Tk()
#my_time()
ob = Employee(root)
root = mainloop()
