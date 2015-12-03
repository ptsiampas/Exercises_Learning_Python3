# Now write a program named cleanup.py that removes all these files.
import os


def clean_file(path):
    # print(path)
    os.remove(path)


def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_dir(path):
    """ Print recursive listing of contents of path """
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)  # Turn name into full pathname
        if os.path.isfile(fullname):
            clean_file(fullname)
        if os.path.isdir(fullname):  # If a directory, recurse.
            print_dir(fullname)


def main():
    print(print_dir("/home/petert/tmp"))
    return


if __name__ == '__main__':
    main()
