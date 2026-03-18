def print_formatted_table(table):
    if not table:
        return

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
        content = "   ".join(row)
        print(f"{row_label}  │   {content}   │")

    print(f"{corner_indent}└{'─' * inner_width}┘")
    print()
