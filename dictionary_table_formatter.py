def format_data_from_dict_list(data):
    """
    Formats a list of dictionaries where each dictionary represents a row of data.
    Prints the data in a formatted table.
    """
    if not data:
        print("No data provided.")
        return

    # Extract headers (keys from the first dictionary)
    headers = list(data[0].keys())
    max_widths = {header: len(header) for header in headers}

    # Calculate max width for each column based on header and row values
    for row in data:
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
    for row in data:
        row_text = "| " + " | ".join(f"{str(row[header]):{max_widths[header]}}" for header in headers) + " |"
        print(row_text)

    print(border)

