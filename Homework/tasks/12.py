def findoutXtension(name_file):

    name_file = name_file.split('.')
    if len(name_file) < 2:
        print("У файла нет расширения")

    print('Расширение файла ', name_file[-1])
findoutXtension('file.exe')