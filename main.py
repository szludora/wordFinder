import sys
import time
import io

from data.parameters import Parameters
from scripts.finder import find_words_in_table
from scripts.build_dynamic_data import build_dynamic_data
from scripts.import_params import import_params
from scripts.print_table import print_formatted_table

def main(parameters: Parameters) -> tuple[set, set]:
    if "pytest" not in sys.modules:
        if isinstance(sys.stdout, io.TextIOWrapper):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        if isinstance(sys.stderr, io.TextIOWrapper):
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
            
    if parameters.build_dynamic_table:
        build_dynamic_data(parameters)

    start = time.time()
    all_forward, all_backward  = find_words_in_table(parameters)
    print(f"Elapsed time: {(time.time() - start):.2f} seconds")

    print_formatted_table(parameters.table, all_forward, all_backward)




if __name__ == "__main__":
    use_custom_params: bool = '--params' in sys.argv
    params: Parameters = import_params(use_custom_params)
    main(params)
