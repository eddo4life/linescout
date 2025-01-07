import argparse
import os
import sys
from file_utils import count_files_and_lines_by_extension
from summary import generate_summary
from config import DEFAULT_EXTENSION, DEFAULT_DIRECTORY
from utils import print_error

def main():
    """
    Main function to handle the command-line arguments, validate them,
    count files and lines, and generate a report if requested.
    """
    parser = argparse.ArgumentParser(description="LineScout: Scan directories for file line counts.")
    parser.add_argument("directory", nargs="?", default=DEFAULT_DIRECTORY, help="Directory to scan: Default is the current working directory.")
    parser.add_argument("extension", nargs="?", default=DEFAULT_EXTENSION, help="File extension to filter by (e.g., .txt, .py). Defaults to config value.")
    parser.add_argument("--size", action="store_true", help="Include file size in summary.")
    parser.add_argument("--report", action="store_true", help="Generate a detailed report.")

    args = parser.parse_args()

    try:
        # Adjust arguments if necessary
        if args.directory.startswith('.'):
            # Treat as extension if it starts with a dot
            args.extension = args.directory
            args.directory = DEFAULT_DIRECTORY

        # Validate arguments
        validate_directory_and_extension(args)

    except Exception as e:
        print_error(e)
        sys.exit(1)

    # Count files and lines
    file_count, total_lines = count_files_and_lines_by_extension(args.directory, args.extension)

    # Print the summary
    print(f"The number of files with extension '{args.extension}' is: {file_count}")
    print(f"The total number of lines in those files is: {total_lines}")

    # Optionally, print file size and generate a detailed report
    if args.size:
        print("Including file sizes in summary...")

    if args.report:
        generate_summary(args.directory, args.extension)

def validate_directory_and_extension(args):
    """
    Validate the directory and file extension provided by the user.
    """
    if not args.extension.startswith('.'):
        raise ValueError(f"Invalid extension '{args.extension}'. Extensions should start with a '.'")
    if not os.path.exists(args.directory):
        raise ValueError(f"Directory '{args.directory}' does not exist.")

if __name__ == "__main__":
    main()
