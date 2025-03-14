import os


def copy_file(command : str) -> None:
    if command is None or "cp" not in command:
        print('Command empty or not "cp". Returning...')
        return
    else:
        word_list = command.split(" ")
    try:
        source_file = word_list[1]
        dest_file = word_list[2]
    except IndexError:
        print("Sorry, input is not valid!")
        return
    if os.path.exists(source_file) and source_file != dest_file:
        with open(source_file, "r") as source, open(dest_file, "w") as dest:
            for line in source.readlines():
                dest.writelines(line)
    else:
        print("Error! Invalid input files.")
