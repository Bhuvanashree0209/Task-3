import os
from datetime import datetime

def create_file_with_timestamp():
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Generate the file name with the timestamp
    file_name = f"timestamp_{timestamp}.txt"
    
    # Content of the file
    file_content = f"Timestamp: {timestamp}"
    
    # Write content to the file
    with open(file_name, 'w') as file:
        file.write(file_content)
    
    print(f"File '{file_name}' created with content:\n{file_content}")

# Call the function to create the file
create_file_with_timestamp()
