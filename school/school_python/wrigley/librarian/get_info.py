
def get_info():
    with open("books.txt", "r") as f:
        #removes unnecesary shit
        for line in f:
            line = line.strip()

            #skips if no line so no dumbass error
            if not line:
                continue

            #splits parts with the comma as splitter
            parts = line.split(",")

            #ez error handling
            if len(parts) != 3:
                print("Invalid line: ", line)
                continue

            #assigns parts to shit
            title, author, isbn = parts