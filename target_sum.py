numbers = list(map(int, input("Enter numbers: ").split()))
num=int(input("Enter the target sum: "))
seen=set()
for number in numbers:
    required=num-number
    if required in seen:
        print("Pair found:", (number, required))
seen.add(number)