# sears.py
# Exercise 1.6

# Lear to read traceback messages
#----------------------------------------
# Traceback (most recent call last):
#  File "sears.py", line 10, in <module>
#    day = days + 1
# NameError: name 'days' is not defined


bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)


# Answer this:
#-----------------------------------------
# Which line is the error?
# What is the error?
# Fix the error
# Run the program successfully