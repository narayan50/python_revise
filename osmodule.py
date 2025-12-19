# os modules demo
import os
print(os.name)

print("hello")

# to check wheather in which os u r on

# nt is windo kernal
# posix is linux unix or mac kernal

if os.name == "nt":
    print("your machine is running on Windows")
else:
    print("your machine is not running on Windows")

# making new directorry py os module 

os.mkdir("C:\\MYsql\\python_revise\\newdirectory")



# to chceck wheather in which directory we are working in it

print(os.getcwd())

# to change current working directory

os.chdir("C:\\")

print("current dir:-----",os.getcwd())

# deleting folder from our system

os.rmdir("C:\\MYsql\\python_revise\\newdirectory")

# listing all directory cwd

os.chdir("C:\\MYsql\\python_revise")

print(os.listdir())


