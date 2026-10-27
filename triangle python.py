#Electricity Billing System
def calculate_bill(units):
    bill=0
    if units<=100:
        bill= units * 1.50
    elif units<=200:
        bill=100*1.50+(units-100)*2.50
