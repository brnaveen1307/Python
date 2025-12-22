def calculate_tax(income, slabs):
    tax = 0
    for lower, upper, rate in slabs:
        if income > lower:
            taxable_amount = min(income, upper) - lower
            tax += taxable_amount * rate
        else:
            break
    return tax


income = 950000

slabs = [
    (0, 250000, 0.00),
    (250000, 500000, 0.05),
    (500000, 1000000, 0.20)
]

tax = calculate_tax(income, slabs)
print(f"Total Tax Payable: ₹{tax}")
