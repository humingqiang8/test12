import os

# Get the environment variable 'a' and evaluate it as a Python list
a_str = os.environ.get('a', '[]')
a_list = eval(a_str)

# Sort the list in descending order
sorted_list = sorted(a_list, reverse=True)

# Print the sorted list
print(sorted_list)