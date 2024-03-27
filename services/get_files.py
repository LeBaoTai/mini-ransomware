import os

_ALL_FILES = []
_ENC_FILES = []

def insert_enc_file(filename):
  _ENC_FILES.append(filename)

def get_enc_files():
  return _ENC_FILES

def re_scan_enc_file(directory):
  for root, _, filenames in os.walk(directory):
    for filename in filenames:
      file_path = os.path.join(root, filename)
      _ALL_FILES.append(file_path)

  for f in _ALL_FILES:
    if f.endswith('.enc'):
     _ENC_FILES.append(f)
  return _ENC_FILES
