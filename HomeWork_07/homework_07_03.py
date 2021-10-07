with open('1.txt') as file1:
    len1 = sum(1 for _ in file1)

with open('2.txt') as file2:
    len2 = sum(1 for _ in file2)

with open('3.txt') as file3:
    len3 = sum(1 for _ in file3)


def get_pivot_dict(files_):
    dict_ = {}
    for file_, count in files_.items():
        if count not in dict_.keys():
            list_ = [file_]
            dict_[count] = list_
        else:
            dict_[count].append(file_)
    return dict_


files = {
    file1.name: len1,
    file2.name: len2,
    file3.name: len3
}

pivot_files = get_pivot_dict(files)
out = open('result.txt', 'w')
for count in sorted(pivot_files.keys()):
    file_name_list = pivot_files[count]
    for file_name in file_name_list:
        with open(file_name) as file:
            lines = file.readlines()
        out.write(file_name)
        out.write('\n')
        out.write(str(count))
        out.write('\n')
        out.writelines(lines)
        out.write('\n')
out.close()

with open('result.txt') as file:
    lines = file.readlines()

print(lines)

