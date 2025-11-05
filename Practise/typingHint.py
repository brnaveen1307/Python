from typing import List, Dict

# Function to calculate total price of items in an order
def calculate_total(order_items: List[Dict[str, float]]) -> float:
    """
    Each item in order_items is a dictionary like:
    {"name": "Laptop", "price": 50000.0}
    """
    total = sum(item["price"] for item in order_items)
    return total


# Function to apply discount
def apply_discount(total: float, discount: float) -> float:
    """Apply a percentage discount to the total amount."""
    discounted_total = total - (total * discount / 100)
    return discounted_total


# Function to print the final order summary
def print_order_summary(customer_name: str, items: List[Dict[str, float]]) -> None:
    total = calculate_total(items)
    discounted_total = apply_discount(total, 10.0)
    print(f"Customer: {customer_name}")
    print(f"Total before discount: ₹{total:.2f}")
    print(f"Total after discount: ₹{discounted_total:.2f}")


# Example usage
order = [
    {"name": "Laptop", "price": 50000.0},
    {"name": "Mouse", "price": 1500.0},
    {"name": "Keyboard", "price": 2500.0}
]

print_order_summary("Naveen Kumar", order)
