# 2 Write a program that reads a file and prints only those lines that contain the substring snake.
f_handle = open("Exercise_13.11.2.txt", "r")

while True:
    line = f_handle.readline()
    if len(line) == 0:
        break
    if "snake" in line.lower():
        print(line, end="")
