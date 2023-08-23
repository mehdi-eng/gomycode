Question 1: Multiply Items in a List

def multiply_list_items(lst):
    result = 1
    for item in lst:
        result *= item
    return result

sample_list = [2, 3, 6]
result = multiply_list_items(sample_list)
print("Result:", result)  # Output: Result: 36
####################################################################

Question 2: Sort Tuples by Last Element

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sorted(sample_list, key=lambda x: x[-1])
print("Sorted List:", sorted_list)  
# Output: Sorted List: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
####################################################################

Question 3: Combine Dictionaries by Adding Values


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = {}
for key in set(d1.keys()) | set(d2.keys()):
    combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)

print("Combined Dictionary:", combined_dict)  
# Output: Combined Dictionary: {'a': 400, 'b': 400, 'c': 300, 'd': 400}
####################################################################

Question 4: Generate Dictionary of Squares


n = int(input("Enter a number: "))
squares_dict = {i: i*i for i in range(1, n+1)}
print("Dictionary of Squares:", squares_dict)
# Input: 8
# Output: Dictionary of Squares: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
####################################################################

Question 5: Sort Tuples by Float Element

tuple_list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_list = sorted(tuple_list, key=lambda x: float(x[1]), reverse=True)
print("Sorted Tuple List:", sorted_list)
# Output: Sorted Tuple List: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
####################################################################

Question 6: Set Operations

# Create a set
my_set = {0, 1, 2, 3, 4}

# Iterate over a set
print("Set Elements:")
for item in my_set:
    print(item)

# Add members to a set
my_set.add(5)
my_set.add(6)
print("Updated Set:", my_set)

# Remove items from a set
my_set.discard(2)
my_set.remove(4)
print("Updated Set:", my_set)
