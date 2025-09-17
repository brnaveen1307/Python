square = lambda x: x * x
print(square(4))

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(7))

def double_def(x):
    return x * 2

print("Normal function result: ", double_def(5))