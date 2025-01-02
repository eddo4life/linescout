import os

def count_files_by_extension(directory, extension):
    """
    Counts the number of files with a specific extension in a directory and its subdirectories.
    
    Args:
        directory (str): The path to the directory to scan.
        extension (str): The file extension to look for (e.g., '.txt').
        
    Returns:
        int: The total number of files with the specified extension.
    """
    if not extension.startswith('.'):
        extension = '.' + extension  # Ensure the extension starts with a dot
    
    file_count = 0
    
    for root, _, files in os.walk(directory):
        file_count += sum(1 for file in files if file.endswith(extension))
    
    return file_count

# Usage
if __name__ == "__main__":
    dir_path = input("Enter the directory path: ").strip()
    file_extension = input("Enter the file extension (e.g., '.txt'): ").strip()
    
    try:
        count = count_files_by_extension(dir_path, file_extension)
        print(f"The number of files with extension '{file_extension}' is: {count}")
    except Exception as e:
        print(f"An error occurred: {e}")
