def is_palindrome(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return text == reversed_text


user_text = input("Enter text: ")

if is_palindrome(user_text):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")