import os
from pathlib import Path

class GetDirs():
  def __init__(self) -> None:
    pass

  def get_home_dirs(self):
    dirs = []
    user_path = str(Path.home())
    document_path = user_path + '\\Documents\\'
    dirs.append(document_path)
    desk_top_path = user_path + '\\Desktop\\'
    dirs.append(desk_top_path)

    return dirs
  
  def scan_all_files(self, directory):
    """Scans all files in a directory and its subdirectories."""
    all_files = []
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)  # Combine path and filename
            all_files.append(file_path)
    return all_files

  def get_all_child_dirs(self, parrent_dir):
    print('test')

  