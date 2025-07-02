"""
General-purpose utility functions used across the engine.
This module provides small helper functions to simplify common or very specific tasks.

Note:This module is not imported by default. You must import it explicitly wherever you need its functionality.
"""

from .decorators import run_every, event_listener
from .engine import print_versions, error, warning, quit
from .platform import get_platform, get_web_platform, is_web, is_local, is_windows, is_linux, is_mac, is_android
from .python import get_filename, get_filetype, load_module, load_class
