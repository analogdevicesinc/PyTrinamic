################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Check if the project is sane."""

import pathlib
import re

import pytrinamic.version


this_files_dir_path = pathlib.Path(__file__).parent
project_root_dir_path = this_files_dir_path / ".."


def test_version():
    """Check if the version in the version file matches the one of the installed package."""

    version_file_path = project_root_dir_path / "pytrinamic/version.py"
    version_pattern = re.compile(r"^__version__\s*=\s*['\"]([^'\"]+)['\"]")
    with open(version_file_path, "r") as file:
        version_line = file.readline()
    m = re.match(version_pattern, version_line)
    version_str = m.group(1)
    assert pytrinamic.version.__version__ == version_str


def test_connection_manager():
    """Check if the connection manager can be imported."""

    from pytrinamic.connections import ConnectionManager

    _ = ConnectionManager()
