from .path import get_folders
import os

def ls(args):
    """List all examples."""
    print("Examples:")
    folders = get_folders()
    for folder_path in sorted(folders):
        print(f"  - {os.path.basename(folder_path)}")

    return folders
