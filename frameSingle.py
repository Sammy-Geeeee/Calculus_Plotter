# This will define the single function frame


from ctypes import alignment
from functionSingle import *
import tkinter as tk
import numpy as np
from sympy import Symbol, sympify, solve, Integral, Derivative, sqrt, sin, cos, tan
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class FrameSingle(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some base variables for sizing of various things
        pad_ext = 5
        pad_int = 2
        entry_width = 10
        label_width = 5


        # To make all the widgets within the single function tab
        self.frame_text = tk.Frame(self.master)
        self.frame_graph = tk.Frame(self.master)
        # Positions of these frames
        self.frame_text.grid(row=0, column=0, sticky='new')
        self.frame_graph.grid(row=0, column=1, padx=pad_ext, pady=pad_ext, sticky='nsew')
        # Configs for these frames
        self.frame_graph.columnconfigure([0], weight=1)
        self.frame_graph.rowconfigure([0], weight=1)
        self.frame_text.columnconfigure([0], weight=1)
        self.frame_text.rowconfigure([2], weight=1)
        

        # Widgets in the text frame
        self.frame_inputs = tk.Frame(self.frame_text)
        self.frame_answers = tk.Frame(self.frame_text)
        self.frame_points = tk.Frame(self.frame_text)
        # To position them
        self.frame_inputs.grid(row=0, column=0, sticky='ew')
        self.frame_answers.grid(row=1, column=0, pady=[0, 5*pad_ext], sticky='w')
        self.frame_points.grid(row=2, column=0, sticky='nsew')
        # Configs for these frames
        self.frame_inputs.columnconfigure([1, 3], weight=1)
        self.frame_points.rowconfigure([1], weight=1)
        self.frame_points.columnconfigure([0, 1, 2], weight=1)
        

        # Widgets in the inputs frame
        self.label_func = tk.Label(self.frame_inputs, text='Function (y=f(x))')
        self.entry_func = tk.Entry(self.frame_inputs)
        self.label_x1 = tk.Label(self.frame_inputs, text='x1')
        self.entry_x1 = tk.Entry(self.frame_inputs)
        self.label_x2 = tk.Label(self.frame_inputs, text='x2')
        self.entry_x2 = tk.Entry(self.frame_inputs)
        self.button_perform = tk.Button(self.frame_inputs, command=self.plotObject, text='Plot & Calculate')
        # Positions
        self.label_func.grid(row=0, column=0, padx=pad_ext, pady=pad_ext, sticky='e')
        self.entry_func.grid(row=0, column=1, columnspan=3, padx=pad_ext, pady=pad_ext, sticky='ew')
        self.label_x1.grid(row=1, column=0, padx=pad_ext, pady=pad_ext, sticky='e')
        self.entry_x1.grid(row=1, column=1, padx=pad_ext, pady=pad_ext, sticky='ew')
        self.label_x2.grid(row=1, column=2, padx=[3*pad_ext, pad_ext], pady=pad_ext, sticky='e')
        self.entry_x2.grid(row=1, column=3, padx=pad_ext, pady=pad_ext, sticky='ew')
        self.button_perform.grid(row=2, column=0, columnspan=4, padx=pad_ext, pady=[3*pad_ext, 5*pad_ext])


        # Widgets in the answers tab
        self.label_deriv = tk.Label(self.frame_answers, width=3*label_width, text='Derivative:')
        self.label_integ = tk.Label(self.frame_answers, width=3*label_width, text='Integral:')
        self.label_area = tk.Label(self.frame_answers, width=3*label_width, text='Area:')
        self.label_length = tk.Label(self.frame_answers, width=3*label_width, text='Length:')
        # StringVar's for the changing values
        self.string_deriv = tk.StringVar(self.frame_answers)
        self.string_integ = tk.StringVar(self.frame_answers)
        self.string_area = tk.StringVar(self.frame_answers)
        self.string_length = tk.StringVar(self.frame_answers)
        # The remaining widgets
        self.label_deriv_val = tk.Label(self.frame_answers, textvariable=self.string_deriv)
        self.label_integ_val = tk.Label(self.frame_answers, textvariable=self.string_integ)
        self.label_area_val = tk.Label(self.frame_answers, textvariable=self.string_area)
        self.label_length_val = tk.Label(self.frame_answers, textvariable=self.string_length)
        # Positioning all these things
        self.label_deriv.grid(row=0, column=0, padx=pad_ext, pady=pad_ext, sticky='e')
        self.label_integ.grid(row=1, column=0, padx=pad_ext, pady=pad_ext, sticky='e')
        self.label_area.grid(row=2, column=0, padx=pad_ext, pady=pad_ext, sticky='e')
        self.label_length.grid(row=3, column=0, padx=pad_ext, pady=pad_ext, sticky='e')
        self.label_deriv_val.grid(row=0, column=1, padx=pad_ext, pady=pad_ext, sticky='e')
        self.label_integ_val.grid(row=1, column=1, padx=pad_ext, pady=pad_ext, sticky='e') 
        self.label_area_val.grid(row=2, column=1, padx=pad_ext, pady=pad_ext, sticky='e')
        self.label_length_val.grid(row=3, column=1, padx=pad_ext, pady=pad_ext, sticky='e')


        # Widgets in the points frame
        self.label_max = tk.Label(self.frame_points, text='Max. Points:')
        self.label_min = tk.Label(self.frame_points, text='Min. Points:')
        self.label_inf = tk.Label(self.frame_points, text='Inf. Points:')
        self.list_max = tk.Listbox(self.frame_points, height=1000)
        self.list_min = tk.Listbox(self.frame_points, height=1000)
        self.list_inf = tk.Listbox(self.frame_points, height=1000)
        # Their positioning
        self.label_max.grid(row=0, column=0, padx=pad_ext, pady=pad_ext)
        self.label_min.grid(row=0, column=1, padx=pad_ext, pady=pad_ext)
        self.label_inf.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.list_max.grid(row=1, column=0, padx=pad_ext, pady=pad_ext) 
        self.list_min.grid(row=1, column=1, padx=pad_ext, pady=pad_ext) 
        self.list_inf.grid(row=1, column=2, padx=pad_ext, pady=pad_ext) 


    def plotObject(self):
        # This will get all the function info
        function = str(self.entry_func.get())
        x1 = float(self.entry_x1.get())
        x2 = float(self.entry_x2.get())

        # This will do the plotting of the function
        function_info = singleFunction(function, x1, x2)
        canvas = canvasObject(function_info, self.frame_graph)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')

        # To update all the function info
        self.string_deriv.set(function_info['derivative'])
        self.string_integ.set(function_info['integral'])
        self.string_area.set(f"{function_info['area']:.2f}")
        self.string_length.set(f"{function_info['length']:.2f}")


        # To reset the lists
        self.list_max.delete(0, 'end')
        self.list_min.delete(0, 'end')
        self.list_inf.delete(0, 'end')

        # To add all the values to the lists
        for max in function_info['maxes']:
            self.list_max.insert(tk.END, f'{float(max[0]):.2f}        {float(max[1]):.2f}')  # To add each of the point coordinates to the list
        for min in function_info['mins']:
            self.list_min.insert(tk.END, f'{float(min[0]):.2f}        {float(min[1]):.2f}')
        for inf in function_info['infs']:
            self.list_inf.insert(tk.END, f'{float(inf[0]):.2f}        {float(inf[1]):.2f}')
