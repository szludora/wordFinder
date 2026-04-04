# 🔍 WordFinder

## A modular Python-based utility designed to search for words within a grid or dataset. This project features a clean separation of concerns, built-in testing, and type-safe directional logic.

## 📂 Project Structure

The repository is organized for high maintainability and clarity:

- **`main.py`**: The central entry point for running the application.
- **`data/`**:
  - `datas.py`: Contains the word lists, grids, or data definitions.
  - `direction.py`: Defines search orientations using Python **Enums**.
  - `parameters.py`: Defines the parameters for the word search.
- **`scripts/`**:
  - `finder.py`: The core search engine and matching algorithms.
  - `build_dynamic_data.py`: A utility for generating dynamic tables.
  - `import_params.py`: Handles importing and validating parameters from external sources (e.g., JSON, YAML).
  - `print_table.py`: Utilities for formatting and displaying results in the terminal.
- **`tests/`**: A dedicated suite using `pytest` to ensure search accuracy.
  - `test_main.py`: Functional tests for the main application flow.
  - `test_searching.py`: Specific logic tests for the search algorithm.
- **`.vscode/`**: Pre-configured environment settings, including debugger and editor configurations.

---

## 🚀 Key Features

- **Structural Pattern Matching:** Utilizes Python 3.10+ `match-case` statements for clean and readable direction dispatching.
- **Type-Safe Directions:** Uses `Enum` for handling orientations, significantly reducing string-based errors.
- **Multi-Directional Search:** 
  - **Horizontal:** Efficient string-based searching (forward and backward), alternative KMP algorithm.
  - **Diagonal:** Comprehensive 4-way diagonal scanning (↘, ↖, ↙, ↗).
  - **Vertical:** Comprehensive 2-way diagonal scanning (^, v).
- **Clean Visualization:** Results are formatted into a readable, professional table for the terminal via `print_table.py`.
- **Automated Testing:** High reliability thanks to integrated unit tests in the `tests/` directory.
- **Dynamic Data Generation:** The `build_dynamic_data.py` script allows for easy creation of new tables and datasets for testing or demonstration purposes.
- **Parameter Importing:** The `import_params.py` module supports flexible configuration through external files, making it easy to adjust search parameters without modifying code.
- **Color-Coded Output:** Uses `colorama` to enhance terminal output, making it easier to distinguish between forward and backward matches.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/szludora/wordFinder.git
   cd wordFinder
   ```
2. **Set up a Virtual Environment (Recommended):**

   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   The project primarily uses standard libraries, but pytest is required for running tests:

   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

To start the WordFinder, simply run the main script from the root directory:

```bash
python main.py
```

## 🧪 Testing

To verify the logic and ensure everything is working correctly, run the test suite:

```bash
python -m pytest
```

## 📄 License

Distributed under the MIT License. See LICENSE for more information.

Developed by:

- Szlucska Dóra
- Lukácsné Téglás Anikó
- Segyevy Nándor
- Tőzsér Máté
