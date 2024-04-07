# Euler's Method
# importing and setting variables
# Note: You WILL need an editor and Python installed on your computer to run the following code
# Note: The following code 

import tkinter as tk
from tkinter import ttk
import sympy as sp
from sympy.abc import x,y
from numpy import arange
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)



class Application:
    """Application root window"""

    def __init__(self, master):
        
        self.final_val = tk.StringVar()
        self.final_val.set("Enter ALL the values then press submit to get the result")
        input_frame = ttk.Frame(master)
        input_frame.pack()
        
        self.dy = sp.Symbol('dy')
        self.C = sp.Symbol('C')
        
        ttk.Label(input_frame, text = 'Deltax:').grid(row = 0, column = 0, padx = 10, sticky = 'sw')
        ttk.Label(input_frame, text = 'Start x value:').grid(row = 0, column = 1, padx = 10, sticky = 'sw')
        ttk.Label(input_frame, text = 'Start y value:').grid(row = 0, column = 2, sticky = 'sw', padx = 10)
        ttk.Label(input_frame, text = 'End x value:').grid(row = 0, column = 3, sticky = 'sw', padx = 10)
        ttk.Label(input_frame, textvariable = self.final_val, wraplength = 750).grid(
            row = 8, column = 0, columnspan = 4, padx = 10)
        ttk.Label(input_frame, text = "Please enter the equation of the derivative as all terms of y on the LHS" +
                  " and all terms of x on the RHS (ignore any dy and dx). " +
                  "Note: Any variables aside from x and y will be considered as constants"
                  , wraplength = 740).grid(row = 4, column = 0, columnspan = 4, padx = 10)
        ttk.Label(input_frame, text = 'Expression of y:').grid(row = 5, column = 0, padx = 10, sticky = 'sw')
        ttk.Label(input_frame, text = 'Expression of x:').grid(row = 5, column = 1, padx = 10, sticky = 'sw')
        
        fig = Figure(figsize = (5, 5), dpi = 100)
        self.plot1 = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master = master)  
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(self.canvas, master)
        toolbar.update()
        self.canvas.get_tk_widget().pack()
        
        canvas_frame = ttk.Frame(master)
        canvas_frame.pack()

        self.entry_Deltax = ttk.Entry(input_frame, width = 24, font = ('Arial', 10))
        self.entry_Deltax.grid(row = 1, column = 0)

        self.entry_x = ttk.Entry(input_frame, width = 24, font = ('Arial', 10))
        self.entry_x.grid(row = 1, column = 1)

        self.entry_y = ttk.Entry(input_frame, width = 24, font = ('Arial', 10))
        self.entry_y.grid(row = 1, column = 2)

        self.entry_final_x = ttk.Entry(input_frame, width = 24, font = ('Arial', 10))
        self.entry_final_x.grid(row = 1, column = 3)
        
        self.y_der = ttk.Entry(input_frame, width = 24, font = ('Arial', 10))
        self.y_der.grid(row = 6, column = 0)
        
        self.x_der = ttk.Entry(input_frame, width = 24, font = ('Arial', 10))
        self.x_der.grid(row = 6, column = 1)
        
        self.entry_x_min = ttk.Entry(canvas_frame, width = 24, font = ('Arial', 10))
        self.entry_x_min.grid(row = 1, column = 0)
        
        self.entry_x_max = ttk.Entry(canvas_frame, width = 24, font = ('Arial', 10))
        self.entry_x_max.grid(row = 1, column = 1) 
        
        self.entry_y_min = ttk.Entry(canvas_frame, width = 24, font = ('Arial', 10))
        self.entry_y_min.grid(row = 1, column = 2)
        
        self.entry_y_max = ttk.Entry(canvas_frame, width = 24, font = ('Arial', 10))
        self.entry_y_max.grid(row = 1, column = 3)
        
        ttk.Label(canvas_frame, text = 'Min Domain:').grid(row = 0, column = 0, padx = 10, sticky = 'sw')
        ttk.Label(canvas_frame, text = 'Max Domain:').grid(row = 0, column = 1, padx = 10, sticky = 'sw')
        ttk.Label(canvas_frame, text = 'Min Range:').grid(row = 0, column = 2, padx = 10, sticky = 'sw')
        ttk.Label(canvas_frame, text = 'Max Range:').grid(row = 0, column = 3, padx = 10, sticky = 'sw')

        ttk.Button(input_frame, text = 'Submit', command = lambda: self.input()
                   ).grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "e", columnspan = 2)
        ttk.Button(input_frame, text = 'Clear', command = lambda: self.clear()
                   ).grid(row = 7, column = 2, padx = 5, pady = 5, sticky = "w", columnspan = 2)
                   
        
        self.canvas.get_tk_widget().bind("<ButtonRelease-1>", lambda e: self.get_lim())


    
    def input(self):
        # Validates all User inputs and calls method
        try:
            self.Deltax = float(self.entry_Deltax.get())
        except ValueError:
            self.final_val.set("Enter a Valid Number then press submit")
            self.entry_Deltax.delete(0, 'end')
            return
        try:
            self.x_val = float(self.entry_x.get())
        except ValueError:
            self.final_val.set("Enter a Valid Number then press submit")
            self.entry_x.delete(0, 'end')
            return
        try:
            self.y_val = float(self.entry_y.get())
        except ValueError:
            self.final_val.set("Enter a Valid Number then press submit")
            self.entry_y.delete(0, 'end')
            return
        try:
            self.final_x = float(self.entry_final_x.get())
        except ValueError:
            self.final_val.set("Enter a Valid Number then press submit")
            self.entry_final_x.delete(0, 'end')
            return
        
        try:
            self.x_min = float(self.entry_x_min.get())
        except ValueError:
            self.final_val.set("Enter a Valid Number then press submit")
            self.entry_x_min.delete(0, 'end')
            return
        
        try:
            self.x_max = float(self.entry_x_max.get())
        except ValueError:
            self.final_val.set("Enter a Valid Number then press submit")
            self.entry_x_max.delete(0, 'end')
            return
        
        if self.Deltax == 0.0:
            self.final_val.set("Delta x cannot be zero")
            return
        
        self.equation = self.x_der.get()
        self.equation = self.equation.replace('^', "**")
        self.equation =  self.equation.replace('pi', "π")
        try:
            antideriv_x = sp.integrate(sp.parse_expr(self.equation).subs("x", x), x) + self.C
            deriv_x = sp.parse_expr(self.equation).subs("x", x)
        except:
            self.final_val.set("Enter a Valid equation then press submit. Make sure you are using * sign EVERYTIME you are multiplying")
            return
        
        # Adjust Expressions to be used to calculate
        
        self.equation = self.y_der.get()
        self.equation = self.equation.replace('^', "**")
        self.equation = self.equation.replace('pi', "π")
        
        antideriv_y = sp.integrate(sp.parse_expr(self.equation).subs("y", y), y)
        deriv_y = sp.parse_expr(self.equation + '*dy').subs("y", y).subs("dy", self.dy)
        
        self.antideriv = sp.Eq(antideriv_y ,antideriv_x)
        self.c = sp.solve(self.antideriv.subs(x, self.x_val).subs(y, self.y_val), self.C)
        self.antideriv = self.antideriv.subs(self.C, self.c[0])
        print(self.antideriv)
        self.deriv = sp.Eq(deriv_y, deriv_x)
        
        self.plot1.set_xlim([self.x_min, self.x_max])
    
        self.method()
        
                

    def method(self):
        """
        Solves for the final answer
        Disclamer: If your final value and x incremented by Deltax do not match. It may result in a wrong estimate.
        (eg. deltax = 0.1, x = 3, final_x = 3.25. The code will return the estimate for x = 3.2 not x = 3.25)
        """
        
        self.graph()
        
        cords = []
        list_x = []
        list_y = []
        cords.append(self.x_val)
        cords.append(self.y_val) 
        slope = self.solve(self.x_val, self.y_val) 
        if self.final_x > self.x_val: # if the final_x is greater than x we increment x
            while self.x_val < self.final_x: 
                self.x_val += self.Deltax # incrementing x by constant
                self.y_val = cords.pop() + slope[0] *(self.x_val - cords.pop()) # solving for the new y value on the tangent line
                slope = self.solve(self.x_val,self.y_val)
                cords.append(self.x_val)
                list_x.append(self.x_val)
                cords.append(self.y_val)
                list_y.append(self.y_val)
        elif self.final_x < self.x_val: # However if the final_x is less than x we decrement x 
            while self.x_val > self.final_x:
                self.x_val -= self.Deltax # decrementing x by constant
                self.y_val = cords.pop() + slope[0]*(self.x_val-cords.pop()) # solving for the new y value on the tangent line
                slope = self.solve(self.x_val,self.y_val)
                cords.append(self.x_val)
                list_x.append(self.x_val)
                cords.append(self.y_val)
                list_y.append(self.y_val)
                
        if str(self.y_val) == 'inf' or str(self.y_val) == 'nan':
            self.final_val.set("The result is too large please check your values")
        else:
            self.final_val.set("Result: "+ str(self.y_val) + "\nC = " + str(self.c[0]))
        
        
        self.plot1.plot(list_x, list_y, color = "orange")
        self.canvas.draw()
        
    
    def solve(self, x_val, y_val):
        # Finds the slope of the graph at a point
        temp = self.deriv.subs(x, x_val)
        temp = temp.subs(y, y_val)
        return sp.solve(temp, self.dy) 
    
    def clear(self):
        # Clears all entry fields beside domain 
        self.entry_Deltax.delete(0, 'end')
        self.entry_x.delete(0, 'end')
        self.entry_y.delete(0, 'end')
        self.entry_final_x.delete(0, 'end')
        self.y_der.delete(0, 'end')
        self.x_der.delete(0, 'end')
        self.final_val.set("Enter ALL the values then press submit to get the result")
        
        
    def graph(self):
        # Plots the graph of the antiderivative on the matplotlib graph
        self.plot1.clear() 
        y_val = []
        x_val = []
        self.maximum = 1
        i = 0
        while i <= self.maximum:
            for r in arange(self.x_min, self.x_max, 0.5):
                temp = self.antideriv.subs(x, r)                  
                temp1 = sp.solve(temp, y)
                if len(temp1) > self.maximum:
                    self.maximum = len(temp1)
                if i + 1 <= len(temp1) and 'I' not in str(temp1[i]): # checking if number is complex
                    y_val.append(temp1[i])
                    x_val.append(r)
                elif 'I' not in str(temp1[len(temp1) - 1]):
                    y_val.append(temp1[len(temp1) - 1])
                    x_val.append(r)
            self.plot1.plot(x_val, y_val, color="blue")
            self.canvas.draw()
            y_val = []
            x_val = []
            i += 1
            
    def get_lim(self):
    
        cords = self.plot1.get_xlim()
        self.entry_x_min.delete(0, 'end')
        self.entry_x_max.delete(0, 'end')
        self.entry_x_min.insert(0, cords[0])
        self.entry_x_max.insert(0, cords[1])
        
            

if __name__ == "__main__":
    root = tk.Tk()
    application = Application(root)
    root.mainloop()