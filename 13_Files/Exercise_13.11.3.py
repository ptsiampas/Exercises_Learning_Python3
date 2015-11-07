# 3. Write a program that reads a text file and produces an output file which is a copy of the file, except the first
# five columns of each line contain a four digit line number, followed by a space. Start numbering the first line
# in the output file at 1. Ensure that every line number is formatted to the same width in the output file.
# Use one of your Python programs as test data for this exercise: your output should be a printed and numbered
# listing of the Python program.

file = open("Exercise_13.11.1.py", "r")
outfile = open("Exercise_13.11.3.txt", "w")
count = 1

while True:
    line = file.readline()
    if len(line) == 0:
        break
    formated_line = "{0:04d} {1}".format(count,line)
    print(formated_line, end="")
    outfile.write(formated_line)
    count += 1

file.close()
outfile.close()
