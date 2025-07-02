from .path import get_path, valid_project
from pyxora.utils import asyncio,python
import subprocess
import webbrowser
import threading
import shutil
import time
import os
import sys

def open_browser(url, delay):
    def delayed_open():
        time.sleep(delay)
        webbrowser.open(url)
    threading.Thread(target=delayed_open, daemon=True).start()

def local_run(args):
    path = get_path(args.name)
    if not valid_project(path):
        print(f"No project found with name '{args.name}'")
        return

    # move to run path
    os.chdir(path)
    # load the main class
    main = python.load_class(os.path.join(path,"main.py"), "main")
    # run the main class
    asyncio.run(main)
    return path

def web_run(args):
    path = get_path(args.name)
    url = "http://localhost:8000/"
    if not valid_project(path):
        print(f"No project found with name '{args.name}'")
        return

    try:
        print("Running pygbag ...")
        print(f"Server ready: {url}")
        print("\nPress Ctrl+C to stop")
        open_browser(url,1)
        subprocess.run(
            [sys.executable, "-m", "pygbag", "main.py"],
            check=True,
            cwd=path,
            stdout=subprocess.DEVNULL,  # suppress output
            stderr=subprocess.DEVNULL  # suppress errors
        )
    except subprocess.CalledProcessError as e:
        print(f"pygbag failed with exit code {e.returncode}")
        return
    except KeyboardInterrupt:
        build_path = os.path.join(path,"build")
        shutil.rmtree(build_path)  # remove the tmp build folders
        return
    except FileNotFoundError:
        print("pygbag command not found. Please ensure pygbag is installed and in your PATH.")
        return

def run(args):
    """Run a project"""
    if args.web:
        web_run(args)
    else:
        local_run(args)
