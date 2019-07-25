#!/usr/bin/env python

import os, sys
import getpass
import sh

print("SIMPLE ENUMERATION TOOL")
print()
print('Requirement: Install sh package. (pip install sh)')
print()

#Print kernel information
print('----------------------------------')
print("KERNEL VERSION")
print('----------------------------------')
print(os.system("uname -a"))
print()

# Print all users
print('----------------------------------')
print("USERS")
print('----------------------------------')
print(os.system("cat /etc/passwd"))

# Print all users
print('----------------------------------')
print("USERS")
print('----------------------------------')
print(os.system("cat /etc/shadow"))

# Print current user
print('----------------------------------')
print("CURRENT USER")
print('----------------------------------')
print(getpass.getuser())
print()

# Access environment variables
print('----------------------------------')
print("ENVIRONMENT VARIABLES")
print('----------------------------------')
print("HOME:")
print(os.environ['HOME'])
print("PATH:")
print(os.environ['PATH'])
print()

#Print the content of the home directory
print('----------------------------------')
print("CONTENT OF THE HOME DIRECTORY")
print('----------------------------------')
home_dir = os.environ['HOME']
dirs = os.listdir(home_dir)
for file in dirs:
  print(file)
print()

# Print IP information
print('----------------------------------')
print("IP CONFIGURATION")
print('----------------------------------')
print(os.system("ifconfig"))
print()

#Print processess run by root
print('----------------------------------')
print("PROCESSES RUN BY ROOT")
print('----------------------------------')
print(sh.grep(sh.ps("aux"), 'root'))
print()


