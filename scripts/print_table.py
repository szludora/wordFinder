from colorama import Fore, Style, init
init ()

def print_formatted_table(table, forward_positions=None, backward_positions=None):
    if not table:
        return

    if forward_positions is None:
        forward_positions = set()
    if backward_positions is None:
        backward_positions = set()

    print()
    num_cols = len(table[0])
    row_num_width = len(str(len(table)))

    numbers_indent = " " * (row_num_width + 6)

    col_header = "".join([str(i).ljust(4) for i in range(1, num_cols + 1)])
    print(f"{numbers_indent}{col_header.rstrip()}")

    inner_width = num_cols + (num_cols + 1) * 3
    corner_indent = " " * (row_num_width + 2)

    print(f"{corner_indent}┌{'─' * inner_width}┐")

    for i, row in enumerate(table, 1):
        row_label = str(i).rjust(row_num_width)
        colored_row = []
        for j, cell in enumerate(row):
            if (i-1, j) in forward_positions:
                colored_row.append(Fore.GREEN + cell + Style.RESET_ALL)
            elif (i-1, j) in backward_positions:
                colored_row.append(Fore.YELLOW + cell + Style.RESET_ALL)
            else:
                colored_row.append(cell)
        content = "   ".join(colored_row)
        print(f"{row_label}  │   {content}   │")

    print(f"{corner_indent}└{'─' * inner_width}┘")
    print()
