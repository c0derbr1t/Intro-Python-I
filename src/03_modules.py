"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import fileinput
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("SYS.ARGV: ")
args = sys.argv[0].split("/")
for i in args:
    print(i)

# for line in fileinput.input():
#     print(line)

# Print out the OS platform you're using:
# YOUR CODE HERE
print("PLATFORM: ")
print(sys.platform)
if sys.platform == 'linux':
    print("Linux")
elif sys.platform == 'win32':
    print("Windows")
elif sys.platform == 'darwin':
    print("Mac")
else:
    print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("VERSION: ")
print(sys.version)

import os
import getpass
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("PROCESS ID: ")
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("CWD: ")
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("LOGIN: ")
print(os.getlogin())
print(getpass.getuser())