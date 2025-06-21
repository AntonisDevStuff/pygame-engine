from .path import get_folders
import os

from pyxora.utils import asyncio, python

def run(args):
    """Run an example project."""
    example_name = args.name
    folders = get_folders()

    examples = {os.path.basename(folder): folder for folder in folders}
    if example_name not in examples:
        print(f"Example '{example_name}' does not exist.")
        return
    path = examples[example_name]
    os.chdir(path)
    main = python.load_class(os.path.join(path, "main.py"), "main")
    # run the main class
    asyncio.run(main)
    return path
