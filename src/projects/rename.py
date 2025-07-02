from .path import get_projects_path, valid_project
import os
import json

def rename(args):
    """Rename a project"""
    project_path = get_projects_path()
    old_path = os.path.join(project_path, args.old_name)
    new_path = os.path.join(project_path, args.new_name)

    # os checks
    if not valid_project(args.old_name):
        print(f"Project '{args.old_name}' does not exist")
        return

    if valid_project(args.new_name):
        print(f"A project named '{args.new_name}' already exists")
        return

    # project checks
    project_file = os.path.join(old_path, "metadata.json")
    try:
        with open(project_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        data["name"] = args.new_name
        with open(project_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except json.JSONDecodeError:
        print("Error: Failed to parse metadata.json. Is it valid JSON?")
        return False

    os.rename(old_path, new_path)

    print(f"Project renamed from '{args.old_name}' to '{args.new_name}'")

    return new_path
