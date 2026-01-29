'''

1. File Input: Automatically read book data from a text file named books.txt upon startup - done

2. Object Storage: Store the data as Book objects in a list/array (not just strings).

3. Search: Allow the user to find a book by entering its title.

4. State Change: Allow a user to "check out" a book, changing its status from "Available" to "Checked Out".

'''


#find num of lines dickead
with open("books.txt", 'r') as fp:
    sum_lines = sum(1 for line in fp)
    # print('Total Number of lines:', sum_lines)

#iterates through each line - testing phase
for idx in range(sum_lines): 
    printline = idx
    lineCounter = 0
    with open('books.txt','r') as f:
        for line in f:
            lineCounter += 1
            if lineCounter == printline:
                print(line, end='')
