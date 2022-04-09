import os
import shutil

file_list = os.listdir("./次枣/次枣数据集1")
file_path = "./次枣/次枣数据集1/"
file_name = "jujube_*.bmp"
file_name_number = 17
for i in range(len(file_list)):
    new_file_name = file_name.replace("*", str(file_name_number))
    try:
        shutil.move(file_path+new_file_name, "./test")
    except:
        continue
    finally:
        file_name_number += 3