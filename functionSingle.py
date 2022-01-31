# The functions for the single function tab will be here


import numpy as np
from sympy import Symbol, sympify, solve, Integral, Derivative, sqrt, sin, cos, tan
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def singleFunction(function, x1, x2):
    # Make the function into a sympify object and define the domain (x values) of the function
    func = sympify(function)
    var = Symbol('x')

    # To divide x space into appropriate values, and list y values
    x_vals = np.linspace(x1, x2, 1000)
    y_vals = []
    for x in x_vals:
        y_vals.append(func.subs({var: x}))

    # To save the derived and integrated functions
    deriv = Derivative(func, var).doit()
    deriv2 = Derivative(func, var, 2).doit()
    integ = Integral(func, var).doit()


    # To make lists of all the critical and inflection points
    crits = sorted(solve(deriv, var))
    inflects = sorted(solve(deriv2, var))
    
    # To make lists of all the max and min points
    maxes, mins = [], []
    for point in crits:
        if not (point < x1 or point > x2):
            value = func.subs({var: point})  # The y value at point x
            deriv2_val = deriv2.subs({var: point})  # The derivative at point x
            if deriv2_val < 0:
                maxes.append((point, value))
            elif deriv2_val > 0:
                mins.append((point, value))

    # To find all the inflection points
    infs = []
    for point in inflects:
        if not (point < x1 or point > x2):
            value = func.subs({var: point})
            infs.append((point, value))

    # To list all the x intercepts
    try:
        x_ints = sorted(solve(func, var))  # To make a list of all the x axes intercepts
    except TypeError:  # This exception is raised sometimes when it cannot find intercepts
        x_ints = []


    # To store all the boundary points, for starting/ending sections of areas
    bounds = []
    for point in x_ints:
        if x1 < point < x2:
            bounds.append(point)

    # This is to help find the bounds of each area
    if len(bounds) < 1:  # This will sort out all the functions that don't have x intercepts, as they will be simple
        area = abs(Integral(func, (var, x1, x2)).doit())
    else:
        sections = [(x1, bounds[0])]  # To start off the first section of the areas need to be found
        
        # Now to find the next area bounds
        for i, v in enumerate(bounds):
            try:
                sections.append((bounds[i], bounds[i+1]))  # To find each set of points that we will need to integrate for
            except IndexError:  # To prevent it from looking beyond the max index of the list
                pass
        sections.append((bounds[-1], x2))

        # Now to find all the areas
        areas = []
        for section in sections:
            areas.append(abs(Integral(func, (var, section[0], section[1])).doit()))
        area = sum(areas)


    # To find the length of the curve
    length = Integral(sqrt(1 + deriv**2), (var, x1, x2)).doit()

    return {
        'function': func,
        'var': var,
        'range': [x1, x2],
        'derivative': deriv,
        'derivative2': deriv2,
        'integral': integ,
        'area': float(area),
        'length': float(length),
        'maxes': maxes,
        'mins': mins,
        'infs': infs,
        'xvals': x_vals,
        'yvals': y_vals
    }
    

def canvasObject(function_info, frame):
    fig = Figure(figsize=[6.4*5, 4.8*5])
    plot = fig.add_subplot(111)

    max_x, max_y, min_x, min_y, inf_x, inf_y = [], [], [], [], [], []  # Blank list for all the critical point coordinates
    for point in function_info['maxes']:  # To add all the max point information to the list
        max_x.append(point[0])
        max_y.append(point[1])
    for point in function_info['mins']:
        min_x.append(point[0])
        min_y.append(point[1])
    for point in function_info['infs']:
        inf_x.append(point[0])
        inf_y.append(point[1])

    plot.plot(function_info['xvals'], function_info['yvals'], zorder=5)  # to plot the main function
    max_points = plot.scatter(max_x, max_y, color='red', zorder=10)  # To plot the max, min, and inflection points
    min_points = plot.scatter(min_x, min_y, color='green', zorder=10)
    inf_points = plot.scatter(inf_x, inf_y, color='orange', zorder=10)

    plot.set_title(f'f({function_info["var"]}) = {function_info["function"]}  {function_info["range"]}')
    plot.axhline(color='black', linestyle='dotted', zorder=0)  # To show the horizontal and vertical axes
    plot.axvline(color='black', linestyle='dotted', zorder=0)
    plot.legend((max_points, min_points, inf_points), ('Max.', 'Min.', 'Inf.'))  # To show a legend

    canvas = FigureCanvasTkAgg(fig, frame)# Creating a tkinter canvas
    return canvas
