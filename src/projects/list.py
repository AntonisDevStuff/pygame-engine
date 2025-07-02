from .path import get_projects_path
import os

def ls(args):
    """List all projects"""
    path = get_projects_path()
    projects = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

    if not projects:
        print("No projects found")
        return []

    print("Total:", len(projects))
    print("List:")
    for name in sorted(projects):
        print(f"  - {name}")
    return projects
