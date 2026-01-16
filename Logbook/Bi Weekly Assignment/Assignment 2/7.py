'''
7.Write a program that takes a list of city names and displays:
The total number of cities entered,
The number of cities that start with the letter "K",
The list of all cities in alphabetical order
'''

# Take city names as input
cities = input("Enter city names separated by commas: ").split(",")

# Remove extra spaces
for i in range(len(cities)):
    cities[i] = cities[i].strip()

# Total number of cities
total_cities = len(cities)

# Count cities starting with 'K'
count_k = 0
for city in cities:
    if city[0] == "K":
        count_k = count_k + 1

# Sort cities alphabetically
cities.sort()

# Display results
print("Total number of cities:", total_cities)
print("Number of cities starting with 'K':", count_k)
print("Cities in alphabetical order:", cities)
