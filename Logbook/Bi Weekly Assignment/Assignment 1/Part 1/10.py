'''
10.The Unicode characters corresponding to these codes: 80, 121, 116, 104, 111, 110.
'''

# List of Unicode codes
codes = [80, 121, 116, 104, 111, 110]

# Convert each code to its corresponding character
chars = [chr(c) for c in codes]
result = chars

# Display the result
print("Unicode characters:", result)

# Combine the characters into a string
d = ''.join(chars)
print("Joined Unicode characters:", d)