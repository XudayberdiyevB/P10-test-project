# [BookNo, Book_Name, Author, Price]

def create_file(filepath, data):
    with open(filepath, "w") as file:
        file.write(data)


book_data = """123, A, AA, 1000
126, D, AA, 1004
124, B, BB, 1001
125, C, CC, 1002
"""

create_file("Book.txt", book_data)


