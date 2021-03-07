from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("1350x750+0+0")
root.title("cafe management system")
root.configure(background ="green")

Tops =Frame(root,width=1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root,width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root,width = 440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width = 900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)


f2a = Frame(f1, width = 900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)


ft2 = Frame(f2, width = 440, height=450, bd=12, relief ="raise")
ft2.pack(side=TOP)

fb2 = Frame(f2, width = 440, height=250, bd=16, relief ="raise")
fb2.pack(side=BOTTOM)

f1aa= Frame(f1a, width = 400, height=330, bd=16, relief ="raise")
f1aa.pack(side=LEFT)

f1ab= Frame(f1a, width = 400, height=330, bd=16, relief ="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width = 450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)

f2ab= Frame(f2a, width = 450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background="green")
f1.configure(background="green")
f2.configure(background="green")

lblinfo = Label(Tops, font=("arial", 50, "bold"), text="Cafe Management System", bd=10)
lblinfo.grid(row=0, column = 0)

#========================= Method=================================
def qExit():
    qExit=messagebox.askyesno("Do you wish to quit?")
    if qExit > 0:
        root.destroy()
        return
#======================RESET=========================================
def reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Latte.set("0")
    E_Espresso.set("0")
    E_Iced_Latte.set("0")
    E_Vale_Coffee.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")
    E_Coffee_Cakes.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatte.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtIced_Latte.configure(state=DISABLED)
    txtVale_Coffee.configure(state=DISABLED)
    txtAfrican_Coffee.configure(state=DISABLED)
    txtAmerican_Coffee.configure(state=DISABLED)
    txtIced_Cappuccino.configure(state=DISABLED)
    txtCoffeeCake.configure(state=DISABLED)
    txtRed_Velvet_Cake.configure(state=DISABLED)
    txtBlack_Forest_Cake.configure(state=DISABLED)
    txtBoston_Cream_Cake.configure(state=DISABLED)
    txtLagos_Chocolate_Cake.configure(state=DISABLED)
    txtKilburn_Chocolate_Cake.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtCarlton_Hill_Cake.configure(state=DISABLED)
    txtQueen_park_Cake.configure(state=DISABLED)
#============================================CheckBUTTON=====================
def chkbutton_value():

        if (var1.get() == 1):
            txtLatte.configure(state=NORMAL)
        elif var1.get() == 0:
            txtLatte.configure(state=DISABLED)
            E_Latte.set("0")
        if (var2.get() == 1):
            txtEspresso.configure(state=NORMAL)
        elif var2.get() == 0:
            txtEspresso.configure(state=DISABLED)
            E_Espresso.set("0")
        if (var3.get() == 1):
            txtIced_Latte.configure(state=NORMAL)
        elif var3.get() == 0:
            txtIced_Latte.configure(state=DISABLED)
            E_Iced_Latte.set("0")
        if (var4.get() == 1):
            txtVale_Coffee.configure(state=NORMAL)
        elif var4.get() == 0:
            txtVale_Coffee.configure(state=DISABLED)
            E_Vale_Coffee.set("0")
        if (var5.get() == 1):
            txtCappuccino.configure(state=NORMAL)
        elif var5.get() == 0:
            txtCappuccino.configure(state=DISABLED)
            E_Cappuccino.set("0")
        if (var6.get() == 1):
            txtAfrican_Coffee.configure(state=NORMAL)
        elif var6.get() == 0:
            txtAfrican_Coffee.configure(state=DISABLED)
            E_African_Coffee.set("0")
        if (var7.get() == 1):
            txtAmerican_Coffee.configure(state=NORMAL)
        elif var7.get() == 0:
            txtAmerican_Coffee.configure(state=DISABLED)
            E_American_Coffee.set("0")
        if (var8.get() == 1):
            txtIced_Cappuccino.configure(state=NORMAL)
        elif var8.get() == 0:
            txtIced_Cappuccino.configure(state=DISABLED)
            E_Iced_Cappuccino.set("0")
        if (var9.get() == 1):
            txtCoffeeCake.configure(state=NORMAL)
        elif var9.get() == 0:
            txtCoffeeCake.configure(state=DISABLED)
            E_Coffee_Cakes.set("0")
        if (var10.get() == 1):
            txtRed_Velvet_Cake.configure(state=NORMAL)
        elif var10.get() == 0:
            txtRed_Velvet_Cake.configure(state=DISABLED)
            E_Red_Velvet_Cake.set("0")
        if (var11.get() == 1):
            txtBlack_Forest_Cake.configure(state=NORMAL)
        elif var11.get() == 0:
            txtBlack_Forest_Cake.configure(state=DISABLED)
            E_Black_Forest_Cake.set("0")
        if (var12.get() == 1):
            txtBoston_Cream_Cake.configure(state=NORMAL)
        elif var12.get() == 0:
            txtBoston_Cream_Cake.configure(state=DISABLED)
            E_Boston_Cream_Cake.set("0")
        if (var13.get() == 1):
            txtLagos_Chocolate_Cake.configure(state=NORMAL)
        elif var13.get() == 0:
            txtLagos_Chocolate_Cake.configure(state=DISABLED)
            E_Lagos_Chocolate_Cake.set("0")
        if (var14.get() == 1):
            txtKilburn_Chocolate_Cake.configure(state=NORMAL)
        elif var14.get() == 0:
            txtKilburn_Chocolate_Cake.configure(state=DISABLED)
            E_Kilburn_Chocolate_Cake.set("0")
        if (var15.get() == 1):
            txtCarlton_Hill_Cake.configure(state=NORMAL)
        elif var15.get() == 0:
            txtCarlton_Hill_Cake.configure(state=DISABLED)
            E_Carlton_Hill_Chocolate_Cake.set("0")
        if (var16.get() == 1):
            txtQueen_park_Cake.configure(state=NORMAL)
        elif var16.get() == 0:
            txtQueen_park_Cake.configure(state=DISABLED)
            E_Queen_Park_Chocolate_Cake.set("0")

#========================RECEIPT==========================
def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref: \t\t\t'+Receipt_Ref.get()+"\t\t\t"+DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t'+'Quantity\t\t\t'+"Price \n\n")

    if E_Latte.get() > 0:
        txtReceipt.insert(END, 'Latte:\t\t\t'+str(E_Latte.get())+'\t\t\t'+str('$%.2f'%(E_Latte.get()*1.2))+'\n')
    if E_Espresso.get() > 0:
        txtReceipt.insert(END, 'Espresso:\t\t\t'+str(E_Espresso.get())+'\t\t\t'+str('$%.2f'%(E_Espresso.get()*1.99))+'\n')
    if E_Iced_Latte.get() > 0:
        txtReceipt.insert(END, 'Iced Latte:\t\t\t'+str(E_Iced_Latte.get())+'\t\t\t'+str('$%.2f'%(E_Iced_Latte.get()*2.05))+'\n')
    if E_Vale_Coffee.get() > 0:
        txtReceipt.insert(END, 'Vale Coffee:\t\t\t'+str(E_Vale_Coffee.get())+'\t\t\t'+str('$%.2f'%(E_Vale_Coffee.get()*1.89))+'\n')
    if E_Cappuccino.get() > 0:
        txtReceipt.insert(END, 'Cappuccino:\t\t\t'+str(E_Cappuccino.get())+'\t\t\t'+str('$%.2f'%(E_Cappuccino.get()*1.99))+'\n')
    if E_African_Coffee.get() > 0:
        txtReceipt.insert(END, 'African Coffee:\t\t\t'+str(E_African_Coffee.get())+'\t\t\t'+str('$%.2f'%(E_African_Coffee.get()*2.99))+'\n')
    if E_American_Coffee.get() > 0:
        txtReceipt.insert(END, 'American Coffee:\t\t\t'+str(E_American_Coffee.get())+'\t\t\t'+str('$%.2f'%(E_American_Coffee.get()*2.39))+'\n')
    if E_Iced_Cappuccino.get() > 0:
        txtReceipt.insert(END, 'Iced Cappuccino:\t\t\t'+str(E_Iced_Cappuccino.get())+'\t\t\t'+str('$%.2f'%(E_Iced_Cappuccino.get()*1.29))+'\n')
    if E_Coffee_Cakes.get() > 0:
        txtReceipt.insert(END, 'Coffee Cake:\t\t\t'+str(E_Coffee_Cakes.get())+'\t\t\t'+str('$%.2f'%(E_Coffee_Cakes.get()*1.35))+'\n')
    if E_Red_Velvet_Cake.get() > 0:
        txtReceipt.insert(END, 'Red Velvet Cake:\t\t\t'+str(E_Red_Velvet_Cake.get())+'\t\t\t'+str('$%.2f'%(E_Red_Velvet_Cake.get()*2.2))+'\n')
    if E_Black_Forest_Cake.get() > 0:
        txtReceipt.insert(END, 'Black Forest Cake:\t\t\t'+str(E_Black_Forest_Cake.get())+'\t\t\t'+str('$%.2f'%(E_Black_Forest_Cake.get()*1.99))+'\n')
    if E_Boston_Cream_Cake.get() > 0:
        txtReceipt.insert(END, 'Boston Cream Cake:\t\t\t'+str(E_Boston_Cream_Cake.get())+'\t\t\t'+str('$%.2f'%(E_Boston_Cream_Cake.get()*1.49))+'\n')
    if E_Lagos_Chocolate_Cake.get() > 0:
        txtReceipt.insert(END, 'Lagos Chocolate Cake:\t\t\t'+str(E_Lagos_Chocolate_Cake.get())+'\t\t\t'+str('$%.2f'%(E_Lagos_Chocolate_Cake.get()*1.80))+'\n')
    if E_Kilburn_Chocolate_Cake.get() > 0:
        txtReceipt.insert(END, 'Kilburn Chocolate Cake:\t\t\t'+str(E_Kilburn_Chocolate_Cake.get())+'\t\t\t'+str('$%.2f'%(E_Kilburn_Chocolate_Cake.get()*1.67))+'\n')
    if E_Carlton_Hill_Chocolate_Cake.get() > 0:
        txtReceipt.insert(END, 'Carlton Hill Chocolate Cake:\t\t\t'+str(E_Carlton_Hill_Chocolate_Cake.get())+'\t\t\t'+str('$%.2f'%(E_Carlton_Hill_Chocolate_Cake.get()*1.6))+'\n')
    if E_Queen_Park_Chocolate_Cake.get() > 0:
        txtReceipt.insert(END, 'Queen Park Chocolate Cake:\t\t\t'+str(E_Queen_Park_Chocolate_Cake.get())+'\t\t\t'+str('$%.2f'%(E_Queen_Park_Chocolate_Cake.get()*1.99))+'\n')

    txtReceipt.insert(END, '\nCost of Drinks:\t'+CostofDrinks.get()+"\tTax Paid:\t"+ PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Cost of Cakes:\t'+CostofCakes.get()+"\tSubTotal:\t"+ SubTotal.get()+"\n")
    txtReceipt.insert(END, 'Service Charge:\t'+ServiceCharge.get()+"\tTotal Cost:\t"+ TotalCost.get()+"\n")
#==========================CH



#============================Variable=============================


var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()

DateofOrder    = StringVar()
Reciept_Ref    = StringVar()
PaidTax        = StringVar()
Subtotal       = StringVar()
TotalCost      = StringVar()
CostofCakes    = StringVar()
CostofDrinks   = StringVar()
ServiceCharge  = StringVar()



E_Latte                   = StringVar()
E_Espresso                = StringVar()
E_IcedLatte               = StringVar()
E_ValeCoffee              = StringVar()
E_Cappuccino              = StringVar()
E_AfricanCoffee           = StringVar()
E_AmericanCoffee          = StringVar()
E_IcedCappuccino          = StringVar()

E_CoffeeCake                  = StringVar()
E_RedVelvetCake               = StringVar()
E_BlackForestCake             = StringVar()
E_BostonCreamCake             = StringVar()
E_LagosChocolateCake          = StringVar()
E_KilburnChocolateCake        = StringVar()
E_CarltonHillChocolateCake    = StringVar()
E_QueenParkChocolate          = StringVar()

E_Latte.set("0")
E_Espresso.set("0")
E_IcedLatte.set("0")
E_ValeCoffee.set("0")
E_Cappuccino.set("0")
E_AfricanCoffee.set("0")
E_AmericanCoffee.set("0")
E_IcedCappuccino.set("0")

E_CoffeeCake.set("0")
E_RedVelvetCake.set("0")
E_BlackForestCake.set("0")
E_BostonCreamCake.set("0")
E_LagosChocolateCake.set("0")
E_KilburnChocolateCake.set("0")
E_CarltonHillChocolateCake.set("0")
E_QueenParkChocolate.set("0")

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")

#===================================================drinks=================================================================================
latte          = Checkbutton(f1aa, text="Latte \t", variable = var1,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=0, sticky=W)
Espresso       = Checkbutton(f1aa, text="Espresso \t", variable = var2,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=1, sticky=W)
IcedLatte      = Checkbutton(f1aa, text="Iced Latte \t", variable = var3,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=2, sticky=W)
ValeCoffee     = Checkbutton(f1aa, text="Vale Coffee \t", variable = var4,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=3, sticky=W)
Cappuccino     = Checkbutton(f1aa, text="Cappuccino \t", variable = var5,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=4, sticky=W)
AfricanCoffee  = Checkbutton(f1aa, text="African Coffee \t", variable = var6,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=5, sticky=W)
AmericanCoffee = Checkbutton(f1aa, text="American Coffee \t", variable = var7,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=6, sticky=W)
IcedCappuccino = Checkbutton(f1aa, text="Iced Cappuccino \t", variable = var8,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=7, sticky=W)


#===================================================cake=================================================================================
CoffeeCake               = Checkbutton(f1ab, text="Coffee Cake\t", variable = var9,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=0, sticky=W)
RedVelvetCake            = Checkbutton(f1ab, text="Red Velvet Cake \t", variable = var10,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=1, sticky=W)
BlackForestCake          = Checkbutton(f1ab, text="Black Forest Cake \t", variable = var11,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=2, sticky=W)
BostonCreamCake          = Checkbutton(f1ab, text="Boston Cream Cake \t", variable = var12,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=3, sticky=W)
LagosChocolateCake       = Checkbutton(f1ab, text="Lagos Chocolate Cake \t", variable = var13,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=4, sticky=W)
KilburnChocolateCake     = Checkbutton(f1ab, text="Kilburn Chocolate Cake \t", variable = var14,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=5, sticky=W)
CarltonHillChocolateCake = Checkbutton(f1ab, text="Carlton Hill Chocolate Cake \t", variable = var15,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=6, sticky=W)
QueenchocolateCake       = Checkbutton(f1ab, text="Queen's Park Chocolate Cake\t", variable = var16,onvalue = 1, offvalue = 0, font= ("calibri", 18, "bold")).grid(row=7,sticky=W)

#================================Enter Widget for Drinks=======================
txtlatte = Entry(f1aa,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable=E_Latte,state= DISABLED)
txtlatte.grid(row=0, column=1)

txtEspresso = Entry(f1aa,font=("arial",18,"bold"),bd=8, width=6, justify="left", textvariable = E_Espresso,state= NORMAL)
txtEspresso.grid(row=1, column=1)

txtIcedLatte = Entry(f1aa,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_IcedLatte,state= NORMAL)
txtIcedLatte.grid(row=2, column=1)

txtValeCoffee = Entry(f1aa,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_ValeCoffee,state= NORMAL)
txtValeCoffee.grid(row=3, column=1)

txtCappuccino = Entry(f1aa,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_Cappuccino,state= NORMAL)
txtCappuccino.grid(row=4, column=1)

txtAfricanCoffee = Entry(f1aa,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_AfricanCoffee,state= NORMAL)
txtAfricanCoffee.grid(row=5, column=1)

txtAmericanCoffee = Entry(f1aa,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_AmericanCoffee, state= NORMAL)
txtAmericanCoffee.grid(row=6, column=1)

txtIcedCappuccino = Entry(f1aa,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_IcedCappuccino,state= NORMAL)
txtIcedCappuccino.grid(row=7, column=1)


#================================Enter Widget for Cakes=========================
txtCoffeecake = Entry(f1ab,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_CoffeeCake,state= NORMAL)
txtCoffeecake.grid(row=0, column=1)

txtRedVelvetCake = Entry(f1ab,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_RedVelvetCake,state= NORMAL)
txtRedVelvetCake.grid(row=1, column=1)

txtBlackForestCake = Entry(f1ab,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_BlackForestCake,state= NORMAL)
txtBlackForestCake.grid(row=2, column=1)

txtBostonCreamCake = Entry(f1ab,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_BostonCreamCake,state= NORMAL)
txtBostonCreamCake.grid(row=3, column=1)

txtLagosChocolateCake = Entry(f1ab,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_LagosChocolateCake,state= NORMAL)
txtLagosChocolateCake.grid(row=4, column=1)

txtKilburnChocolateCake = Entry(f1ab,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_KilburnChocolateCake,state= NORMAL)
txtKilburnChocolateCake.grid(row=5, column=1)

txtCarltonHillChocolateCake = Entry(f1ab,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_CarltonHillChocolateCake,state= NORMAL)
txtCarltonHillChocolateCake.grid(row=6, column=1)

txtQueensParkChocolateCake = Entry(f1ab,font=("arial",18,"bold"),bd=8, width=6, justify="left",textvariable = E_QueenParkChocolate,state= NORMAL)
txtQueensParkChocolateCake.grid(row=7, column=1)

#================Info=========================
lblreceipt = Label(ft2,font=("arial", 12, "bold"), text="receipt", bd=2, anchor="w")
lblreceipt.grid(row=0,column=0,sticky=W)
txtReceipt = Text(ft2,font=("arial",12,"bold"),bd=8, width=59,height=22,bg="white")
txtReceipt.grid(row=1, column=0)



#================cost of items Info===================
lblCostofDrinks=Label(f2aa,font=("arial", 12, "bold"),text ="cost of drinks", bd=8)
lblCostofDrinks.grid(row=0, column=0, sticky=W)
txtCostofDrinks=Entry(f2aa,font=("arial", 12, "bold"), bd=8, justify="left",textvariable =CostofDrinks)
txtCostofDrinks.grid(row=0,column =1, sticky=W)

lblCostofCakes=Label(f2aa,font=("arial", 12, "bold"),text ="cost of cakes", bd=8)
lblCostofCakes.grid(row=1, column=0, sticky=W)
txtCostofCakes=Entry(f2aa,font=("arial", 12, "bold"), bd=8, justify="left",textvariable =CostofCakes)
txtCostofCakes.grid(row=1,column =1, sticky=W)

lblServiceChar=Label(f2aa,font=("arial", 12, "bold"),text ="Service Charge", bd=8)
lblServiceChar.grid(row=2, column=0, sticky=W)
txtServiceChar=Entry(f2aa,font=("arial", 12, "bold"), bd=8, justify="left")
txtServiceChar.grid(row=2,column =1, sticky=W)

#===============Payment Information===========
lblPaidTax=Label(f2ab,font=("arial", 12, "bold"),text ="Paid Tax", bd=8)
lblPaidTax.grid(row=0, column=0, sticky=W)
txtPaidTax=Entry(f2ab,font=("arial", 12, "bold"), bd=8, justify="left" ,textvariable=PaidTax)
txtPaidTax.grid(row=0,column =1, sticky=W)

lblSubtotal=Label(f2ab,font=("arial", 12, "bold"),text ="Sub Total", bd=8, textvariable=SubTotal)
lblSubtotal.grid(row=1, column=0, sticky=W)
txtSubtotal=Entry(f2ab,font=("arial", 12, "bold"), bd=8, justify="left")
txtSubtotal.grid(row=1,column =1, sticky=W)

lblTotalCost=Label(f2ab,font=("arial", 12, "bold"),text ="Total Cost", bd=8)
lblTotalCost.grid(row=2, column=0, sticky=W)
txtTotalCost=Entry(f2ab,font=("arial", 12, "bold"), bd=8, justify="left")
txtTotalCost.grid(row=2,column =1, sticky=W)

PaidTax.set("")
Subtotal.set("")
TotalCost.set("")
CostofDrinks.set("")
CostofCakes.set("")


#================Button==========
btnTotal=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=("arial",10,"bold"), width=5,text="total").grid(row=0,column=0)

btnReceipt=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=("arial",10,"bold"), width=5,text="Receipt").grid(row=0,column=1)

btnReset=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=("arial",10,"bold"), width=5,text="Reset").grid(row=0,column=2)

btnExit=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=("arial",10,"bold" ), width=5,text="Exit", command = qExit) .grid(row=0,column=3)



root.mainloop()





