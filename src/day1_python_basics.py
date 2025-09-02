# src/day1_python_basics.py
user_name = "Rena"
scores = [88, 92, 76]

def average(nums: list[float]) -> float:
    if not nums:
        return 0.0
    return sum(nums) / len(nums)

scores.append(95)
passed = [s for s in scores if s >= 80]

if __name__ == "__main__":
    print(f"Hello, {user_name}!")
    print("scores:", scores)
    print("avg:", round(average(scores), 2))
    print("passed:", passed)
