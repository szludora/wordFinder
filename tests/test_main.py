from main import main

import os
import subprocess
import sys

from scripts.import_params import import_params

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_main_without_error():
    result = subprocess.run([sys.executable, os.path.join(ROOT_DIR, "main.py")], capture_output=True, cwd=ROOT_DIR)
    assert result.returncode == 0

def test_main_with_params_json():
    original_dir = os.getcwd()
    try:
        os.chdir(ROOT_DIR)
        params = import_params(True)
        main(params)
        assert len(params.table) == 15
        assert len(params.table[0]) == 20
    finally:
        os.chdir(original_dir)

def test_main_with_params_default():
    original_dir = os.getcwd()
    try:
        os.chdir(ROOT_DIR)
        params = import_params(False)
        main(params)
        assert len(params.table) == 13
        assert len(params.table[0]) == 13
    finally:
        os.chdir(original_dir)
