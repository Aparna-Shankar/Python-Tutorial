

# class Open_File():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exec_type, exec_val, traceback): // teardown method - will get called when you exit
#         self.file.close()


# with Open_File('Test.txt', 'w') as f:
#     f.write('Test2')

# print(f.closed)


# The same functionality of enter and exit can be replicated by using the contextmanager decorator
# from contextlib import contextmanager


# @contextmanager
# def Open_File(filename, mode):
#     try:
#         f = open(filename, mode)
#         yield f  # is similar to return
#     finally:
#         f.close()


# with Open_File('Test.txt', 'w') as f:
#     f.write('Test2')

# print(f.closed)


# without context manager

from contextlib import contextmanager
import os

# # # Code to switch directories and list the contents of the switched directory
# # cwd = os.getcwd()
# # os.chdir('Dir')
# # print(os.listdir())
# # os.chdir(cwd)

# # the above functionality can be achieved wih the help of a context manager


# @contextmanager
# def chg_dir(destination):
#     try:
#         cwd = os.getcwd()
#         os.chdir(destination)
#         yield
#     finally:
#         os.chdir(cwd)


# with chg_dir('Dir'):
#     print(os.listdir())

# print(os.listdir())
