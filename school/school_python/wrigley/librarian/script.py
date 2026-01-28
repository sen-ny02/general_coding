with open("books.txt", "r") as fuck_this_shit:
    for line in fuck_this_shit:
        line = line.strip()

        if not line:
            continue

        parts = line.split(",")

        if len(parts) != 3:
            print("Invalid line: ", line)
            continue

        title, author, isbn = parts
        print(title, author, isbn)

print(title)
print()
print(author)
print()
print(isbn)
