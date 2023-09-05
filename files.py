# 1. Read an entire text file
file_name = "example.txt"
with open(file_name, "r") as f:
    content = f.read()
    print("1. Reading the entire text file:")
    print(content)

# 2. Read the first n lines of a file
n = 5  # Number of lines to read
with open(file_name, "r") as f:
    print("\n2. Reading the first", n, "lines of the file:")
    for i in range(n):
        line = f.readline()
        if not line:
            break
        print(line, end="")

# 3. Read the last n lines of a file
n = 5  # Number of lines to read from the end
with open(file_name, "r") as f:
    lines = f.readlines()
    last_n_lines = lines[-n:]
    print("\n\n3. Reading the last", n, "lines of the file:")
    for line in last_n_lines:
        print(line, end="")

# 4. Count the number of words in a text file
with open(file_name, "r") as f:
    text = f.read()
    words = text.split()
    word_count = len(words)
    print("\n\n4. Counting the number of words in the file:")
    print("Number of words:", word_count)

# 5. (Bonus) Read the last n lines of a file (without reading the entire file)
n = 5  # Number of lines to read from the end
with open(file_name, "r") as f:
    lines = f.readlines()
    last_n_lines = lines[-n:]
    print("\n\n5. (Bonus) Reading the last", n, "lines of the file (without reading the entire file):")
    for line in last_n_lines:
        print(line, end="")
