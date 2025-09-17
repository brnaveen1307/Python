def second_largest():
    numbers = [10, 100, 20, 80, 90, 50]
    unique = list(set(numbers))
    unique.sort()
    print("Second Largest: ", unique[-2])

second_largest()