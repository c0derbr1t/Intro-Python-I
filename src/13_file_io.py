"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
foo_file = open("foo.txt", "r")
print(foo_file.read())
foo_file.close()

print(foo_file.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar_file = open("bar.txt", "w")
bar_file.write("This is my Bar file. \n")
bar_file.write("There are many others like it. \n")
bar_file.write("But this one is all mine!")
bar_file.close()

bar_read = open("bar.txt", "r")
print(bar_read.read())
bar_read.close()