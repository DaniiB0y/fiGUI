# -*- coding: utf-8 -*-
from tkinter import *
import os
import string
import random
m = "Metros"
r = ""
colors = ['#ff25fc', '#f36767', '#fffdfd', '#35ff62', '#f3f84d']
colorsf = ['#000','#3F3939','#23110C','#001036']
c = random.choice(colors)
cf = random.choice(colorsf)
ce = cf
def cinematica():
	print ('Its working')
def dinamica():
	root.destroy()
	# New "class"
	x = "800x300"
	new = Tk()							           
	new.title("Akt 1.0")					   
	new.geometry(x)	
	ox = new.geometry(x)		 
	new.resizable(False, False) 		
	new ['background'] = cf            	   	
	fonte = ("Times", "8", "roman")
	fonte1 = ("Times", "10", "italic")
	fonter = ("Times", "16", "roman")
	fontem = ("Verdana", "8", "roman")
	# Now is just config some other things
	menu = Menu(new)
	new.config(menu=menu)
	subMenu = Menu(menu, font=fontem, fg="black",bg="light gray")
	menu.add_cascade(label="Options", menu=subMenu,font=fontem)
	subMenu.add_command(label="Pt-br", command=lptbr,font=fontem)
	subMenu.add_command(label="English", command=le,font=fontem)
	subMenu.add_separator()
	subMenu.add_command(label="Help", command=helm,font=fontem)
	subMenu.add_separator()
	subMenu.add_command(label="Fisica Cinematica", command=cinematica,font=fontem)
	#
	rslt = Label(new, text="0 = 0",font = fonter, fg=c, bg=cf)         		  
	rslt.grid(row=0)
	#
def helm():
	os.system('notepad help.txt' if os.name == 'nt' else 'nano help.txt')
def vovat():
	ovo = voe.get()
	oa = ae.get()
	ot = te.get()
	v = ovo + oa * ot
	rslt ['text'] = "V = ",v,'m/s'
def tempo():
	ovo = ve.get()
	oso = se.get()
	nvo = int(ovo)
	nso = int(oso)
	t =  nso / onvo
	rslt ['text'] = "T = ",t,"Segundos"
def sovtaum():
	oso = soe.get()
	ovo = voe.get()
	ot = te.get()
	oa = ae.get()
	nso = int(oso)
	nvo = int(ovo)
	nt = int(ot)
	na = int(oa)
	s = nso + nvo * nt * na 
	sq = s ** 2
	x = sq / 2
	rslt ['text'] = "S = ",x,"Metros"
def am():
	ov = ve.get()
	ot = te.get()
	nv = int(ov)
	nt = int(ot)
	x = nv / nt
	rslt ['text'] = "A = ",x,"m/s"
def lptbr():
	rslt ['text'] = "0 = 0"
	reset ['text'] = "Resetar"
	m = "Metros"
	sde ['text'] = "Metros"
	tde ['text'] = "Segundos"
	x = "800x300"
	root.geometry(x)		
def le():
	r = "0 = 0:"
	rslt ['text'] = r
	reset ['text'] = "Reset"
	m = "Meters"
	sde ['text'] = "Meters"
	tde ['text'] = "Seconds"
	x = "800x300"
	root.geometry(x)	
def reset():
	r = "0 = 0"
	rslt ['text'] = r
	lptbr()
def vm():
	os = se.get()
	ot = te.get()
	ns = int(os)
	nt = int(ot)
	vm = ns / nt 
	rslt ['text'] = (vm," m/s")
def sovt():
	os = se.get()
	ov = ve.get()
	ot = te.get()
	ns = int(os)
	nv = int(ov)
	nt = int(ot)
	x = ns + nv * nt 
	rslt ['text'] = x,m
def torric():					   		
	ov0 = voe.get()
	oa = ae.get()
	os = se.get()
	nv0 = int(ov0)
	na = int(oa)
	ns = int(os)
	y = nv0 * nv0 + 2 * na * ns
	x = y * 0.5
	rslt ['text'] = x,"m/s"

x = "800x300"
root = Tk()							           
root.title("Akt 1.0")					   
root.geometry(x)	
ox = root.geometry(x)		 
root.resizable(False, False) 		
root ['background'] = cf            	   	
fonte = ("Times", "8", "roman")
fonte1 = ("Times", "10", "italic")
fonter = ("Times", "16", "roman")
fontem = ("Verdana", "8", "roman")

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu, font=fontem, fg="black",bg="light gray")
menu.add_cascade(label="Options", menu=subMenu,font=fontem)
subMenu.add_command(label="Pt-br", command=lptbr,font=fontem)
subMenu.add_command(label="English", command=le,font=fontem)
subMenu.add_separator()
subMenu.add_command(label="Help", command=helm,font=fontem)
subMenu.add_separator()
subMenu.add_command(label="Fisica Dinamica", command=dinamica,font=fontem)

vo = Label(root,text="Vo:",fg=c,bg=cf, font = fonte)
a = Label(root,text="A:",fg=c,bg=cf, font = fonte)		
s = Label(root,text="S:",fg=c,bg=cf, font = fonte)	
t = Label(root,text="T:",fg=c,bg=cf, font = fonte)	
v = Label(root,text="V:",fg=c,bg=cf, font = fonte)
so = Label(root,text="So:",fg=c,bg=cf, font = fonte)
g = Label(root, text="G↓:", fg=c, bg=cf, font = fonte)

vode = Label(root,text="M/s ",fg=c,bg=cf, font = fonte)	
ade = Label(root,text="M/s ",fg=c,bg=cf, font = fonte)
sde = Label(root,text="Metros",fg=c,bg=cf, font = fonte)
tde = Label(root,text="Segundos ",fg=c,bg=cf, font = fonte)
vde = Label(root,text="M/s ",fg=c,bg=cf, font = fonte)
soe = Label(root,text="Metros ",fg=c,bg=cf, font = fonte)
ge = Label(root,text="m/s",fg=c,bg=cf, font = fonte)

vo.grid(row=1)								   
a.grid(row=2)								   
s.grid(row=3)								   
t.grid(row=4)								   
v.grid(row=5)	
so.grid(row=6)	
g.grid(row=7)
vode.grid(row=1, column=2)
ade.grid(row=2, column=2)
sde.grid(row=3, column=2)
tde.grid(row=4, column=2)
vde.grid(row=5, column=2)
soe.grid(row=6, column=2)
ge.grid(row=7, column=2)						   

voe = Entry(root,font=fonte1,fg=c,bg=ce,bd="1px",width="62")	
ae = Entry(root,font=fonte1,fg=c,bg=ce,bd="1px",width="62")							   		
se = Entry(root,font=fonte1,fg=c,bg=ce,bd="1px",width="62")							   		
te = Entry(root,font=fonte1,fg=c,bg=ce,bd="1px",width="62")							   	
ve = Entry(root,font=fonte1,fg=c,bg=ce,bd="1px",width="62")	
so = Entry(root,font=fonte1,fg=c,bg=ce,bd="1px",width="62")	
ge = Entry(root,font=fonte1,fg=c,bg=ce,bd="1px",width="62")					   	 
voe.grid(row=1, column=1)					   	
ae.grid(row=2, column=1) 					   	
se.grid(row=3, column=1)					   		 
te.grid(row=4, column=1)					   			 
ve.grid(row=5, column=1)	
so.grid(row=6, column=1)	
ge.grid(row=7, column=1)			   
        
rslt = Label(root, text="0 = 0",font = fonter, fg=c, bg=cf)         		  
rslt.grid(row=0)							   		

sovt = Button(root, text=" S = so + Δv * Δt        ", fg=c, bg=cf, command=sovt,width="18")			
sovt.grid(row=9, column=1)

calc = Button(root, text="V² = Vo² + 2.a.s   ", fg=c, bg=cf, command=torric,width="18")
calc.grid(row=9)

vm = Button(root, text="  ΔV = Δs / Δt ", fg=c, bg=cf, command=vm,width="18")
vm.grid(row=9, column=2)

reset = Button(root, text="   Resetar    ", fg=c, bg=cf, command=reset,width="18")
reset.grid(row=10, column=2)

am = Button(root, text="A = Δv / Δt ", fg=c, bg=cf, command=am,width="18")
am.grid(row=10)

eqhe = Button(root, text="S = So + Vo. t. + a.t²/2", fg=c, bg=cf, command=sovtaum,width="18")
eqhe.grid(row=10, column=1)

t = Button(root, text="T = ΔS / ΔV", fg=c, bg=cf, command=tempo,width="18")
t.grid(row=11)

voat = Button(root, text="v = vo + a*t", fg=c, bg=cf, command=vovat, width="18")
voat.grid(row=11, column=1)
root.mainloop()
