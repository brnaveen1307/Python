# Expense Tracker using File Handling

def add_expense(amount, category, description):
    """Add a new expense to the file."""
    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category},{description}\n")
    print("✅ Expense added successfully!")


def view_expenses():
    """Read and display all expenses from the file."""
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("📂 No expenses recorded yet.")
                return
            
            print("\n📊 Your Expenses:\n-------------------")
            total = 0
            for line in lines:
                amount, category, description = line.strip().split(",")
                print(f"💰 ₹{amount} | Category: {category} | Note: {description}")
                total += float(amount)
            print("-------------------")
            print(f"Total Spent: ₹{total}")
    except FileNotFoundError:
        print("⚠️ No expense file found. Add an expense first.")


# Example usage
add_expense(250, "Food", "Lunch with friends")
add_expense(100, "Transport", "Auto fare")
view_expenses()
