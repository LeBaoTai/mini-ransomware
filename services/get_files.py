import os

_ALL_FILES = []
_ENC_FILES = []

def get_all_files(directory):
  for root, _, filenames in os.walk(directory):
    for filename in filenames:
      file_path = os.path.join(root, filename)
      _ALL_FILES.append(file_path)

def get_txt_files():
  txt_files = []
  for f in _ALL_FILES:
    if(f.endswith('.txt')):
      txt_files.append(f)
  return txt_files

def get_docx_files():
  docx_file = []
  for f in _ALL_FILES:
    if f.endswith('.doc') or f.endswith('.docx'):
      docx_file.append(f)
  return docx_file

def get_pdf_files():
  pdf_files = []
  for f in _ALL_FILES:
    if f.endswith('.pdf'):
      pdf_files.append(f)
  return pdf_files

def get_nhom1_files():
  nhom1_files = []
  for f in _ALL_FILES:
    if f.endswith('.nhom1'):
      nhom1_files.append(f)
  return nhom1_files

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
