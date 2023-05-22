import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title("Hospital Form")

# Create a frame to hold the widgets
frame = ttk.Frame(window, padding=10)
frame.grid()

padding_xaxis = 10
padding_yaxis = 5

#row 1
hospital_id = ttk.Label(frame, text="Hospital ID")
hospital_id.grid(row=0, column=0, sticky=tk.W)

hospital_id_entry = ttk.Entry(frame)
hospital_id_entry.grid(row=0, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def isdigit_ensure(input):
    return input.isdigit() or input == ""

isdigit_ensure_validate = (frame.register(isdigit_ensure), "%P")

hospital_id_entry.configure(validate="key", validatecommand=isdigit_ensure_validate)

hospital_name = ttk.Label(frame, text="Hospital Name")
hospital_name.grid(row=0,column=2, sticky=tk.W)

hospital_name_entry = ttk.Entry(frame)
hospital_name_entry.grid(row=0, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atmost_thirty_char_onlyalpha_ensure(input):
    return len(input) <= 30 or input == "" and input.isalpha()

atmost_thirty_char_onlyalpha_ensure_validator = (frame.register(atmost_thirty_char_onlyalpha_ensure), "%P")

hospital_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validator)

#row 2
password = ttk.Label(frame, text="Password")
password.grid(row=1, column=0, sticky=tk.W)

password_entry = ttk.Entry(frame)
password_entry.grid(row=1, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atmost_thirty_char_ensure(input):
    return len(input) <= 30 or input == ""

atmost_thirty_char_ensure_validate = (frame.register(atmost_thirty_char_ensure), "%P")


total_capacity = ttk.Label(frame, text="Total Capacity")
total_capacity.grid(row=1, column=2, sticky=tk.W)

total_capacity_entry = ttk.Entry(frame)
total_capacity_entry.grid(row=1, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def isdigit_atmost_fourhundred_ensure(input):
    return input.isdigit() and input<50 or input == ""

isdigit_atmost_fourhundred_ensure_validate = (frame.register(isdigit_atmost_fourhundred_ensure), "%P")

total_capacity_entry.configure(validate="key", validatecommand=isdigit_atmost_fourhundred_ensure_validate)

#row 3
quantity_required = ttk.Label(frame, text="Quantity Required")
quantity_required.grid(row=2, column=0, sticky=tk.W)

quantity_required_entry = ttk.Entry(frame)
quantity_required_entry.grid(row=2, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

quantity_required_entry.configure(validate="key", validatecommand=isdigit_atmost_fourhundred_ensure_validate)


contact_number = ttk.Label(frame, text="Contact Number")
contact_number.grid(row=2, column=2, sticky=tk.W)

contact_number_entry = ttk.Entry(frame)
contact_number_entry.grid(row=2, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atleast_ten_digit_ensure(input):
    return input.isdigit() and len(input) <= 10 or input == ""

atleast_ten_digit_ensure_validate = (frame.register(atleast_ten_digit_ensure), "%P")

contact_number_entry.configure(validate="key", validatecommand=atleast_ten_digit_ensure_validate)

#row 4
street_name = ttk.Label(frame, text="Street Name")
street_name.grid(row=3, column=0, sticky=tk.W)

street_name_entry = ttk.Entry(frame)
street_name_entry.grid(row=3, column=1, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

street_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validator)


city = ttk.Label(frame, text="City")
city.grid(row=3, column=2, sticky=tk.W, )

city_entry = ttk.Entry(frame)
city_entry.grid(row=3, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

city_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validator)

#row 5
district = ttk.Label(frame, text="District")
district.grid(row=4, column=0, sticky=tk.W)

district_entry = ttk.Entry(frame)
district_entry.grid(row=4, column=1, sticky=tk.W , padx= padding_xaxis,pady= padding_yaxis)

district_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validator)


state = ttk.Label(frame, text="State")
state.grid(row=4, column=2, sticky=tk.W)

state_entry = ttk.Entry(frame)
state_entry.grid(row=4, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

state_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validator)

#row 6
country = ttk.Label(frame, text="Country")
country.grid(row=5, column=0, sticky=tk.W)

country_entry = ttk.Entry(frame)
country_entry.grid(row=5, column=1, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

def atmost_twenty_char_onlyalpha_ensure(input):
    return len(input) <= 20 or input == "" and input.isalpha()

atmost_twenty_char_onlyalpha_ensure_validator = (frame.register(atmost_twenty_char_onlyalpha_ensure), "%P")
country_entry.configure(validate="key", validatecommand=atmost_twenty_char_onlyalpha_ensure_validator)

#row7
o_positive_available = ttk.Label(frame, text="O+ Available")
o_positive_available.grid(row=6, column=0, sticky=tk.W)

o_positive_available_entry = ttk.Entry(frame)
o_positive_available_entry.grid(row=6, column=1, sticky=tk.W , padx= padding_xaxis,pady= padding_yaxis)

def isdigit_atmost_fifty_ensure(input):
    return (input.isdigit() and int(input)<=50 ) or input == ""

isdigit_atmost_fifty_ensure_validate = (frame.register(isdigit_atmost_fifty_ensure), "%P")

o_positive_available_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

o_negative_available = ttk.Label(frame, text="O- Available")
o_negative_available.grid(row=6, column=2, sticky=tk.W)

o_negative_available_entry = ttk.Entry(frame)
o_negative_available_entry.grid(row=6, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

o_negative_available_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

#row 8
a_positive_available = ttk.Label(frame, text="A+ Available")
a_positive_available.grid(row=7, column=0, sticky=tk.W)

a_positive_available_entry = ttk.Entry(frame)
a_positive_available_entry.grid(row=7, column=1, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

a_positive_available_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

a_negative_available = ttk.Label(frame, text="A- Available")
a_negative_available.grid(row=7, column=2, sticky=tk.W)

a_negative_available_entry = ttk.Entry(frame)
a_negative_available_entry.grid(row=7, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

a_negative_available_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

#row 9
b_positive_available = ttk.Label(frame, text="B+ Available")
b_positive_available.grid(row=8, column=0, sticky=tk.W)

b_positive_available_entry = ttk.Entry(frame)
b_positive_available_entry.grid(row=8, column=1, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

b_positive_available_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

b_negative_available = ttk.Label(frame, text="B- Available")
b_negative_available.grid(row=8, column=2, sticky=tk.W)

b_negative_available_entry = ttk.Entry(frame)
b_negative_available_entry.grid(row=8, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

b_negative_available_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

#row 10
ab_positive_available = ttk.Label(frame, text="AB+ Available")
ab_positive_available.grid(row=9, column=0, sticky=tk.W)

ab_positive_available_entry = ttk.Entry(frame)
ab_positive_available_entry.grid(row=9, column=1, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

ab_positive_available_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

ab_negative_available = ttk.Label(frame, text="AB- Available")
ab_negative_available.grid(row=9, column=2, sticky=tk.W)

ab_negative_available_entry = ttk.Entry(frame)
ab_negative_available_entry.grid(row=9, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

ab_negative_available_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

#row 11
o_positive_maximum = ttk.Label(frame, text="O+ Maximum")
o_positive_maximum.grid(row=10, column=0, sticky=tk.W)

o_positive_maximum_entry = ttk.Entry(frame)
o_positive_maximum_entry.grid(row=10, column=1, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

o_positive_maximum_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

o_negative_maximum = ttk.Label(frame, text="O- Maximum")
o_negative_maximum.grid(row=10, column=2, sticky=tk.W)

o_negative_maximum_entry = ttk.Entry(frame)
o_negative_maximum_entry.grid(row=10, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

o_negative_maximum_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

#row 12
a_positive_maximum = ttk.Label(frame, text="A+ Maximum")
a_positive_maximum.grid(row=11, column=0, sticky=tk.W)

a_positive_maximum_entry = ttk.Entry(frame)
a_positive_maximum_entry.grid(row=11, column=1, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

a_positive_maximum_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

a_negative_maximum = ttk.Label(frame, text="A- Maximum")
a_negative_maximum.grid(row=11, column=2, sticky=tk.W)

a_negative_maximum_entry = ttk.Entry(frame)
a_negative_maximum_entry.grid(row=11, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

a_negative_maximum_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)    

#row 13
b_positive_maximum = ttk.Label(frame, text="B+ Maximum")
b_positive_maximum.grid(row=12, column=0, sticky=tk.W)

b_positive_maximum_entry = ttk.Entry(frame)
b_positive_maximum_entry.grid(row=12, column=1, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

b_positive_maximum_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

b_negative_maximum = ttk.Label(frame, text="B- Maximum")
b_negative_maximum.grid(row=12, column=2, sticky=tk.W)

b_negative_maximum_entry = ttk.Entry(frame)
b_negative_maximum_entry.grid(row=12, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

b_negative_maximum_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

#row 14
ab_positive_maximum = ttk.Label(frame, text="AB+ Maximum")
ab_positive_maximum.grid(row=13, column=0, sticky=tk.W)

ab_positive_maximum_entry = ttk.Entry(frame)
ab_positive_maximum_entry.grid(row=13, column=1, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

ab_positive_maximum_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

ab_negative_maximum = ttk.Label(frame, text="AB- Maximum")
ab_negative_maximum.grid(row=13, column=2, sticky=tk.W)

ab_negative_maximum_entry = ttk.Entry(frame)
ab_negative_maximum_entry.grid(row=13, column=3, sticky=tk.W, padx= padding_xaxis,pady= padding_yaxis)

ab_negative_maximum_entry.configure(validate="key", validatecommand=isdigit_atmost_fifty_ensure_validate)

#row 15

btn = ttk.Button(frame, text="Submit")
btn.grid(row=14, column=1)

frame.mainloop()

# Start the main loop
window.mainloop()

