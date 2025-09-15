amount = int(input("Enter the amount in rupees: "))

notes_200 = amount // 2000
amount = amount % 2000

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_20 = amount // 20
amount = amount % 20

notes_10 = amount // 10
amount = amount % 10

coins_5 = amount // 5
amount = amount % 5

coins_2 = amount // 2
amount = amount % 2

coins_1 = amount // 1
amount = amount % 1

print("2000 rupee notes:", notes_200)
print("500 rupee notes:", notes_500)
print("200 rupee notes:", notes_200)
print("100 rupee notes:", notes_100)
print("50 rupee notes:", notes_50)
print("20 rupee notes:", notes_20)
print("10 rupee notes:", notes_10)
print("5 rupee coins:", coins_5)
print("2 rupee coins:", coins_2)
print("1 rupee coins:", coins_1)