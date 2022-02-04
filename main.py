from tkinter import *
import tkinter
import time
from PIL import ImageTk, Image
import pyautogui as pyt
from chempy import Substance
from chempy import balance_stoichiometry
from chempy.util import periodic as prd
from tkinter import messagebox
from chempy import balance_stoichiometry
from chempy import mass_fractions
from chempy import Equilibrium
a=Tk()
a.maxsize(1366,768)
a.minsize(1366,768)
a.iconbitmap("icon.ico")
a.title("Balancing stoichiometry of a chemical reaction/Balancing reactions/Chemical equilibria/Chemical kinetics (system of ordinary differential equations)")
#a.wm_attributes('-transparentcolor', 'green')
image1 = Image.open('background.jpg').resize((1366,768))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)

image1 = Image.open('img1.jpg').resize((220,330))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=1130, y=250)

#,bg="#ab23ff"
def formula():
    x=var.get()
    try:
        ff=Substance.from_formula(x)
        pyt.alert(" Your Component Unicode name is {} \n\n Latex Name :- {} \n\n Html  Name :- {} \n\n Mass :- {} \n\n Composition :- {} \n\n Charge :- {} ".format(ff.unicode_name,ff.latex_name,ff.html_name,ff.mass,ff.composition,ff.charge))
    except:
        messagebox.showwarning("Warning","Please write correct component name according to periodic table like \n\n\t\tC6H6 (Benzene)")
        #pyt.alert("Component Symbols :- {}\n\n".format([i for i in prd.symbols]))
def all_component():
    messagebox.showwarning("Component Symbol ","Component Symbol :- {} \n\n".format([i for i in prd.symbols]))
def all_names():
    messagebox.showwarning("Component  Name ","Component Name :- {} \n\n".format([i for i in prd.names]))
def all_molar_mass():
    a=prd.names
    b=prd.relative_atomic_masses
    d={}
    for i in range(118):
        d[a[i]]=b[i]
    messagebox.showwarning("Component Mass","Component Mass :- {} \n\n".format(d))
def periodic_table():
    import os
    os.system("python table.py")
def evaluate1():
    a=int(var1.get())
    b=set()
    for i in range(a):
        a=pyt.prompt('Enter Left Substance Element Name')
        b.add(a)
    return b
    #reac, prod = balance_stoichiometry(a,b)
    #{'NH4ClO4', 'Al'}, {'Al2O3', 'HCl', 'H2O', 'N2'}
    #pyt.alert(reac)
    #pyt.alert(prod)
def evaluate2():
    a=int(var2.get())
    b=set()
    for i in range(a):
        a=pyt.prompt('Enter Right Substance Element Name')
        b.add(a)
    return b
def final_evaluation():
    a=evaluate1()
    b=evaluate2()
    d={}
    reac, prod = balance_stoichiometry(a,b)
    d.update(reac)
    d.update(prod)
    pyt.alert("Balanced Left Substance Equation  :- {} \n\n Balanced Right Substance Equation :- {} \n\n Complete Equation :- {}".format(reac,prod,d))
    return reac,prod
def fraction_mass():
    reac,prod=final_evaluation()
    for fractions in map(mass_fractions, [reac, prod]):
        a={k: '{0:.3g} wt%'.format(v*100) for k, v in fractions.items()}
        pyt.alert(a)
def hint():
    a=' 1.) Choose Number of Left Substance Length \n 2.) Choose Number of Right Substance Length \n 3.) Click On Final Evaluation \n 4.) Enter the Left Substance name one-by-one when prompt is open \n 5.) Enter the Right Substance name one-by-one when prompt is open \n 6.) You follow these steps correctly then you got your balanced \n       equation'
    pyt.alert(a)

def search_by_symbol():
    a=prd.symbols
    b=prd.names
    c=var3.get()
    d={}
    for i in range(118):
        d[a[i]]=b[i]
    if c in d:
        messagebox.showwarning("Element Name",d[c])
    else:
        messagebox.showwarning("Warning","No Data Found")
def search_by_mass():
    a=prd.relative_atomic_masses
    b=prd.names
    c=int(var3.get())
    d={}
    for i in range(118):
        d[int(a[i])]=b[i]
    if c in d:
        messagebox.showwarning("Element Name",d[c])
    else:
        messagebox.showwarning("Warning","No Data Found")
def find_atomic_number():
    a=var3.get()
    messagebox.showwarning("Atomic Number ","Atomic Number is  :- {} ".format(prd.atomic_number(a)))
def periodic_group():
    messagebox.showwarning("Periodic Group","Periodic Group :- {} ".format(prd.groups))
def period_length():
    messagebox.showwarning("Periodic Length","Period Length :- {} ".format(prd.period_lengths))
def Equalibrium_1():
    a=int(var4.get())
    b=int(var5.get())
    aa={}
    bb={}
    for i in range(a):
        c=pyt.prompt("Enter Your Left Element name with charge")
        d=pyt.prompt("Enter your left coefficient")
        aa[c]=int(d)
    for i in range(b):
        c=pyt.prompt("Enter Your Right Element name with charge")
        d=pyt.prompt("Enter your right coefficient")
        bb[c]=int(d)
    return aa,bb

def Equalibrium_2():
    a=int(var6.get())
    b=int(var7.get())
    aa={}
    bb={}
    for i in range(a):
        c=pyt.prompt("Enter Your Left Element name with charge")
        d=pyt.prompt("Enter your right coefficient")
        aa[c]=int(d)
    for i in range(b):
        c=pyt.prompt("Enter Your Right Element name with charge")
        d=pyt.prompt("Enter your right coefficient")
        bb[c]=int(d)
    return aa,bb
def evaluate():
    messagebox.showwarning("Equalibrium 1","This is for First Equalibrium make sure you entered right length")
    a,b=Equalibrium_1()
    messagebox.showwarning("Equalibrium 1","Your First Equalibrium Equation is :- \n\n for left {} \n\n for right {} ".format(a,b))
    messagebox.showwarning("Equalibrium 2","This is for Second Equalibrium make sure you entered right length")
    c,d=Equalibrium_2()
    messagebox.showwarning("Equalibrium 2","Your Second Equalibrium Equation is :- \n\n for left {} \n\n for right {} ".format(c,d))
    e1=Equilibrium(a,b)
    e2=Equilibrium(c,d)
    coeff = Equilibrium.eliminate([e1, e2], 'e-')
    #print(coeff)
    redox = e1*coeff[0] + e2*coeff[1]
    #print(redox)
    pyt.alert(" Your Coefficient Of the Equation is : - {} \n\n Your Complete Redox Reaction is :- \n\n {} ".format(coeff,redox))
lb=Label(a,text="Balancing stoichiometry of a chemical reaction",font=("Arial",45)).place(x=60,y=10)
var=StringVar()
et3=Entry(a,fg="green",font=("Arial",18),borderwidth = 5,textvariable=var)
et3.insert(0,'FeCN6-3')
et3.place(x=10,y=130)
btn=Button(a,text="Formula",bd=4,font=("Arial",14,"bold"),command=formula).place(x=320,y=130)
btn=Button(a,text="Show All Component Symbol ",bd=4,font=("Arial",14,"bold"),command=all_component).place(x=400,y=200)
btn=Button(a,text="Show All Component Name ",bd=4,font=("Arial",14,"bold"),command=all_names).place(x=700,y=130)
btn=Button(a,text="Show All Component Mass ",bd=4,font=("Arial",14,"bold"),command=all_molar_mass).place(x=1000,y=200)
btn=Button(a,text="Periodic Table ",bd=4,font=("Arial",14,"bold"),command=periodic_table).place(x=760,y=200)
lb=Label(a,text="Balancing",bg="#3B8258",fg="yellow",font=("Arial",30)).place(x=2,y=240)
var1=StringVar()
var2=StringVar()
et1=Entry(a,fg="black",font=("Arial",16),borderwidth = 5,textvariable=var1)
et1.insert(0,'Left Length')
et1.place(x=30,y=320)
et2=Entry(a,fg="black",font=("Arial",16),borderwidth = 5,textvariable=var2)
et2.insert(0,'Right Length')
et2.place(x=320,y=320)
btn=Button(a,text="Evaluate",bd=4,font=("Arial",12,"bold"),command=final_evaluation).place(x=600,y=320)
btn=Button(a,text="Hint How to Evaluate",bd=4,font=("Arial",12,"bold"),command=hint).place(x=700,y=320)
btn=Button(a,text="Fraction Mass of a Equation",bd=4,font=("Arial",12,"bold"),command=fraction_mass).place(x=896,y=320)
lb=Label(a,text="Searching",bg="#3B8258",fg="yellow",font=("Arial",30)).place(x=2,y=380)
var3=StringVar()
et1=Entry(a,fg="black",font=("Arial",16),borderwidth = 5,textvariable=var3)
et1.insert(0,'Fe')
et1.place(x=30,y=460)
btn=Button(a,text="Search by Symbol",bd=4,font=("Arial",12,"bold"),command=search_by_symbol).place(x=300,y=460)
btn=Button(a,text="Search by Mass",bd=4,font=("Arial",12,"bold"),command=search_by_mass).place(x=470,y=460)
btn=Button(a,text="Find Atomic Number",bd=4,font=("Arial",12,"bold"),command=find_atomic_number).place(x=630,y=460)
btn=Button(a,text="Periodic Group",bd=4,font=("Arial",12,"bold"),command=periodic_group).place(x=830,y=460)
btn=Button(a,text="Period Length ",bd=4,font=("Arial",12,"bold"),command=period_length).place(x=990,y=460)

lb=Label(a,text="Equilibrium",bg="#347A50",fg="yellow",font=("Arial",30)).place(x=2,y=520)

var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
et1=Entry(a,fg="black",font=("Arial",16),borderwidth = 5,textvariable=var4)
et1.insert(0,'Left Length (Eq1)')
et1.place(x=30,y=600)
et2=Entry(a,fg="black",font=("Arial",16),borderwidth = 5,textvariable=var5)
et2.insert(0,'Right Length(Eq1)')
et2.place(x=300,y=600)
et1=Entry(a,fg="black",font=("Arial",16),borderwidth = 5,textvariable=var6)
et1.insert(0,'Left Length(Eq2)')
et1.place(x=580,y=600)
et2=Entry(a,fg="black",font=("Arial",16),borderwidth = 5,textvariable=var7)
et2.insert(0,'Right Length(Eq2)')
et2.place(x=860,y=600)
btn=Button(a,text="Evaluate/Redox/Coefficient",bd=4,font=("Arial",12,"bold"),command=evaluate).place(x=1130,y=600)

b=Label(a,text="Made By :- Sanjeev Kumar Prajapati").place(x=600,y=670)
a.mainloop()
"""
This is a
Balancing stoichiometry of a chemical reaction GUI Application based on python, it is used for 1.) Balancing  any chemical reaction, 2.) balancing any redox reaction 3.) Find any element in a periodic table.
4.) Get the Standard Formula of any component .
"""
