def copy_file(command: str) -> None:

    if "cp" not in command:
        return

    words = command.split()

    if len(words) != 3:
        return

    command = words[0]
    source = words[1]
    destination = words[2]

    if source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
