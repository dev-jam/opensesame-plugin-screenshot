# Copyright (C) 2024-2026 Bob Rosbag <mail@bobrosbag.nl>
# SPDX-License-Identifier: GPL-3.0-or-later

from importlib.metadata import PackageNotFoundError, version

# These packages will be checked by the updater extension for updates on
# conda and pip
packages = ['opensesame-plugin-screenshot']

# The version is set in pyproject.toml only; this reads it from the
# installed package
try:
    __version__ = version(packages[0])
except PackageNotFoundError:
    # Running from a source folder that is not installed
    __version__ = 'unknown'
