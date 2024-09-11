

def write_file(file_name, file_content):
   
    with open(file_name + ".txt", 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    
    with open(file_name + ".txt", 'a') as file:
        file.write(append_content + "\n")

def read_file(file_name):
    
    with open(file_name + ".txt", 'r') as file:
        return file.read()
