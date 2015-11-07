# Write a program that reads a file and writes out a new file with the lines in reversed order
# (i.e. the first line in the old file becomes the last one in the new file.)

i_handle = open("Exercise_13.11.1.txt", "r")
in_lines = i_handle.readlines()
i_handle.close()

in_lines.reverse()

o_handle = open("rExercise_13.11.1.txt", "w")
for out in in_lines:
    o_handle.write(out)
o_handle.close()

