from dictionary_table_formatter import format_data_from_dict_list
from file_utils import bytes_to_megabytes, get_file_size
import os

def generate_summary(directory, extension):
    """
    Generates a summary report of files with the given extension.
    Includes file size and line count details.
    """
    print(f"\n--- Summary Report for {extension} files in {directory} ---")
    
    total_size = 0
    file_details = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                size = get_file_size(file_path)
                total_size += size
                with open(file_path, 'r', encoding='utf-8') as f:
                    line_count = sum(1 for _ in f)
                file_details.append({
                    'file': file,
                    'size in bytes': size,
                    'size in megabytes':bytes_to_megabytes(size),
                    'lines': line_count
                })
                
    
    # Output the file details
    format_data_from_dict_list(file_details)
    
    print(f"\nTotal size of all files: {total_size} bytes -> {bytes_to_megabytes(total_size)} megabytes")
