import os
import shutil

def sort_files_by_type(directory):
    # Get the list of files in the directory
    files = os.listdir(directory)
    
    # Create a dictionary to store the file types as keys and corresponding file paths as values
    file_types = {}
    
    # Iterate over each file
    for file in files:
        # Ignore directories
        if os.path.isdir(os.path.join(directory, file)):
            continue
        
        # Extract the file extension
        file_extension = os.path.splitext(file)[1]
        
        # Add the file to the dictionary based on its extension
        if file_extension in file_types:
            file_types[file_extension].append(file)
        else:
            file_types[file_extension] = [file]
    
    # Create a subdirectory for each file type and move the files into their respective subdirectories
    for file_extension, files in file_types.items():
        type_directory = os.path.join(directory, file_extension[1:].upper() + "_Files")
        
        # Create the subdirectory if it doesn't exist
        if not os.path.exists(type_directory):
            os.makedirs(type_directory)
        
        # Move each file to its respective subdirectory
        for file in files:
            src_path = os.path.join(directory, file)
            dest_path = os.path.join(type_directory, file)
            shutil.move(src_path, dest_path)
    
    print("Files sorted by type successfully.")

# Example usage:
directory_path = "/path/to/your/directory"
sort_files_by_type(directory_path)
