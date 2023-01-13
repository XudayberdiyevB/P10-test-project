def write_exceptions(error):
    with open("exceptions.txt", "a") as f:
        f.write(f"{error}\n")
