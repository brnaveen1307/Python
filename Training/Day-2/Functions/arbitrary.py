print("Function with arbitrary arguments")

def add(*num):
    for i in num:
        print(i)

add(10, 20, 30)