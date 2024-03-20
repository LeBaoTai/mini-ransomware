import os
from pathlib import Path

def get_home_dirs():
  dirs = []
  user_path = str(Path.home())
  document_path = user_path + '\\Documents\\'
  dirs.append(document_path)
  desk_top_path = user_path + '\\Desktop\\'
  dirs.append(desk_top_path)
  return dirs

  