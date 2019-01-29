from Utils.find import find_in

def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()  # Returns the entire file contents as a string with \n. To remove, use strip()

print(__name__)