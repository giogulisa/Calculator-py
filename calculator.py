# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import math
 
class Calculator:
    calc_value = 0.0
 
    #shemowmeba
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False
    
    
 
    # daklikvis shemdeg ra unda moxdes
    def button_press(self, value):
 
        #current value  entry- shi  
        entry_val = self.number_entry.get()
 
        # vasworeb rom marjvniv daumatos da ara marcxnidan
        entry_val += value
 
        # entry -is vasuptaveb
        self.number_entry.delete(0, "end")
 
        # Insert vaketeb new value -is marcxnidan marjvniv
        self.number_entry.insert(0, entry_val)
 
    # float ad shemowmeba
    def isfloat(self, str_val):
        try:

            float(str_val)
 
            return True
        except ValueError:
            return False
 
    # moqmedebebs vasrulebineb aq
    def math_button_press(self, value):
 
        # tu numberebia mashin
        if self.isfloat(str(self.number_entry.get())):
 
            # aq vanuleb moqmedebas
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False
 
            #vigeb entry box idan values
            self.calc_value = float(self.entry_value.get())
 
            
            # moqmedebas vaketeb True -d da vamowmeb consolshi daeklika tu ara
            if value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif value == "*":
                print("* Pressed")
                self.mult_trigger = True
            elif value == "+":
                print("+ Pressed")
                self.add_trigger = True
            else:
                print("- Pressed")
                self.sub_trigger = True
 
            #entry box is gasuptaveba
            self.number_entry.delete(0, "end")
 
    #aq davamateb AC it washlas ...
    #damatda warmatebit
    def dlt_button_press(self):
        print("deletes daewira")
        self.calc_value=0.0
        solution=0
        self.number_entry.delete(0, "end")
        
    #davamate akvadrateba
            
    def kvadrati_button_press(self):
        print("akvadratebis funqcia gaeshva")
        ricxvi=self.entry_value.get()
        solution=pow(float(ricxvi),2)
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, solution)
        
    #davamate pesvis amogeba    
    def pesvi_button_press(self):
        print("pesvis funqcia gaeshva")
        solution=math.sqrt(float(self.entry_value.get()))
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, solution)
        
    def equal_button_press(self):
 
        # math gilakze daweris shemowmeba
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
 
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())
 
            print(self.calc_value, " ", float(self.entry_value.get()),
                                            " ", solution)
 
            # kidev vasuptaveb entry box
            self.number_entry.delete(0, "end")
 
            self.number_entry.insert(0, solution)
 
 
    def __init__(self, root):
        self.entry_value = StringVar(root, value="")
        root.title("Calculator")
        root.geometry("310x150")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)
 
        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)
        self.number_entry = ttk.Entry(root,
                        textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4)
 
        # ----- 1st Row -----
 
        self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)
 
        self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)
 
        self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)
 
        self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)
 
        # ----- 2nd Row -----
 
        self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)
 
        self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)
 
        self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)
 
        self.button_mult = ttk.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=3)
 
        # ----- 3rd Row -----
 
        self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)
 
        self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)
 
        self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)
 
        self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3)
 
        # ----- 4th Row -----
 
        self.button_clear = ttk.Button(root, text="AC", command=lambda: self.dlt_button_press()).grid(row=4, column=0)
 
        self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)
 
        self.button_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=2)
 
        self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3)
        
        # ----- 5th Row -----
        self.buttonx2 = ttk.Button(root, text="X^2", command=lambda: self.kvadrati_button_press()).grid(row=5, column=0)
        self.buttonx1_2 = ttk.Button(root, text="√", command=lambda: self.pesvi_button_press()).grid(row=5, column=1)
        
        
        
        
root = Tk()
 
calc = Calculator(root)
 
#root.mainloop()


# 1) AC gilaki ar mushaobs  // gasworda
# 2) davamato pesvis amogeba an rame msgavsi ...//akavdrateba + , pesvic davamate
# mxolod bolo or ricxvs vamaxsovrebineb sheidzleba amazec dapiqreba magram ewvi mepareba :D