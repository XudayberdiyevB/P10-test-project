from exceptions import write_exceptions


def count_author(filepath, author_name):
    counter = 0
    try:
        with open(filepath, "r") as file:
            data = file.readlines()
    except FileNotFoundError as e:
        write_exceptions(e)
    else:
        for line in data:
            for d in line.split(","):
                if d.strip() == author_name:
                    counter += 1
    return counter


print(count_author("Book123.txt", "AA"))
