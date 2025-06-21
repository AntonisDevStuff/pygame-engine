import os.path

def get_folders():
    path = os.path.dirname(os.path.abspath(__file__))
    folders = [
        os.path.join(path, name)
        for name in os.listdir(path)
        if os.path.isdir(os.path.join(path, name)) and name != "__pycache__"
    ]
    return folders
