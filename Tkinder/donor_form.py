import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title("Donor Form")

# Create a frame to hold the widgets
# frame = tk.Frame(window, bg='grey', width = 500, height=50,padx=20, pady=20)
frame = tk.Frame(window,padx=20, pady=20)

frame.grid()

# Create labels and entries for each column in the table

#row 1
width_combobox = 17
padding_xaxis = 10
padding_yaxis = 5

First_name = ttk.Label(frame, text="First Name")
First_name.grid(row=0, column=0, sticky=tk.W)

First_name_entry = ttk.Entry(frame)
First_name_entry.grid(row=0, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atmost_twenty_char_onlyalpha_ensure(input):
    return input.isalpha() and len(input) <= 20 or input == ""

atmost_twenty_char_onlyalpha_validator = (frame.register(atmost_twenty_char_onlyalpha_ensure), "%P")

First_name_entry.configure(validate="key", validatecommand=atmost_twenty_char_onlyalpha_validator)


Last_name = ttk.Label(frame, text="Last Name")
Last_name.grid(row=0, column=2, sticky=tk.W)

Last_name_entry = ttk.Entry(frame)
Last_name_entry.grid(row=0, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Last_name_entry.configure(validate="key", validatecommand=atmost_twenty_char_onlyalpha_validator)

#row 2
adhaar_id = ttk.Label(frame, text="Aadhaar ID")
adhaar_id.grid(row=1, column=0, sticky=tk.W)

adhaar_id_entry = ttk.Entry(frame)
adhaar_id_entry.grid(row=1, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atleast_twelve_digit_ensure(input):
    return input.isdigit() and len(input) <= 12 or input == ""

atleast_twelve_digit_ensure_validate = (frame.register(atleast_twelve_digit_ensure), "%P")

adhaar_id_entry.configure(validate="key", validatecommand=atleast_twelve_digit_ensure_validate)


gender = ttk.Label(frame,text="Gender")
gender.grid(row=1, column=2, sticky=tk.W)

# Create a list of gender options
gender_options = ["Male", "Female", "Nonbinary", "Other"]

# Create a combobox with the gender_options as values
gender = ttk.Combobox(frame, width=width_combobox, textvariable=tk.StringVar(), values=gender_options)
gender.grid(row=1, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


#row 3
Date_of_birth = ttk.Label(frame, text="Date of Birth (DD/MM/YYYY)")
Date_of_birth.grid(row=2, column=0, sticky=tk.W)

Date_of_birth_entry = ttk.Entry(frame)
Date_of_birth_entry.grid(row=2, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def date_of_birth_ensure(input):
    return len(input) <= 10 or input == ""

date_of_birth_validate = (frame.register(date_of_birth_ensure), "%P")

Date_of_birth_entry.configure(validate="key", validatecommand=date_of_birth_validate)


Blood_type = ttk.Label(frame, text="Blood Type")
Blood_type.grid(row=2, column=2, sticky=tk.W)

Blood_type = ttk.Combobox(frame, width = width_combobox, textvariable = tk.StringVar(), values=["A+","A-","B+","B-","AB+","AB-","O+","O-"])
Blood_type.grid(row=2, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


#row 4
Pregnancy_status = ttk.Label(frame, text="Pregnancy Status")
Pregnancy_status.grid(row=3, column=0, sticky=tk.W)

Pregnancy_status = ttk.Combobox(frame, width = width_combobox, textvariable = tk.StringVar(), values=["Yes","No"])
Pregnancy_status.grid(row=3, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


HIV_status = ttk.Label(frame, text="HIV Status")
HIV_status.grid(row=3, column=2, sticky=tk.W)

HIV_status = ttk.Combobox(frame, width = width_combobox, textvariable = tk.StringVar(), values=["Positive","Negative"])
HIV_status.grid(row=3, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


#row 5
Street_name = ttk.Label(frame, text="Street Name")
Street_name.grid(row=4, column=0, sticky=tk.W)

Street_name_entry = ttk.Entry(frame)
Street_name_entry.grid(row=4, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)

def atmost_fifty_char_ensure(input):
    return input.isalpha() and len(input) <= 20 or input == ""

street_address_validator = (frame.register(atmost_fifty_char_ensure), "%P")

Street_name_entry.configure(validate="key", validatecommand=street_address_validator)


City = ttk.Label(frame, text="City")
City.grid(row=4, column=2, sticky=tk.W)

City_entry = ttk.Entry(frame)
City_entry.grid(row=4, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atmost_thirty_char_ensure(input):
    return len(input) <= 30 or input == ""

atmost_thirty_char_ensure_validator = (frame.register(atmost_thirty_char_ensure), "%P")

City_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validator)


#row 6
District = ttk.Label(frame, text="District")
District.grid(row=5, column=0, sticky=tk.W)

District_entry = ttk.Entry(frame)
District_entry.grid(row=5, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

District_entry.configure(validate="key",validatecommand=atmost_thirty_char_ensure_validator)

State = ttk.Label(frame, text="State")
State.grid(row=5, column=2, sticky=tk.W)

State_entry = ttk.Entry(frame)
State_entry.grid(row=5, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

State_entry.configure(validate="key",validatecommand=atmost_thirty_char_ensure_validator)

#row 7
Country = ttk.Label(frame, text="Country")
Country.grid(row=6, column=0, sticky=tk.W)

Country_entry = ttk.Entry(frame)
Country_entry.grid(row=6, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atmost_twenty_char_ensure(input):
    return len(input) <= 20 or input == ""

atmost_twenty_char_ensure_validator = (frame.register(atmost_twenty_char_ensure), "%P")

Country_entry.configure(validate="key",validatecommand=atmost_twenty_char_ensure_validator)

Country_code = ttk.Label(frame,text="Country Code (ex: +91)")
Country_code.grid(row=6, column=2, sticky=tk.W)

Country_code_entry = ttk.Entry(frame)
Country_code_entry.grid(row=6, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atmost_plus_three_char_ensure(input):
    if(input!=""):
        if(len(input)<=3):
            if(len(input)==1 and input[0]=='+'):
                return True

            elif(len(input)==2 and input[0]=='+' and input[1].isdigit()):
                return True
        
            elif(len(input)==3 and input[0]=='+' and input[1].isdigit() and input[2].isdigit() ):
                return True
        
            return False
        
        
        return False
    
    return True

atmost_plus_three_char_ensure_validator = (frame.register(atmost_plus_three_char_ensure), "%P")

Country_code_entry.configure(validate="key",validatecommand=atmost_plus_three_char_ensure_validator)


#row 8
Father_name = ttk.Label(frame, text="Father Name")
Father_name.grid(row=7, column=0, sticky=tk.W)

Father_name_entry = ttk.Entry(frame)
Father_name_entry.grid(row=7, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)

def atmost_thirty_char_onlyalpha_ensure(input):
    return len(input) <= 30 or input == "" and input.isalpha()

atmost_thirty_char__onlyalpha_ensure_validator = (frame.register(atmost_thirty_char_onlyalpha_ensure), "%P")

Father_name_entry.configure(validate="key", validatecommand=atmost_thirty_char__onlyalpha_ensure_validator)


Mother_name = ttk.Label(frame, text="Mother Name")
Mother_name.grid(row=7, column=2, sticky=tk.W)

Mother_name_entry = ttk.Entry(frame)
Mother_name_entry.grid(row=7, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Mother_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validator)


#row 9
Guardian_name = ttk.Label(frame, text="Guardian Name")
Guardian_name.grid(row=8, column=0, sticky=tk.W)

Guardian_name_entry = ttk.Entry(frame)
Guardian_name_entry.grid(row=8, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)

Guardian_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validator)


#row 10
Phone_1 = ttk.Label(frame, text="Phone 1")
Phone_1.grid(row=9, column=0, sticky=tk.W)

Phone_1_entry = ttk.Entry(frame)
Phone_1_entry.grid(row=9, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atleast_ten_digit_ensure(input):
    return input.isdigit() and len(input) <= 10 or input == ""

atleast_ten_digit_ensure_validate = (frame.register(atleast_ten_digit_ensure), "%P")

Phone_1_entry.configure(validate="key", validatecommand=atleast_ten_digit_ensure_validate)


Phone_2 = ttk.Label(frame, text="Phone 2")
Phone_2.grid(row=9, column=2, sticky=tk.W)

Phone_2_entry = ttk.Entry(frame)
Phone_2_entry.grid(row=9, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Phone_2_entry.configure(validate="key", validatecommand=atleast_ten_digit_ensure_validate)

#row 11
Hospital_ID = ttk.Label(frame, text="Hospital ID")
Hospital_ID.grid(row=10, column=0, sticky=tk.W)

Hospital_ID_entry = ttk.Entry(frame)
Hospital_ID_entry.grid(row=10, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)

def isdigit_ensure(input):
    return input.isdigit() or input == ""

isdigit_ensure_validate = (frame.register(isdigit_ensure), "%P")

Hospital_ID_entry.configure(validate="key", validatecommand=isdigit_ensure_validate)

#row 12
New_Password = ttk.Label(frame, text="New Password")
New_Password.grid(row=11, column=0, sticky=tk.W)

New_Password_entry = ttk.Entry(frame)
New_Password_entry.grid(row=11, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atmost_thirtychar_ensure(input):
    return len(input) <= 30 or input == ""

atmost_thirtychar_ensure_validate = (frame.register(atmost_thirtychar_ensure), "%P")

New_Password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)


Password = ttk.Label(frame, text="Confirm Password")
Password.grid(row=11, column=2, sticky=tk.W)

Password_entry = ttk.Entry(frame)
Password_entry.grid(row=11, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)

#validator function

def form_validator():

    popup = tk.Toplevel()
    # popup.geometry("200x100")
    popup.title("Error")

    label = tk.Label(popup, text="hello")
    label.pack(pady=10)


# Create a button to submit the form
btn = ttk.Button(frame, text="Submit",command=form_validator)
btn.grid(row=16, column=2, sticky=tk.W,pady= 30)

# Start the main loop
window.mainloop()