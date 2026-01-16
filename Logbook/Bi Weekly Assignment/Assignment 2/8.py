'''
8.Write a function named merge_student_scores that takes two dictionaries:
student_names = {1: 'Anish', 2: 'Priya', 3: 'Sujan'}
student_scores = {1: 88, 2: 92, 3: 79}
and returns a new dictionary combining both, in the format:
{'Anish': 88, 'Priya': 92, 'Sujan': 79}
'''

def merge_student_scores(student_names, student_scores):
    merged = {}

    for key in student_names:
        name = student_names[key]
        score = student_scores[key]
        merged[name] = score

    return merged


# Given dictionaries
student_names = {1: 'Anish', 2: 'Priya', 3: 'Sujan'}
student_scores = {1: 88, 2: 92, 3: 79}

# Function call
result = merge_student_scores(student_names, student_scores)

print(result)
