num1=[10,10,20,30,40,50]
seen=[]
duplicates=[]
for num in num1:
    if num not in seen:
        seen.append(num)
    else:
        if num not in duplicates:
            duplicates.append(num)
print("Duplicate numbers:", duplicates)