numbers = [1, 2, 4, 5]

n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print("Missing number:", missing)