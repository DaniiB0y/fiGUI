# -*- coding: utf-8 -*-
from tkinter import *
#++++++++++++++++++++++++++++++++++++++++++++++
# Abaixo colocando os comandos!!!!
#++++++++++++++++++++++++++++++++++++++++++++++
#______________________________________________
def reset():
	rslt ['text'] = "Resultado:"
	root.geometry("500x300")
def vm():
	os = se.get()
	ot = te.get()
	ns = int(os)
	nt = int(ot)
	vm = ns / nt 
	rslt ['text'] = (vm," m/s")
	root.geometry("500x300")
def sovt():
	os = se.get()
	ov = ve.get()
	ot = te.get()
	ns = int(os)
	nv = int(ov)
	nt = int(ot)
	x = ns + nv * nt 
	rslt ['text'] = x," Metros"
	root.geometry("500x300")
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
	root.geometry("500x300")
#+++++++++++++++++++++++++++++++++++++++++++++++
#Colocando as configuraçoes do mestre |
#_____________________________________V_________
#_______________________________________________
root = Tk()							           
root.title("Fisicx ALPHA 0.2.5 ")					   
root.geometry("500x300")					   		
root ['background'] = "black"            	   	
fonte = ("Verdana", "8", "bold")
fonte1 = ("Verdana", "6")
fonter = ("Times", "16", "bold")		                       
#________________________________________________
#Colocando as configuraçoes das label |
#_____________________________________V_________
vo = Label(root,text="Vo:",fg="white",bg="black", font = fonte)
a = Label(root,text="A:",fg="white",bg="black", font = fonte)		
s = Label(root,text="S:",fg="white",bg="black", font = fonte)	
t = Label(root,text="T:",fg="white",bg="black", font = fonte)	
v = Label(root,text="V:",fg="white",bg="black", font = fonte)	
################################################
vo.grid(row=1)								   #			
a.grid(row=2)								   #		
s.grid(row=3)								   #		
t.grid(row=4)								   #	
v.grid(row=5)								   #	 
#+++++++++++++++++++++++++++++++++++++++++++++++
#Colocando as configuraçoes das entradas |
#________________________________________V______
voe = Entry(root, font = fonte1, fg="black", bg="white")	
ae = Entry(root, font = fonte1, fg="black", bg="white")							   		
se = Entry(root, font = fonte1, fg="black", bg="white")							   		
te = Entry(root, font = fonte1, fg="black", bg="white")							   	
ve = Entry(root, font = fonte1, fg="black", bg="white")							   	 
voe.grid(row=1, column=1)					   	
ae.grid(row=2, column=1) 					   	
se.grid(row=3, column=1)					   		 
te.grid(row=4, column=1)					   			 
ve.grid(row=5, column=1)					   
#______________________________________________
#__________________________________________-[]X|
#											   |
#										       |			
#==============================================|
#          Abaixo declarando as Labels		   |	
#==============================================|
#					_	     			       |		
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\________________________/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/|     
#Abaixo declarando  os botões 		|		 | |		
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~V~~~~~~~~~\|
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
cvo = Checkbutton(root, text="M/s", variable=v,font = fonte, fg='white',bg='black')
cvo.grid(row=1, column=2)
cvo.var = v
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sovt = Button(root, text="      Sovt      ", fg="white", bg="black", command=sovt)			
sovt.grid(row=8, column=1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/\_____________________/\
calc = Button(root, text="   Torricelli   ", fg="white", bg="black", command=torric)
calc.grid(row=8)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|	( º )		    ( º )|
vm = Button(root, text="Velocidade Média", fg="white", bg="black", command=vm)
vm.grid(row=8, column=2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\/\/\/\/\/\/\/\/\/\/\/\/\
reset = Button(root, text="Resetar", fg="black", bg="#00FFFF", command=reset)
reset.grid(row="99", column=1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\/\/\/\/\/\/\/\/\/\/\/\/
cv = Checkbutton(root, text="M/s", variable=vo, font = fonte, fg='white',bg='black')
cv.grid(row=5, column=2)
cv.var = vo
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root.mainloop()
