def convert_currency(amount, rate):
    return amount * rate

usd_price = 250
usd_to_inr_rate = 83.20

price_in_inr = convert_currency(usd_price, usd_to_inr_rate)

print(f"The price in INR is ₹{price_in_inr}")
