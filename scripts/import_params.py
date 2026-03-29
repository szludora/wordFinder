from data.parameters import Parameters
from data.direction import Direction
import json

def import_params(use_parameters_file: bool) -> Parameters:
    """
        Optionally read the parameters stored in the `params/parameters.json` file,
        or provide the default parameters defined in the `data/parameters.py` file.
        Directions parameter in `params/parameters.json` file expected to match the enum names, not the values.
    """
    if use_parameters_file:
        print("Fetch parameters from params/parameters.json file")
        config = get_params()
        result: Parameters = Parameters()
        if "useKMP" in config:
            result.use_kmp = config["useKMP"]
        if "buildTable" in config:
            result.build_dynamic_table = config["buildTable"]
        if "minDimensionX" in config:
            result.dynamic_table_min_x = config["minDimensionX"]
        if "minDimensionY" in config:
            result.dynamic_table_min_y = config["minDimensionY"]
        if "requiredWords" in config:
            result.required_words = config["requiredWords"]
        if "words" in config:
            result.words = config["words"]
        if "directions" in config:
            result.directions = [Direction[d] for d in config["directions"]]
        return result
    else:
        print("Use default parameters.")
        result: Parameters = Parameters()
        return result
    
def get_params():
    with open("params/parameters.json", "r", encoding="utf-8") as f:
        return json.load(f)