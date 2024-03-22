from pathlib import Path
import ctypes
import itertools
import os
import string
import platform

def get_available_drives():
    if 'Windows' not in platform.system():
        return []
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    return list(itertools.compress(string.ascii_uppercase,
               map(lambda x:ord(x) - ord('0'), bin(drive_bitmask)[:1:-1])))

def get_home_dirs():
  dirs = []
  for drive in get_available_drives():
    dirs.append(str(drive) + ':\\')
  return dirs


print(get_home_dirs())