import os

path = r"d:\read_write_test"

i = 0
pathList = []
for (path, dirs, files) in os.walk(path):
    print("////////////////////////////////////////////////////////////////////////")
    print(path)
    # print(dirs)
    print(files)
    # pathList.append(path)
    print("-------------")


# print(pathList)
