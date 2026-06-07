import random

n = int(input("How many choices do you have?"))
L = [input(f"insert choice {i}")for i in range(n)]
print(f"I've decided, you should do {random.choice(L)}")
