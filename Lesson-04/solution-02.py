# Value input from the keyboard
print("Please enter the data:")
value = str(input())

# Check if the element is palindrome or not
if value == value[::-1]:
    print("Yes")
else:
    print("No")
