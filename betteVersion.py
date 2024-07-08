from readAndWriteFiles import file_read,file_write
# import readAndWriteFiles
# If we keep like this then the functions belons to readAndWriteFiles file (file_read,file_write) should call as readAndWriteFiles.file_read
import time
t = time.strftime("%b %d, %Y %H:%M:%S")
print(t)
filePath = "store.txt"
i = 0
while True:
    a = input("Enter the case: add,show,edit,delete,exit:")
    a = a.strip()  # removes white spaces

    if a.startswith("add"):
        list = file_read()
        b = a[4:] + "\n"

        """"
        file = open("store.txt","r")
        list = file.readlines()
        file.close()
        """
        # In a better way we can write the files by using context-manager
        list.append(b)
        """"
        file = open("store.txt","w")
        file.writelines(list)
        file.close()
        """
        file_write(list)
        print(f"Successfully added {b}")


    elif a.startswith("show"):
        """
        i=0
        while i<len(list):
            print(list[i])
            i=i+1
            """
        list = file_read()

        new_list = []
        for i in list:
            new_item = i.strip("\n")
            new_list.append(new_item)
        print(list)
        for i, item in enumerate(list):
            item = item.title()
            """"
            item = item.upper()
            item = item.lower()
            """
            # print(i, item)

            item = item.strip('\n')
            print(f"{i}){item}")

    elif a.startswith("edit"):

        try:
            list = file_read()

            num = int(a[5:])

            if num > i:
                print("Enter the valid index")
                continue
            elem = input("enter the edited value:") + "\n"
            em = list[num]
            list[num] = elem

            file_write(list)

            ed = f"Successfully edited from {em} to {elem}"
            print(ed)

        except ValueError:
            print("Entered command is Invalid")
            continue

    elif a.startswith("delete"):
        try:
            list = file_read()
            num = int(a[7:])
            remove = list[num]
            list.pop(num)

            file_write(list)
            print("Successfully removed the ", remove, "data")
        except IndexError:
            print("Entered command is Invalid")
            continue
        except ValueError:
            print("Enter the index value")
            continue
    elif a.startswith("exit"):
        break
    else:
        print("re-enter")
