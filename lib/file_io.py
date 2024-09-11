

def write_file(file_name, file_content):
    """Writes content to a .txt file, overwriting if file exists."""
    with open(file_name + ".txt", 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Appends content to a .txt file, creating it if it does not exist."""
    with open(file_name + ".txt", 'a') as file:
        file.write(append_content + "\n")

def read_file(file_name):
    """Reads content from a .txt file and returns it."""
    with open(file_name + ".txt", 'r') as file:
        return file.read()
