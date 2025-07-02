from pygame.system import get_pref_path
from shutil import rmtree as rm
import os

# help functions to manage the project directory

def create_path(name):
    """Creates the path to the target project directory"""
    return get_pref_path("pyxora",name)

def get_projects_path():
    """Returns the path to the projects directory."""
    # hack to get the projects directory
    tmp_path = os.path.abspath(get_pref_path("pyxora","..tmp"))
    path = os.path.dirname(tmp_path)
    rm(tmp_path)
    return path

def get_path(name):
    """Returns the path to the target project directory."""
    projects_path = get_projects_path()
    path = os.path.join(projects_path, name)
    return path

def valid_project(name):
    """Checks if a project with the given name exists and is valid."""
    metadata_file = os.path.join(get_path(name), "metadata.json")
    if not os.path.isfile(metadata_file):
        return False
    return True
