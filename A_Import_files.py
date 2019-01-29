'''
This explains how to import python functionality from another file
Whenever we import something, that's called a module
and whenever we run something, that's called a script.
generally, we have one script and many modules that we import
One thing we need to remember is that any code in the module will be executed during import
'''

'''
Option 1: import entire module
'''

# import File_Operations
# File_Operations.save_to_file('Aparna', 'Import_namefile.txt')

'''
Option 2: import only certain functions. This will however be a problem if you have functions of
#same name in multiple modules
#imports can be done only if the modules are available in the top level of project
'''

from Utils.common.File_Operations import save_to_file, read_file

'''
Directory name Utils need to be specified
# This is called an absolute import because we specify the full path right from the project folder
'''

# from Utils.find import find_in

# save_to_file('Aparna', 'Import_namefile.txt')
# print(read_file('Import_namefile.txt'))
print(__name__)


'''
Import Errors
When we try to import a specific function from a module that is already imported, it throws an error.
However, if we just import the module again, Python knows to ignore it because it knows that we already imported it.

e.g: In Import files, if we import File_operations and File_operations import find and find in turn again tries to import File_operations
Here, it will throw an error if we are trying to import specific methods in find. It however knows to ignore if we import the entire module
'''




