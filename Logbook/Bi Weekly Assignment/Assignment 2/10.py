'''
10.Create three dictionaries:
a = {'x': 5, 'y': 10}
b = {'z': 15, 'w': 20}
c = {'p': 25, 'q': 30}

Perform the following tasks:
(a) Merge all dictionaries into a single one.
(b) Add a new pair 'r': 35.
(c) Double all the values in the resulting dictionary.
(d) Delete the key 'y'.
(e) Compute and print the average value of all remaining items.
'''

# Given dictionaries
a = {'x': 5, 'y': 10}
b = {'z': 15, 'w': 20}
c = {'p': 25, 'q': 30}

# (a) Merge all dictionaries into one
merged = {}
merged.update(a)
merged.update(b)
merged.update(c)

# (b) Add a new key-value pair 'r': 35
merged['r'] = 35

# (c) Double all the values in the dictionary
for key in merged:
    merged[key] = merged[key] * 2

# (d) Delete the key 'y'
del merged['y']

# (e) Compute and print the average of remaining values
total = 0
count = 0

for value in merged.values():
    total = total + value
    count = count + 1

average = total / count

# Display results
print("Final dictionary:", merged)
print("Average value:", average)
