# Chapter 13 Files
http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3/files.html

## Notes
### Read a line at a time:
Standard text file read pattern.

```python
mynewhandle = open("test.txt", "r")
while True:                            # Keep reading forever
    theline = mynewhandle.readline()   # Try to read next line
    if len(theline) == 0:              # If there are no more lines
        break                          #     leave the loop

    # Now process the line we've just read
    print(theline, end="")

mynewhandle.close()
```

Minimal binary file read.

```python
f = open("somefile.zip", "rb")
g = open("thecopy.zip", "wb")

while True:
    buf = f.read(1024)  # Read up to 1024 bytes
    if len(buf) == 0:
         break
    g.write(buf)

f.close()
g.close()
```

## Exercises Completed
#### 13.11. Exercises
1. ~~Write a program that reads a file and writes out a new file with the lines in reversed order (i.e. the first line in the old file becomes the last one in the new file.)~~
2. ~~Write a program that reads a file and prints only those lines that contain the substring snake.~~
3. ~~Write a program that reads a text file and produces an output file which is a copy of the file, except the first five columns of each line contain a four digit line number, followed by a space. Start numbering the first line in the output file at 1. Ensure that every line number is formatted to the same width in the output file. Use one of your Python programs as test data for this exercise: your output should be a printed and numbered listing of the Python program.~~
4. ~~Write a program that undoes the numbering of the previous exercise: it should read a file with numbered lines and produce another file without line numbers.~~
