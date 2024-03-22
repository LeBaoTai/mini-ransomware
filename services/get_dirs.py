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

def get_all_dirs():
  dirs = []
  for drive in get_available_drives():
    if str(drive) == 'C':
      dirs.append(str(drive) + ':\\Users')
    else:
      dirs.append(str(drive) + ':\\Users')
  return dirs