# -*- coding: utf-8 -*-
"""
Loads environment variables from .env and configures sys.path for quartopy.

This module is imported at the top of entry-point scripts so that
``from quartopy import ...`` works regardless of IDE configuration.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the project root (same directory as this file)
_PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(_PROJECT_ROOT / ".env")

# --------------- quartopy path ---------------

def setup_quartopy(*, silent: bool = True):
    """Add QUARTOPY_PATH to sys.path if not already present."""
    quartopy_path = os.getenv("QUARTOPY_PATH")
    if quartopy_path and quartopy_path not in sys.path:
        sys.path.insert(0, quartopy_path)
        if not silent:
            print(f"[setup_dependencies] Added QUARTOPY_PATH to sys.path: {quartopy_path}")


# Run automatically on import
setup_quartopy()
