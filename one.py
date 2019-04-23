import tkinter as tk 
from tkinter import *
from tkinter import messagebox

import os



r = tk.Tk() 
r.title('VMC') 
r.geometry("800x600")
circVar = IntVar()
rectVar = IntVar()

circ = tk.Checkbutton(r,text = 'Circle', variable = circVar, \
                 height=5, \
                 width = 20)
rect = tk.Checkbutton(r,text = 'Rectangle', variable = rectVar, \
                 height=5, \
                 width = 20)
circ.config(font=("Courier", 20))
rect.config(font=("Courier", 20))
circ.place(x=288,y=50)
rect.place(x=288,y=150)

forward = tk.Button(r, text='Next', width=25,height = 4, command=lambda :first() )
forward.place(x=288,y=400) 


#--------------------------------------
#circle
#--------------------------------------

radl = tk.Label(text="Diameter : ")
rad = tk.Entry(r)
radl.place(x=800,y=600)
rad.place(x=800,y=600)

yl = tk.Label(text="Y : ")
y = tk.Entry(r)
yl.place(x=800,y=600)
y.place(x=800,y=600)

xl = tk.Label(text="X : ")
x = tk.Entry(r)
xl.place(x=800,y=600)
x.place(x=800,y=600)

#depth
dl = tk.Label(text="Depth : ")
d = tk.Entry(r)
dl.place(x=800,y=600)
d.place(x=800,y=600)
#spindle speed
ssl = tk.Label(text="Spindle Speed : ")
ss = tk.Entry(r)
ssl.place(x=800,y=600)
ss.place(x=800,y=600)
#cutter diameter
cdl = tk.Label(text="Cutter Diameter : ")
cd = tk.Entry(r)
cdl.place(x=800,y=600)
cd.place(x=800,y=600)
#step down
sdl = tk.Label(text="Step Down: ")
sd = tk.Entry(r)
sdl.place(x=800,y=600)
sd.place(x=800,y=600)

#penetration feed
pfl = tk.Label(text="Penetration feed ")
pf = tk.Entry(r)
pfl.place(x=800,y=600)
pf.place(x=800,y=600)

#feed
fl = tk.Label(text="feed: ")
feed = tk.Entry(r)
fl.place(x=800,y=600)
feed.place(x=800,y=600)


#--------------------------------------
#Rectangle
#---------------------------------------
x1l = tk.Label(text="X1 : ")
x1 = tk.Entry(r)
x1l.place(x=800,y=600)
x1.place(x=800,y=600)

x2l = tk.Label(text="X2 : ")
x2 = tk.Entry(r)
x2l.place(x=800,y=600)
x2.place(x=800,y=600)

y1l = tk.Label(text="Y1 : ")
y1 = tk.Entry(r)
y1l.place(x=800,y=600)
y1.place(x=800,y=600)

y2l = tk.Label(text="Y2 : ")
y2 = tk.Entry(r)
y2l.place(x=800,y=600)
y2.place(x=800,y=600)



def first():
    forward.place(x=800,y=600)
    circ.place(x=800,y=600)
    rect.place(x=800,y=600)
    if circVar.get()==1:
        data = "Circle "
        radl.place(x=300,y=50)
        rad.place(x=500,y=50)

        xl.place(x=300,y=80)
        x.place(x=500,y=80)

        yl.place(x=300,y=110)
        y.place(x=500,y=110)

        dl.place(x=300,y=140)
        d.place(x=500,y=140)

        ssl.place(x=300,y=170)
        ss.place(x=500,y=170)

        cdl.place(x=300,y=200)
        cd.place(x=500,y=200)

        sdl.place(x=300,y=230)
        sd.place(x=500,y=230)

        pfl.place(x=300,y=260)
        pf.place(x=500,y=260)

        fl.place(x=300,y=290)
        feed.place(x=500,y=290)

    elif rectVar.get()==1:
        data = "Rectangle "
        x1l.place(x=300,y=150)
        x1.place(x=400,y=150)
        y1l.place(x=300,y=200)
        y1.place(x=400,y=200)
        x2l.place(x=300,y=250)
        x2.place(x=400,y=250)
        y2l.place(x=300,y=300)
        y2.place(x=400,y=300)

    label = tk.Label(r,text = data)
    label.config(font=("Courier", 20))
    label.place(x=340,y=20)    

    button = tk.Button(r,text = 'Generate ',command = lambda : second())
    button.config(font=("Courier", 20))
    button.place(x=340,y=500)

#G03 X60. I-10. F1500. ; i/p feed and 60 = (2)
#X80. I10.
#G01 Z-0.2 F300.


#G03 X60. I-10. F1500. 
#X80. I10.

default = "G21\nG00 G17 G40 G49 G80 G90 G62 G64\nG28 G91 Z0.\nG90\n" 
def second():
     if circVar.get()==1:
        xA = int(x.get()) + int(rad.get())/2 - int(cd.get())/2 #80
        xB = int(x.get()) - int(rad.get())/2 + int(cd.get())/2 #60
        i = int(rad.get())/2 - int(cd.get())/2
        print(os.getcwd())
        f = open(os.getcwd() + "/circle.nc","wt")
        f.write(default)
        f.write("S"+ss.get()+" M03\n")
        f.write("G00 X" + str(xA) + ". Y"+y.get())
        f.write("Z15. G49 H01\nG01 Z5. F6000.\n")
        f.write("Z1.1 F"+ pf.get()+"\n")
        
        f.write("Z-"+sd.get()+"\n")
        
        a = float(sd.get()) * 2
        
        while a <= (int(d.get())+0.1):
            f.write("G03 X"+str(xB)+" I-"+str(i)+" F"+ feed.get() +"\nX" + str(xA)+" I"+ str(i)+"\nG01 Z-" + "{0:.2f}".format(a) + " F" + pf.get() +"\n")
            a = a +  float(sd.get())  

        f.write("G03 X"+str(xB)+" I-"+str(i)+" F"+ feed.get() +"\nX" + str(xA)+" I"+ str(i)+"\n\n")
        f.write("G01 Z15. F6000.\nG28 G91 Z0.\nG90\nG49\nG28 G91 X0. Y0.\nG90\nM30\n % \n")

        
        messagebox.showinfo("Done","Done\nPlease Quit")     



r.mainloop()  