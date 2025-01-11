from file_utils import format_size
from tabulate import tabulate

def format_data_with_tabulate(data):
    """
    Formats and prints data using the tabulate library.
    """
    if not data:
        print("No data provided.")
        return

    headers = list(data[0].keys())
    table = [list(row.values()) for row in data]

    print(tabulate(table, headers=headers))


def format_data_from_dict_list_with_tabulate(extension_summary):
    """
    Formats a dictionary of extensions and their information using tabulate.
    """
    if not extension_summary:
        print("No data provided.")
        return

    headers = ['Extension', 'Count', 'Total Size']
    rows = [
        [ext or 'No Extension', info.get('count', 0), format_size(info.get('total_size', 0))]
        for ext, info in extension_summary.items()
    ]

    print(tabulate(rows, headers=headers))
