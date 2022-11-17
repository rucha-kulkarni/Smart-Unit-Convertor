from tkinter import *
from tkinter import ttk

root = Tk()
root.title('SMART UNIT CONVERTER')
root.geometry("455x350+500+200")
label = Label(root, text='SMART UNIT CONVERTER', justify=CENTER, font=("Arial", 20, "italic"))
label.place(x=50, y=20)
Button(root, text="QUIT", bg="white", fg="blue", font=("Arial", 14, "bold"), relief=SUNKEN, bd=5, overrelief=GROOVE, activebackground="light pink", activeforeground="black", command=root.destroy).place(x=330, y=300)


def currency_converter():
    # factors to multiply to a value to convert from the following units to INR
    factors = {'USD': 81.64, 'EUR': 84.47, 'INR': 1}
    ids = {"US Dollar": 'USD', "Euros": 'EUR', "Indian Rupees": 'INR'}

    def convert(amt, frm, to):
        if frm != 'INR':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def clear():
        in_amt.set("")
        out_amt.set("")

    def callback():
        try:
            amt = float(input.get())

        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    top = Toplevel()
    top.title("Currency Converter")

# initiate frame
    frame = ttk.Frame(top, padding="5 12 7 12")
    frame.pack()
    Label(frame, text="Currency Converter", font=("Arial", 12, "bold")).grid(column=1, row=1)
    in_amt = StringVar()
    in_amt.set('')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

# Add input field
    input = ttk.Entry(frame, width=20, textvariable=in_amt)
    input.grid(row=1, column=2, sticky=(W, E))

# Add drop-down for input unit
    in_select = OptionMenu(frame, in_unit, "US Dollar", "Euros", "Indian Rupees").grid(column=3, row=1, sticky=W)

# Add output field and drop-down
    ttk.Entry(frame, textvariable=out_amt, state="readonly").grid(column=2, row=2, sticky=(W, E))
    in_select = OptionMenu(frame, out_unit, "US Dollar", "Euros", "Indian Rupees").grid(column=3, row=2, sticky=W)

    calculate = ttk.Button(frame, text="Calculate", command=callback).grid(column=2, row=3, sticky=E)
    clear = ttk.Button(frame, text="Clear", command=clear).grid(column=3, row=3, sticky=E)


def weight_converter():
    # factors to multiply to a value to convert from the following units to meters(m)
    factors = {'kg': 1000, 'g': 1, 'mg': 0.001, 't': 1000000, 'lbs': 453.592}
    ids = {"Kilogram": 'kg', "gram": 'g', "Milligram": 'mg', "Tons": 't', "Pound": 'lbs'}
# function to convert from a given unit to another

    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def clear():
       in_amt.set("")
       out_amt.set("")

    def callback():
        try:
            amt = float(input.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

# initiate window
    top = Toplevel()
    top.title("Weight Converter")

# initiate frame
    frame = ttk.Frame(top, padding="5 12 7 12")
    frame.pack()
    Label(frame, text="Weight Converter", font=("Arial", 12, "bold")).grid(column=1, row=1)

    in_amt = StringVar()
    in_amt.set('')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    # Add input field
    input = ttk.Entry(frame, width=20, textvariable=in_amt)
    input.grid(row=1, column=2, sticky=(W, E))

# Add drop-down for input unit
    in_select = OptionMenu(frame, in_unit, "Kilogram", "gram", "Milligram", "Tons", "Pound") .grid(column=3, row=1, sticky=W)

# Add output field and drop-down
    ttk.Entry(frame, textvariable=out_amt, state="readonly").grid(column=2, row=2, sticky=(W, E))
    in_select = OptionMenu(frame, out_unit, "Kilogram", "gram", "Milligram", "Tons", "Pound").grid(column=3, row=2, sticky=W)

    calculate = ttk.Button(frame, text="Calculate", command=callback).grid(column=2, row=3, sticky=E)
    clear = ttk.Button(frame, text="Clear", command=clear).grid(column=3, row=3, sticky=E)


def length_converter():
    # factors to multiply to a value to convert from the following units to meters(m)
    factors = {'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001}
    ids = {"Miles": 'mi', "Yards": 'yd', "Feet": 'ft', "Inches": 'inch', "Kilometers": 'km', "Meters": 'm', "Centimeters": 'cm', "Millimeters": 'mm'}

# function to convert from a given unit to another
    def convert(amt, frm, to):
        if frm != 'm':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def clear():
        in_amt.set("")
        out_amt.set("")

    def callback():
        try:
            amt = float(input.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

# initiate window
    top = Toplevel()
    top.title("Length Converter")

# initiate frame
    frame = ttk.Frame(top, padding="5 12 7 12")
    frame.pack()
    Label(frame, text="Length Converter", font=("Arial", 12, "bold")).grid(column=1, row=1)

    in_amt = StringVar()
    in_amt.set('')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

# Add input field
    input = ttk.Entry(frame, width=20, textvariable=in_amt)
    input.grid(row=1, column=2, sticky=(W, E))

# Add drop-down for input unit
    in_select = OptionMenu(frame, in_unit, "Miles", "Yards", "Feet", "Inches", "Kilometers", "Meters", "Centimeters", "Millimeters").grid(column=3, row=1, sticky=W)

# Add output field and drop-down
    ttk.Entry(frame, textvariable=out_amt, state="readonly").grid(column=2, row=2, sticky=(W, E))
    in_select = OptionMenu(frame, out_unit,  "Miles", "Yards", "Feet", "Inches", "Kilometers", "Meters", "Centimeters", "Millimeters").grid(column=3, row=2, sticky=W)

    calculate = ttk.Button(frame, text="Calculate", command=callback).grid(column=2, row=3, sticky=E)
    clear = ttk.Button(frame, text="Clear", command=clear).grid(column=3, row=3, sticky=E)


def temperature_converter():
    ids = {'celsius': "c", 'fahrenheit': "f", 'kelvin': "K"}

    # function to convert from a given unit to another
    def convert(amt, frm, to):
        if frm == 'K' and to == 'c':
            amt = amt - 273.15
            return amt
        elif frm == 'K' and to == 'f':
            amt = (amt - 273.15)*1.8 + 32
            return amt
        elif frm == 'f' and to == 'c':
            amt = (amt - 32)*0.555
            return amt
        elif frm == 'f' and to == 'K':
            amt = (amt - 32)*0.555 + 273.15
            return amt
        elif frm == 'c' and to == 'f':
            amt = (amt * 1.8)+32
            return amt
        elif frm == 'c' and to == 'K':
            amt = amt + 273.15
            return amt

    def clear():
        in_amt.set("")
        out_amt.set("")

    def callback():
        try:
            amt = float(input.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    # initiate window
    top = Toplevel()
    top.title("Temperature Converter")

    # initiate frame
    frame = ttk.Frame(top, padding="5 12 7 12")
    frame.pack()
    Label(frame, text="Temperature Converter", font=("Arial", 12, "bold")).grid(column=1, row=1)

    in_amt = StringVar()
    in_amt.set('')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    # Add input field
    input = ttk.Entry(frame, width=20, textvariable=in_amt)
    input.grid(row=1, column=2)

    # Add drop-down for input unit
    in_select = OptionMenu(frame, in_unit, "celsius", "fahrenheit", 'kelvin').grid(column=3, row=1, sticky=W)

    # Add output field and drop-down
    ttk.Entry(frame, textvariable=out_amt, state="readonly").grid(column=2, row=2, sticky=(W, E))
    in_select = OptionMenu(frame, out_unit,  "celsius", "fahrenheit", 'kelvin').grid(column=3, row=2, sticky=W)

    calculate = ttk.Button(frame, text="Calculate", command=callback).grid(column=2, row=3, sticky=E)
    clear = ttk.Button(frame, text="Clear", command=clear).grid(column=3, row=3, sticky=E)


Button(root, text="Currency converter", bg="white", fg="red", bd=3, font=("Arial", 14, "bold"), relief=RAISED, overrelief=GROOVE, activebackground="light blue", activeforeground="blue", command=currency_converter).place(x=50, y=60)
Button(root, text="Length Converter", bg="white", fg="red", bd=3, font=("Arial", 14, "bold"), relief=RAISED, overrelief=GROOVE, activebackground="light blue", activeforeground="blue", command=length_converter).place(x=50, y=120)
Button(root, text="Weight Converter", bg="white", fg="red", bd=3, font=("Arial", 14, "bold"), relief=RAISED, overrelief=GROOVE, activebackground="light blue", activeforeground="blue", command=weight_converter).place(x=50, y=180)
Button(root, text="Temperature Converter", bg="white", fg="red", bd=3, font=("Arial", 14, "bold"), relief=RAISED, overrelief=GROOVE, activebackground="light blue", activeforeground="blue", command=temperature_converter).place(x=50, y=240)
root.mainloop()