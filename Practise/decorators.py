import datetime
from functools import wraps

# Decorator for logging user access
def log_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get("user", "Guest")
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{time}] User '{user}' accessed {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper


# Example functions (as if in a web app)
@log_access
def view_profile(user):
    print(f"Displaying profile for {user}")

@log_access
def view_dashboard(user):
    print(f"Welcome to {user}'s dashboard!")


# Simulating function calls
view_profile(user="Naveen")
view_dashboard(user="Naveen")
