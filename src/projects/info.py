from .path import get_path,valid_project
import json
import os.path

def info(args):
    """Display information about a project by name."""
    path = get_path(args.name)
    metadata_file = os.path.join(path, "metadata.json")

    if not valid_project(args.name):
        print(f"No project found with name '{args.name}'")
        return

    try:
        with open(metadata_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        print("=======================")
        print(f"Name:        {metadata.get('name')}")
        print(f"Description: {metadata.get('description')}")
        print(f"Version:     {metadata.get('version')}")
        print(f"Engine:      {metadata.get('engine')}")
        print(f"Tags:        {', '.join(metadata.get('tags'))}")
        print("=======================")
        print(f"Author:      {metadata.get('author')}")
        print(f"Created:     {metadata.get('created')}")
        print("=======================")
    except json.JSONDecodeError:
        print("Error: Failed to parse metadata.json. Is it valid JSON?")
        return False
    return metadata
