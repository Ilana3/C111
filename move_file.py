import os
import shutil

from_dir = "C:/Users\Sergio\Documents\Programação\C111\Downloads"
to_dir = "C:/Users\Sergio\Documents\Programação\C111"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    print(name)
    print(extension)

    if extension == "":
        continue

    if extension in [".txt", ".pdf", ".doc", ".docx"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Arquivos_documentos" 
        path3 = to_dir + "/" + "Arquivos_documentos" + file_name

    if os.path.exists(path2):
        print("movendo " + file_name)
        shutil.move(path1, path3)
    else:
        os.makedirs(path2)
        print("movendo " + file_name)
        shutil.move(path1, path3)
