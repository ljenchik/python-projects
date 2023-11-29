file_name = "words.txt"
def count(file):
    try:
        with open(file, 'r') as file:
            content = file.read()
            word_count = len(content.split(' '))
            return word_count
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied. Unable to access '{file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print(count(file_name))
