import os

def print_dir(path, level):
    files = os.listdir(path)
    for f in files:
        if os.path.isdir(f'{path}/{f}'):
            print('\t' * level, end='') # print tabs at level
            print(f' + {f}')            # print folder name
            print_dir(f'{path}/{f}', level+1)       # recursively print folder contents
        else:
            print('\t' * level, end='') # print tabs at level
            print(f' - {f}')            # print file name


path = input('Enter a path: ')
print_dir(path, 0)