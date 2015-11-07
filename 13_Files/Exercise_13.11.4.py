# 4. Write a program that undoes the numbering of the previous exercise: it should read a file with numbered lines
# and produce another file without line numbers.

infile = open("Exercise_13.11.3.txt", "r")
outfile = open("Exercise_13.11.4.txt", "w")

while True:
    line = infile.readline()
    if len(line) == 0:
        break
    # print(line[5:], end="")
    outfile.write(line[5:])

infile.close()
outfile.close()