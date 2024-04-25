def read_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the content of the file
            file_content = file.read()
            # Display the content in the console
            print("Content of the file:")
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Example usage: Read from a text file named 'example.txt'
read_file('example.txt')
