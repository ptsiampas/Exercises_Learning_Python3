import os


def get_dirlist(path):
    """
    Return a sorted list of all entries in the path.
    :param path: path to get the dir list.
    :return: Just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix=""):
    """
    Print recursive listing of contents of the path
    :param path: path name
    :param prefix: prefix to search for
    :return: list of files
    """
    if prefix == "":  # detect out most call, print heading
        print('Folder listing for', path)
        prefix = "|"

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix + f)  # print the line
        fullE = os.path.join(path, f)  # turn name into full path
        if os.path.isdir(fullE):
            print_files(fullE, prefix + "| ")


print_files("/home/petert/Documents")
