class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # the iterator object itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Using the iterator
for num in Countdown(5):
    print(num)
