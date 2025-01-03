import os
from tqdm import tqdm

def count_files_and_lines_by_extension(directory, extension):
    """
    Counts the number of files with a specific extension and sums up the total lines in those files.
    """
    if not extension.startswith('.'):
        extension = '.' + extension  # Ensure the extension starts with a dot
    
    file_count = 0
    total_lines = 0
    
    for root, _, files in tqdm(os.walk(directory), desc="Scanning directories"):
        for file in files:
            if file.endswith(extension):
                file_count += 1
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        total_lines += sum(1 for _ in f)
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    return file_count, total_lines

def get_file_size(file_path):
    """
    Returns the size of the file in bytes.
    """
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        print(f"Error getting file size for {file_path}: {e}")
        return 0
    
def format_size(bytes_value):
    """
    Converts a size in bytes to an appropriate human-readable format.
    """
    if bytes_value < 1024:
        return f"{bytes_value}B"
    elif bytes_value < 1024**2:
        return f"{bytes_value / 1024:.2f}KB"
    elif bytes_value < 1024**3:
        return f"{bytes_value / 1024**2:.2f}MB"
    else:
        return f"{bytes_value / 1024**3:.2f}GB"

