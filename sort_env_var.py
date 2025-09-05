import os

# Get the environment variable 'a'
env_var_a = os.environ.get('a')

# Convert the string representation of the list to an actual list
# Assuming the format is like a=[18,12,20,100,99,1,5,8]
list_a = eval(env_var_a)

# Sort the list in ascending order
sorted_list_a = sorted(list_a)

# Print the sorted list
print(sorted_list_a)