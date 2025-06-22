from .path import get_path,valid_project,create_path
from datetime import datetime
import os.path
import json
import shutil
import getpass
import pyxora


def new(args):
    """Create a new project."""
    path = get_path(args.name)
    system_user = getpass.getuser()
    if valid_project(args.name):
        print(f"project `{args.name}` already exists!")
        return

    create_path(args.name)
    if not args.author:
        args.author = system_user

    if args.input:
        print("Note: if you want to use the default value, just press enter")
        print("======================")
        author = input("Enter project author: ")
        description = input("Enter project description: ")
        version = input("Enter project version: ")
        tags = input("Enter project tags (use comma to separate tags): ").split(",")
        if description:
            args.description = description.strip()
        if author:
            args.author = author.strip()
        if version:
            args.version = version.strip()
        if tags:
            args.tags = [tag.strip() for tag in tags]
        print("======================")

    metadata_file = os.path.join(path, "metadata.json")
    with open(metadata_file, "w") as f:
        json.dump(
            {
                "name": args.name,
                "description": args.description,
                "author": args.author,
                "version": args.version,
                "engine": pyxora.version,
                "tags": args.tags,
                "created": datetime.today().strftime('%d/%m/%Y')
            }, f, indent=4
        )
    print(f"path: {path}")
    print(f"project '{args.name}' created successfully!")

    shutil.copytree(os.path.join(os.path.dirname(pyxora.__file__),"data","template"), path,dirs_exist_ok=True)
    return path
