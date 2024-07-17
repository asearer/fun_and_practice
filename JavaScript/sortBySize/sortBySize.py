import os

def sort_files_by_size(directory):
    # Get the list of files in the directory
    files = os.listdir(directory)
    
    # Create a list to store tuples of (file, size)
    file_sizes = []
    
    # Iterate over each file
    for file in files:
        # Ignore directories
        if os.path.isdir(os.path.join(directory, file)):
            continue
        
        # Get the file size
        file_path = os.path.join(directory, file)
        size = os.path.getsize(file_path)
        
        # Add the file and its size to the list
        file_sizes.append((file, size))
    
    # Sort the files by size in descending order
    file_sizes.sort(key=lambda x: x[1], reverse=True)
    
    # Print the sorted files
    for file, size in file_sizes:
        print(f"{file} - {size} bytes")

# Example usage:
directory_path = "/path/to/your/directory"
sort_files_by_size(directory_path)
