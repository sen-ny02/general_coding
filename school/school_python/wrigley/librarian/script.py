'''
Success criteria:
1. File Input: Automatically read book data from a text file named books.txt upon startup.

2. Object Storage: Store the data as Book objects in a list/array (not just strings).

3. Search: Allow the user to find a book by entering its title.

4. State Change: Allow a user to "check out" a book, changing its status from "Available" to "Checked Out".
'''

file = open("books.txt", "r")
lines = file.readline()
lines = lines.strip()
print(lines)

for line in file:
    print(lines)