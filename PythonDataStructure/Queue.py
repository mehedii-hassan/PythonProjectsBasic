from collections import deque

bank = deque(["mehedi", "mow", "mayan"])
print(bank)
bank.popleft()
bank.popleft()
print(bank)
bank.popleft()
if not bank:
    print("No person left")
