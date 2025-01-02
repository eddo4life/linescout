import os

def count_lines_in_file(file_path):
    """
    Counts the number of lines in a given file.
    
    Args:
        file_path (str): The path to the file to count lines in.
        
    Returns:
        int: The number of lines in the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return 0

def count_files_and_lines_by_extension(directory, extension):
    """
    Counts the number of files with a specific extension and the total number of lines 
    across those files in a directory and its subdirectories.
    
    Args:
        directory (str): The path to the directory to scan.
        extension (str): The file extension to look for (e.g., '.txt').
        
    Returns:
        tuple: A tuple containing the total number of files and the total number of lines.
    """
    if not extension.startswith('.'):
        extension = '.' + extension  # Ensure the extension starts with a dot
    
    file_count = 0
    total_lines = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_count += 1
                file_path = os.path.join(root, file)
                total_lines += count_lines_in_file(file_path)
    
    return file_count, total_lines

# Usage
if __name__ == "__main__":
    dir_path = input("Enter the directory path: ").strip()
    file_extension = input("Enter the file extension (e.g., '.txt'): ").strip()
    
    try:
        file_count, total_lines = count_files_and_lines_by_extension(dir_path, file_extension)
        print(f"The number of '{file_extension}' files is: {file_count}")
        print(f"The total number of lines in those files is: {total_lines}")
    except Exception as e:
        print(f"An error occurred: {e}")
