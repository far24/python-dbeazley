# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid part 1', total_paid)


# Exercise 1.8: Extra payments
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment = 1000
month = 0

print('Month', 'Total paid')
while principal > 0:
    if month <= 12:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    month = month +1

    print(f'{month:0>3d} {total_paid:0.2f}')
