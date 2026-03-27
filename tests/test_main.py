from main import main
from data.direction import Direction

import subprocess
import sys


def test_main_without_error():
    result = subprocess.run([sys.executable, "main.py"], capture_output=True)

    assert result.returncode == 0
