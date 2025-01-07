import mimetypes
import os
from tqdm import tqdm

from utils import print_error

def count_files_and_lines_by_extension(directory, extension):
    """
    Counts the number of files with a specific extension and sums up the total lines in those files.
    """
    if not extension.startswith('.'):
        extension = '.' + extension  # Ensure the extension starts with a dot
    
    file_count = 0
    total_lines = 0
    
    for root, _, files in tqdm(os.walk(directory), desc="\033[93mScanning directories \033[0m"):
        for file in files:
            if file.endswith(extension):
                file_count += 1
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        total_lines += sum(1 for _ in f)
                except Exception as e:
                    print_error(f"\nError reading file {file_path}: {e}")
    
    return file_count, total_lines

def get_file_size(file_path):
    """
    Returns the size of the file in bytes.
    """
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        print_error(f"Error getting file size for {file_path}: {e}")
        return 0
    
def is_text_file(file_path):
    """
    Determines if a file is a text-based file.
    """
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith("text")
    
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

