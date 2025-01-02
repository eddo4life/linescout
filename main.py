from file_utils import count_files_and_lines_by_extension
import argparse

def main():
    parser = argparse.ArgumentParser(description="LineScout: Scan directories for file line counts.")
    parser.add_argument("directory", help="Directory to scan")
    parser.add_argument("extension", help="File extension to filter by (e.g., .txt, .py)")
    
    args = parser.parse_args()
    
    # Count files and lines
    file_count, total_lines = count_files_and_lines_by_extension(args.directory, args.extension)
    
    # Print the summary
    print(f"The number of files with extension '{args.extension}' is: {file_count}")
    print(f"The total number of lines in those files is: {total_lines}")
    
if __name__ == "__main__":
    main()
