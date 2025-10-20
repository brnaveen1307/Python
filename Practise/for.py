import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Sample client data (usually fetched from a database)
clients = [
    {"name": "Alice", "email": "alice@example.com", "due_amount": 1200, "due_date": "2025-10-15"},
    {"name": "Bob", "email": "bob@example.com", "due_amount": 800, "due_date": "2025-10-18"},
    {"name": "Charlie", "email": "charlie@example.com", "due_amount": 500, "due_date": "2025-10-10"},
]

# Loop through each client and send reminder
for client in clients:
    # Check if payment is overdue
    due_date = datetime.strptime(client["due_date"], "%Y-%m-%d")
    if due_date < datetime.now():
        subject = f"Payment Reminder - Invoice Due"
        message = (
            f"Dear {client['name']},\n\n"
            f"This is a friendly reminder that your payment of ₹{client['due_amount']} "
            f"was due on {client['due_date']}. Please make the payment at your earliest convenience.\n\n"
            "Thank you,\nAccounts Team"
        )

        # Create email
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = "accounts@company.com"
        msg['To'] = client["email"]

        # (Example only — replace with actual mail server)
        print(f"📧 Sending email to {client['email']}...")
        # with smtplib.SMTP('smtp.yourserver.com', 587) as server:
        #     server.login("your_username", "your_password")
        #     server.send_message(msg)

print("✅ All overdue invoice reminders processed.")
