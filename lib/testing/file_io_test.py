import os
import tempfile
from lib.file_io import write_file, append_file, read_file

def test_write_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_name = temp_file.name
    file_name = os.path.splitext(file_name)[0]
    file_content = "This is a test content."
    write_file(file_name, file_content)
    with open(file_name + ".txt", 'r') as f:
        file_content_read = f.read()
    assert file_content_read == file_content
    os.remove(file_name + ".txt")

def test_append_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_name = temp_file.name
    file_name = os.path.splitext(file_name)[0]
    file_content = "This is a test content."
    append_content = "\nAppended content."
    write_file(file_name, file_content)
    append_file(file_name, append_content)
    with open(file_name + ".txt", 'r') as f:
        file_content_read = f.read()
    assert file_content_read == file_content + append_content
    os.remove(file_name + ".txt")

def test_read_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_name = temp_file.name
    file_name = os.path.splitext(file_name)[0]
    file_content = "This is a test content."
    write_file(file_name, file_content)
    file_content_read = read_file(file_name)
    assert file_content_read == file_content
    os.remove(file_name + ".txt")
