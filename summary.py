from tqdm import tqdm
from dictionary_table_formatter import format_data_with_tabulate, format_data_from_dict_list_with_tabulate
from file_utils import format_size, get_file_size, is_text_file
import os

from utils import print_error, print_success

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
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        line_count = sum(1 for _ in f)
                    file_details.append({
                        'file': file,
                        'size': format_size(size),
                        'lines': line_count
                    })
                except Exception as e:
                    print_error(f'{file}:\n\t{e}')
    
    # Output the file details
    format_data_with_tabulate(file_details)
    
    if total_size>0:
        print_success(f"\nTotal size of all files: {format_size(total_size)}")
    else:
        print_error(f"\nTotal size of all files: {format_size(total_size)}")

def analyze_directory(directory):
    """
    Generate a comprehensive report of all file types in the directory, including line counts for text-based files.
    """
    extension_summary = {}
    text_file_details = []

    for root, _, files in tqdm(os.walk(directory), desc="\033[93mAnalyzing directories \033[0m"):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                ext = os.path.splitext(file)[1].lower()
                if ext not in extension_summary:
                    extension_summary[ext] = {"count": 0, "total_size": 0}
                
                # Increment counts and size
                extension_summary[ext]["count"] += 1
                extension_summary[ext]["total_size"] += os.path.getsize(file_path)

                # Check if it's a text-based file
                if is_text_file(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        line_count = sum(1 for _ in f)
                    text_file_details.append({
                        "name": file,
                        "path": file_path,
                        "lines": line_count,
                        "size": os.path.getsize(file_path)
                    })
            except Exception as e:
                print_error(f"Error analyzing file {file_path}: {e}")
    
    # Print extension summary
    print("\n\033[96mFile Extension Summary:\033[0m")
    format_data_from_dict_list_with_tabulate(extension_summary)

    # Print text file details
    print("\n\033[92mText-Based File Details:\033[0m")
    format_data_with_tabulate(text_file_details)
