#Real World Exception Example

class PaymentError(Exception):
    """Custom exception for payment related errors."""
    def __init__(self, message="Payment failed"):
        self.message = message
        super().__init__(self.message)

def process_payment(card_number, amount):
    # Simulating a real payment gateway scenario
    if len(str(card_number)) != 16:
        raise PaymentError("Invalid card number. Must be 16 digits.")
    if amount <= 0:
        raise PaymentError("Invalid payment amount.")
    if card_number == 1111222233334444:
        raise PaymentError("Card declined by the bank.")

    print(f"✅ Payment of ₹{amount} was successful!")

def checkout():
    try:
        card_number = int(input("Enter your 16-digit card number: "))
        amount = float(input("Enter the amount to pay: ₹"))
        process_payment(card_number, amount)
    except PaymentError as pe:
        print(f"❌ Payment Error: {pe}")
        # Real world: Log the error or alert the user to try again
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e}")
    else:
        print("🎉 Order placed successfully!")
    finally:
        print("📝 Transaction attempt finished.")

checkout()
