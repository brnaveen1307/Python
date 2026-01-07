def round_to_nearest(value, base):
    return round(value / base) * base

bill_amount = 247
rounded_bill = round_to_nearest(bill_amount, 5)

print("Original bill:", bill_amount)
print("Rounded bill:", rounded_bill)