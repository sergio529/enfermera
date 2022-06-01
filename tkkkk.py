import pygame

def ventana():
    
    vp= Tk()
    vp.title("Ingreso Enfermera")
    vp.geometry('400x200')
    centrar(vp)
    mostrar(vp)
    nomproy=Label(vp,width="15",height="2",bg="Turquoise",text="Ingreso enfermera",font=("Comic Sans MS",10),fg="White")
        
    nomc=Button(vp,text="Nombre",command=ingresar(vp))
    cc=Button(vp,text="Cedula",command=ingresar(vp))
    turno=Button(vp,text="Turno",command=ingresar(vp))
    puntaje=Button(vp,text="Rendimiento")
    
    nomc.grid(row=1, column=0)
    turno.grid(row=3, column=0)
    cc.grid(row=2, column=0)
    nomproy.grid(column=3,row=0)
    puntaje.grid(row=4, column=0)
    

    vp.mainloop()
def mostrar(ventana):
        ventana.deiconify()
def ocultar(ventana):
        ventana.withdraw()
def centrar(ventana):
    ventana.update_idletasks()
    w=ventana.winfo_width()
    h=ventana.winfo_height()
    extraW=ventana.winfo_screenwidth()-w
    extraH=ventana.winfo_screenheight()-h
    ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))
def ingresar(vp):
    nomci=Entry(vp,width=10)
    cci=Entry(vp,width=10)
    tti=Entry(vp,width=10)
    nomci.grid(row=1, column=2)
    cci.grid(row=2, column=2)
    tti.grid(row=3, column=2)
    t= nomci.get()
    p= cci.get()
    d= tti.get()
    ocultar(vp)
    v="si"
    return(v)
def n_1():
    n=1
    
