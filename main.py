from file_utils import count_files_and_lines_by_extension
from summary import generate_summary
import argparse

def main():
    parser = argparse.ArgumentParser(description="LineScout: Scan directories for file line counts.")
    parser.add_argument("directory", help="Directory to scan")
    parser.add_argument("extension", help="File extension to filter by (e.g., .txt, .py)")
    parser.add_argument("--size", action="store_true", help="Include file size in summary")
    parser.add_argument("--report", action="store_true", help="Generate a detailed report")
    
    args = parser.parse_args()
    
    # Count files and lines
    file_count, total_lines = count_files_and_lines_by_extension(args.directory, args.extension)
    
    # Print the summary
    print(f"The number of files with extension '{args.extension}' is: {file_count}")
    print(f"The total number of lines in those files is: {total_lines}")
    
    # Optionally, print file size and generate detailed report
    if args.size:
        print("Including file sizes in summary...")
    
    if args.report:
        generate_summary(args.directory, args.extension)

if __name__ == "__main__":
    main()
