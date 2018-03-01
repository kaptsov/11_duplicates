import argparse
import os
from collections import defaultdict


def get_directory_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirpath')
    return parser.parse_args()


def find_duplicates(root_directory):
    dup_files = defaultdict(list)
    for dirpath, dirnames, files in os.walk(root_directory):
        for filename in files:
            full_file_path = os.path.join(dirpath, filename)
            file_size = os.stat(full_file_path).st_size
            dup_files[(filename, file_size)].append(full_file_path)
    return {key[0]: val for key, val in dup_files.items() if len(val) > 1}


def print_list(duplicate_list):
    for key, value in duplicate_list.items():
        print('File "{0}" found in following directories:'.format(key))
        for v in value:
            print('    {0}'.format(v))


if __name__ == '__main__':
    try:
        directory_path = get_directory_path().dirpath
        print('Alright, let me see..')
        duplicate_list = find_duplicates(directory_path)
        print_list(duplicate_list)
    except (NotADirectoryError):
        exit('Folder is missing.')
