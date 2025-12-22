def calculate_gst(amount, rate):
    gst = amount * (rate / 100)
    return gst

# Real-world usage
base_price = 18000
gst_rate = 18

gst_amount = calculate_gst(base_price, gst_rate)
final_price = base_price + gst_amount

print("Base Price: ₹", base_price)
print("GST Amount: ₹", gst_amount)
print("Total Payable Amount: ₹", final_price)
