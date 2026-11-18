word=input("Enter a string: ")
freq={}
for char in word:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print("Character Frequency:", freq)