from file_utils import format_size


def format_table(headers, rows):
    """
    General function to format and print a table from headers and rows of data.
    """
    if not rows:
        print("No data provided.")
        return

    # Calculate max width for each column based on header and row values
    max_widths = {header: len(header) for header in headers}
    for row in rows:
        for header in headers:
            max_widths[header] = max(max_widths[header], len(str(row[header])))

    # Create border
    border = "+" + "+".join("-" * (max_widths[header] + 2) for header in headers) + "+"

    # Print headers
    print(border)
    header_row = "| " + " | ".join(f"{header:{max_widths[header]}}" for header in headers) + " |"
    print(header_row)
    print(border)

    # Print rows
    for row in rows:
        row_text = "| " + " | ".join(f"{str(row[header]):{max_widths[header]}}" for header in headers) + " |"
        print(row_text)

    print(border)


def format_data_from_list_dict(data):
    """
    Formats a list of dictionaries where each dictionary represents a row of data.
    Prints the data in a formatted table.
    """
    if not data:
        print("No data provided.")
        return

    # Extract headers (keys from the first dictionary)
    headers = list(data[0].keys())

    # Use the format_table helper function to print the data
    format_table(headers, data)


def format_data_from_dict_list(extension_summary):
    """
    Formats a dictionary where each key is an extension and each value is a dictionary
    containing the 'count' and 'total_size' for that extension.
    Prints the data in a formatted table.
    """
    if not extension_summary:
        print("No data provided.")
        return

    # Define the headers
    headers = ['Extension', 'Count', 'Total Size']

    # Prepare rows of data
    rows = []
    for ext, info in extension_summary.items():
        ext_str = ext or 'No Extension'
        count_str = str(info.get('count', 0))
        size_str = format_size(info.get('total_size', 0))
        rows.append({'Extension': ext_str, 'Count': count_str, 'Total Size': size_str})

    # Use the format_table helper function to print the data
    format_table(headers, rows)
