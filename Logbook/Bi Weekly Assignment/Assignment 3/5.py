'''
5.Develop a program that reads a text file and displays the most frequently occurring word
along with its number of occurrences.
'''

# Program to find the most frequent word in a text file

filename = input("Enter the filename: ")

try:
    file = open(filename, "r")
    text = file.read()
    file.close()

    words = text.split()   # Split text into words
    freq = {}              # Dictionary to store word count

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    most_word = ""
    max_count = 0

    for word in freq:
        if freq[word] > max_count:
            max_count = freq[word]
            most_word = word

    print("Most frequent word:", most_word)
    print("Number of occurrences:", max_count)

except:
    print("File not found!")
