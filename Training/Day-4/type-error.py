a = 10

try:
    # a = a + "python" => This does not work
    a += 10
    print(a)
except TypeError as e:
    print("Value e: ", e)
 