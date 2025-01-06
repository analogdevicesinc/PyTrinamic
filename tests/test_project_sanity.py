
import pathlib
import re

import pytrinamic.version


this_files_dir_path = pathlib.Path(__file__).parent
project_root_dir_path = this_files_dir_path / ".."


def test_version():
    version_file_path = project_root_dir_path / "pytrinamic/version.py"
    version_pattern = re.compile(r"^__version__\s*=\s*['\"]([^'\"]+)['\"]")
    with open(version_file_path, "r") as file:
        version_line = file.readline()
    m = re.match(version_pattern, version_line)
    version_str = m.group(1)
    assert pytrinamic.version.__version__ == version_str