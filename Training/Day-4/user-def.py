
class InvalidAgeException(Exception): 
    pass

try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Eligible to vote")
    else:
        raise InvalidAgeException("Invalid age")
    
except InvalidAgeException as e:
    print("Exception occurred: ", e)