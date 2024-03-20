import os

class GetFiles():
  def __init__(self, my_dir) -> None:
    self.my_dir = my_dir
    self.all_files = []
    for root, directories, filenames in os.walk(my_dir):
        for filename in filenames:
            file_path = os.path.join(root, filename)  
            self.all_files.append(file_path)
    pass

  def get_txt_files(self):
    txt_files = []
    for f in self.all_files:
      if(f.endswith('.txt')):
        txt_files.append(f)
    return txt_files

  def get_docx_files(self):
    docx_file = []
    for f in self.all_files:
      if f.endswith('.doc') or f.endswith('.docx'):
        docx_file.append(f)
    
    return docx_file
  
  def get_pdf_files(self):
    pdf_files = []
    for f in self.all_files:
      if f.endswith('.pdf'):
        pdf_files.append(f)

    return pdf_files

  def get_nhom1_files(self):
    nhom1_files = []
    for f in self.all_files:
      if f.endswith('.nhom1'):
        nhom1_files.append(f)

    return nhom1_files