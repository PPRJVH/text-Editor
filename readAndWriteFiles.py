def file_read(path = "store.txt"):
    with open(path, "r") as f:
        li = f.readlines()
    return li


def file_write(list_data,path = "store.txt"):
    with open(path, 'w') as file:
        file.writelines(list_data)

# If we execute this readAndWrite file then the value of the __name__ will be __main__ itself. So, it satisfies the if condition and then prints the statement in the if
# If we execute the betterVersion file then the value of the --name-- will be readAndWrite (value of the file name). So, if condition doesnt satisfies.


if __name__ == "__main__":
    print("Hi Hello")