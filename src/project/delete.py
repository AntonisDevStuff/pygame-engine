from .path import get_path,valid_project
from shutil import rmtree as rm
from time import sleep

def delete(args):
    """Delete a project."""
    path = get_path(args.name)
    if not valid_project(args.name):
        print(f"No project found with name '{args.name}'")
        return

    # deletion process is irreversible, so this is safe mechanism
    # the force is for bypassing the confirmation prompt, great for gui.
    force = args.force
    timer = 3
    if not force:
        print("WARNING: This action is irreversible")
        verify = input(f"Are you sure you want to delete project '{args.name}'? [y/N] ").lower() == "y"
        if not verify:
            print("No action taken")
            return
        while timer > 0:
            print(f"Deleting in {timer} seconds...")
            sleep(1)
            timer -= 1
    rm(path)
    print(f"project `{args.name}` deleted successfully!")
    return path
