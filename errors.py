# Code 1: Index Error
mylist = [14, "hello", 967]
# Attempting to access an index that doesn't exist
# The list has three elements, so valid indices are 0, 1, and 2
# Index 6 is out of range
# Error: IndexError: list index out of range
# Corrected code: Access a valid index (0, 1, or 2)

# Code 2: Import Error
import Pandas
import NumPy
# Attempting to import non-existent modules
# There is no module named "Pandas" or "NumPy" (case-sensitive)
# Error: ImportError: No module named Pandas
# Corrected code: Import correct module names, 'pandas' and 'numpy'.

# Code 3: Syntax Error
Print"python errors"
# Incorrect capitalization of the 'print' statement
# 'Print' should be 'print' (all lowercase)
# Error: SyntaxError: invalid syntax
# Corrected code: 'print("python errors")'

# Code 4: Key Error
mydictionary = {True: "hello", False: "bye", '3': "python"}
mydictionary['True']
# Attempting to access a key ('True') as a string while it's stored as a boolean (True)
# Keys are case-sensitive; 'True' and True are different keys
# Error: KeyError: 'True'
# Corrected code: Access the key as 'True' (without quotes) or use the boolean key (True).

# Code 5: Indentation Error
i = 14
while i < 78:
print(i)
i += 1
# Missing indentation within the while loop
# Indentation is required in Python to define a block of code
# Error: IndentationError: expected an indented block
# Corrected code: Indent the 'print' statement and 'i += 1' line inside the while loop.

# Code 6: Stop Iteration Error
it = iter([1, 2, 3])
next(it)
next(it)
next(it)
next(it)
# Attempting to call 'next' beyond the iterator's length
# 'next' raises StopIteration when there are no more items to iterate
# Error: StopIteration
# Corrected code: Use 'try' and 'except' to handle StopIteration or iterate only up to the available items.

# Code 7: Type Error
'15' + 15
# Attempting to concatenate a string ('15') and an integer (15)
# The '+' operator between different data types is not allowed
# Error: TypeError: cannot concatenate 'str' and 'int' objects
# Corrected code: Convert one of them to the same data type (e.g., '15' + str(15))

# Code 8: Value Error
int('python')
# Attempting to convert a non-integer string ('python') to an integer
# 'int' can only convert valid integer strings
# Error: ValueError: invalid literal for int() with base 10: 'python'
# Corrected code: Provide a valid integer string for conversion (e.g., '123')

# Code 9: Name Error
python
# Attempting to use the variable 'python' which is not defined
# Variables need to be defined before use
# Error: NameError: name 'python' is not defined
# Corrected code: Define the variable 'python' with a value.

# Code 10: Zero Division Error
x = 19 / 0
# Attempting to divide by zero
# Division by zero is not allowed in mathematics
# Error: ZeroDivisionError: division by zero
# Corrected code: Avoid division by zero, ensure the denominator is not zero.
