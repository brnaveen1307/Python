# Set Operations

s = {1, 2, 3, 4}

s.add(5)
print(s)

s.update([6, 7])
print(s)

s.remove(2)
print(s)

s.discard(10) # Safer than remove
print(s)

popped = s.pop()
print(s)

copy_s = s.copy()
print(s)

print("Set Operations: ", copy_s)