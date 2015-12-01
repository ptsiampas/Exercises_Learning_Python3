# Write a program that walks a directory structure (as in the last section of this chapter), but instead of printing
# filenames, it returns a list of all the full paths of files in the directory or the subdirectories.
# (Don’t include directories in this list — just files.) For example, the output list might have elements like this:
#
# ['C:\Python31\Lib\site-packages\pygame\docs\ref\mask.html',
#  'C:\Python31\Lib\site-packages\pygame\docs\ref\midi.html',
#  ...
#  'C:\Python31\Lib\site-packages\pygame\examples\aliens.py',
#  ...
#  'C:\Python31\Lib\site-packages\pygame\examples\data\boom.wav',
#  ... ]
import os


def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def list_files(path, prefix=""):
    fileList = []
    if prefix == "":
        print('Folder listing for', path)
        prefix = path + '/'

    dirlist = get_dirlist(path)
    for f in dirlist:
        if not os.path.isdir(os.path.join(path, f)):  # FIXME: this is ugly as, but just want to fix it now..
            fileList.append(prefix + f)

        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            fileList.extend(list_files(fullname, prefix + f + '/'))
    return fileList


def main():
    print(list_files("/usr/local/lib/python3.4/dist-packages/pygame"))
    return


if __name__ == '__main__':
    main()
