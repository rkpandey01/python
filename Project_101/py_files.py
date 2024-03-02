f = open('Sample.txt', 'r')

txt = f.read()
print(txt)
f.close()

# Create a list of strings
lines = ["This is line 1.\n", "This is line 2.\n", "This is line 3.\n"]

# Open the file in write mode
with open("file.txt", "w") as file:
    # Write the list of strings to the file
    file.writelines(lines)

# Read the file content to verify
with open("file.txt", "r") as file:
    file_content = file.read()

# Print the content
print(file_content)
