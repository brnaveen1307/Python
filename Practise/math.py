import math
import random
import statistics

# 🎲 Step 1: Simulate dice rolls for 100 players
players_scores = []

for _ in range(100):
    rolls = [random.randint(1, 6) for _ in range(10)]  # 10 dice rolls per player
    score = sum(rolls)
    
    # 🧮 Step 2: Apply a math-based bonus system
    # Bonus = square root of (score * random multiplier)
    bonus = math.sqrt(score * random.uniform(1.1, 2.0))
    
    total_score = score + bonus
    players_scores.append(total_score)

# 📊 Step 3: Statistical analysis of all players’ performance
average = statistics.mean(players_scores)
median = statistics.median(players_scores)
std_dev = statistics.stdev(players_scores)

# 📈 Display results
print(f"Average Score: {average:.2f}")
print(f"Median Score: {median:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")

# 🎯 Identify top performer
best_score = max(players_scores)
print(f"Top Player Score: {best_score:.2f}")
