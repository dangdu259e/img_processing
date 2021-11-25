import os

FJoin = os.path.join


def GetFiles(path):
    """Output: file_list là danh sách tất cả các file trong path và trong tất cả các
           thư mục con bên trong nó. dir_list là danh sách tất cả các thư mục con
           của nó. Các output đều chứa đường dẫn đầy đủ."""
    file_list, dir_list = [], []
    for dir, subdirs, files in os.walk(path):
        file_list.extend([FJoin(dir, f) for f in files])
        dir_list.extend([FJoin(dir, d) for d in subdirs])
    # remove file is link
    file_list = filter(lambda x: not os.path.islink(x), file_list)
    dir_list = filter(lambda x: not os.path.islink(x), dir_list)
    return file_list, dir_list

def getFileName(path):
    files, dirs = GetFiles(os.path.expanduser(path))
    filenames = []
    for i in files:
        filenames.append(i.split('\\')[1])
    return filenames

if __name__ == "__main__":
    filenames = getFileName(os.path.expanduser("./img"))
    print(filenames)
