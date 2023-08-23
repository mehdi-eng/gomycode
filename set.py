#Question 1: Multiply All Items in a List


def multiply_list_items(lst):
    result = 1
    for item in lst:
        result *= item
    return result

sample_list = [2, 3, 6]
result = multiply_list_items(sample_list)
print("Result:", result)
###############################################################
#Question 2: Sort List of Tuples by Last Element


def sort_tuples_by_last_element(lst):
    return sorted(lst, key=lambda x: x[-1])

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort_tuples_by_last_element(sample_list)
print("Sorted List:", sorted_list)
##############################################################
#Question 3: Combine Dictionaries by Adding Values for Common Keys


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = {}
for key in d1.keys() | d2.keys():
    result[key] = d1.get(key, 0) + d2.get(key, 0)

print("Combined Dictionary:", result)
##############################################################
#Question 4: Generate a Dictionary of Squares

n = int(input("Enter a number: "))
result_dict = {i: i*i for i in range(1, n+1)}
print("Result:", result_dict)
##############################################################
#Question 5: Sort a Tuple by its Float Element


def sort_tuple_by_float_element(lst):
    return sorted(lst, key=lambda x: float(x[1]), reverse=True)

sample_list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_list = sort_tuple_by_float_element(sample_list)
print("Sorted List:", sorted_list)
##############################################################
#Question 6: Create, Iterate Over, Add, and Remove from a Set


# Create a set
my_set = {0, 1, 2, 3, 4}
print("Initial Set:", my_set)

# Iterate over a set
print("Iterating Over Set:")
for item in my_set:
    print(item)

# Add members to a set
my_set.add(5)
my_set.add(6)
print("After Adding:", my_set)

# Remove items from a set
my_set.discard(2)
my_set.remove(3)
print("After Removing:", my_set)
