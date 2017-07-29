# -*- coding: utf-8 -*-
from tkinter import *
import os
import string
#++++++++++++++++++++++++++++++++++++++++++++++
# Abaixo colocando os comandos!!!!
#++++++++++++++++++++++++++++++++++++++++++++++
#______________________________________________
"""
S = S0 + V0. t. + a.t²/2 
"""
m = "Metros"
r = "Resultado:"
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
	rslt ['text'] = x
def am():
	ov = ve.get()
	ot = te.get()
	nv = int(ov)
	nt = int(ot)
	x = nv / nt
	rslt ['text'] = x,"m/s"
def lptbr():
	rslt ['text'] = "Resultado:"
	vm ['text'] = "Velocidade Média"
	reset ['text'] = "Resetar"
	m = "Metros"
	sde ['text'] = "Metros"
	tde ['text'] = "Segundos"
	x = "450x500"
	root.geometry(x)	
def le():
	r = "Result:"
	rslt ['text'] = r
	vm ['text'] = "Avagerage Speed"
	am ['text'] = "Avagerage Aceleration"
	reset ['text'] = "Reset"
	m = "Meters"
	sde ['text'] = "Meters"
	tde ['text'] = "Seconds"
	x = "500x500"
	root.geometry(x)	
def reset():
	rslt ['text'] = r
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
#+++++++++++++++++++++++++++++++++++++++++++++++
#Colocando as configuraçoes do mestre |
#_____________________________________V_________
#_______________________________________________
x = "460x500"
root = Tk()							           
root.title("Fisicx ALPHA 0.2.5 ")					   
root.geometry(x)	
ox = root.geometry(x)		   		
root ['background'] = "black"            	   	
fonte = ("Verdana", "8", "bold")
fonte1 = ("Verdana", "6")
fonter = ("Times", "16", "bold")
#________________________________________________
# Colocando configurançoes dos menus
#________________________________________________
# AM = ^V / ^T
menu = Menu(root)
root.config(menu=menu)
#
subMenu = Menu(menu, font= fonte, fg="white", bg="black")
menu.add_cascade(label="Language", menu=subMenu, font= fonte)
subMenu.add_command(label="Pt-br", command=lptbr, font= fonte)
subMenu.add_command(label="English", command=le, font= fonte)
#________________________________________________
#Colocando as configuraçoes das label |
#_____________________________________V_________
vo = Label(root,text="Vo:",fg="white",bg="black", font = fonte)
a = Label(root,text="A:",fg="white",bg="black", font = fonte)		
s = Label(root,text="S:",fg="white",bg="black", font = fonte)	
t = Label(root,text="T:",fg="white",bg="black", font = fonte)	
v = Label(root,text="V:",fg="white",bg="black", font = fonte)
so = Label(root,text="So:",fg="white",bg="black", font = fonte)
#
vode = Label(root,text="M/s ",fg="white",bg="black", font = fonte)	
ade = Label(root,text="M/s ",fg="white",bg="black", font = fonte)
sde = Label(root,text="Metros",fg="white",bg="black", font = fonte)
tde = Label(root,text="Segundos ",fg="white",bg="black", font = fonte)
vde = Label(root,text="M/s ",fg="white",bg="black", font = fonte)
soe = Label(root,text="Metros ",fg="white",bg="black", font = fonte)
################################################
vo.grid(row=1)								   
a.grid(row=2)								   
s.grid(row=3)								   
t.grid(row=4)								   
v.grid(row=5)	
so.grid(row=6)	
vode.grid(row=1, column=2)
ade.grid(row=2, column=2)
sde.grid(row=3, column=2)
tde.grid(row=4, column=2)
vde.grid(row=5, column=2)
soe.grid(row=6, column=2)						   
#+++++++++++++++++++++++++++++++++++++++++++++++
#Colocando as configuraçoes das entradas |
#________________________________________V______
voe = Entry(root, font = fonte1, fg="black", bg="white")	
ae = Entry(root, font = fonte1, fg="black", bg="white")							   		
se = Entry(root, font = fonte1, fg="black", bg="white")							   		
te = Entry(root, font = fonte1, fg="black", bg="white")							   	
ve = Entry(root, font = fonte1, fg="black", bg="white")	
so = Entry(root, font = fonte1, fg="black", bg="white")						   	 
voe.grid(row=1, column=1)					   	
ae.grid(row=2, column=1) 					   	
se.grid(row=3, column=1)					   		 
te.grid(row=4, column=1)					   			 
ve.grid(row=5, column=1)	
so.grid(row=6, column=1)				   
#______________________________________________
#__________________________________________-[]X|
#					       |
#				               |			
#==============================================|
#          Abaixo declarando as Labels	       |	
#==============================================|
#					       |		
#                   |                          |
#                   |                          |
#                   |                          | 
#___________________V__________________________|
                    #_/|\_#
                    #_/|\_#
                    #_/|\_#
    #_______________#_/|\_#__________________
   #__________________/|\____________________|         
rslt = Label(root, text="  Resultado:   ",font = fonter, fg="red", bg="black")         		  
rslt.grid(row=0)							   		
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~		
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/|     
#Abaixo declarando  os botões 		     | |		
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~V~~~~~~~~~\|
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#        caixa=Frame(janela, borderwidth=3, relief=GROOVE) [X]
#
#
sovt = Button(root, text="          Sovt           ", fg="white", bg="black", command=sovt)			
sovt.grid(row=9, column=1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/\_____________________/\
calc = Button(root, text="      Torricelli     ", fg="white", bg="black", command=torric)
calc.grid(row=9)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|	( º )     ( º )  |
vm = Button(root, text="  Velocidade Média ", fg="white", bg="black", command=vm)
vm.grid(row=9, column=2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\/\/\/\/\/\/\/\/\/\/\/\/\
reset = Button(root, text="   Resetar    ", fg="white", bg="black", command=reset)
reset.grid(row=10, column=2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
am = Button(root, text="Aceleração média", fg="white", bg="black", command=am)
am.grid(row=10)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\/\/\/\/\/\/\/\/\/\/\/\/
#________________________________________________\_______________________/
am = Button(root, text="S = S0 + V0. t. + a.t²/2", fg="white", bg="black", command=sovtaum)
am.grid(row=10, column=1)
root.mainloop()
