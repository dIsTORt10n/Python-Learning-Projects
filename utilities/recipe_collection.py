"""Compatibility wrapper for the legacy recipe collection script."""

import importlib.util
from pathlib import Path


def run_legacy_script(filename):
    """Load a script from the repository root and execute it."""
    script_path = Path(__file__).resolve().parents[1] / filename
    spec = importlib.util.spec_from_file_location("legacy_script", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    """Run the original root script."""
    module = run_legacy_script("recipe_collection.py")
    if hasattr(module, "main"):
        module.main()


if __name__ == "__main__":
    main()
