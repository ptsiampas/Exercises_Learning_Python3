# Write a program named litter.py that creates an empty file named trash.txt in each subdirectory of a directory
# tree given the root of the tree as an argument (or the current directory as a default).
import os


def create_trash(path):
    print(path + "/litter.txt")
    trash = open(path + "/litter.txt", "w")
    trash.write("..\n")
    trash.close()


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
        if os.path.isdir(fullname):  # If a directory, recurse.
            create_trash(fullname)
            print_dir(fullname)


def main():
    print(print_dir("/home/petert/tmp"))
    return


if __name__ == '__main__':
    main()
