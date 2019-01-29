"""
File Objects

******************************************************************************************************
Reading from files
******************************************************************************************************

"""


f = open('File_test.txt','r') # Here f is the file object

print(f.name) # prints the name of the file
print(f.mode) # prints the mode in which the file was opened


# f_contents = f.readline() # Reads the file line by line
# print(f_contents, end='') # end='' gets rid of the newline after reading each line
# f_contents = f.readline()
# print(f_contents, end='')

f_contents = f.read() # Reads the entire file
# print(f_contents)

"""
There is a limit to the number of files that can be opened simultaneously. So it is necessary 
to close the file after we read it

"""
f.close()

print(f.closed) # to check if the file is closed
# print(f.read()) # cannot read the file when closed

"""
Using files with context managers. This will automatically close files
with open('File_test.txt','r') as f:

"""

# To read the entire file contents using for loop

	# for line in f:
	# 	print(line, end='')


# To read certain number of characters from the file

	# size_to_read = 10

	# f_contents = f.read(size_to_read)
	# while len(f_contents) > 0:
	# 	print(f_contents, end='')
	# 	f_contents = f.read(size_to_read)
	

	# print(f.tell()) # Tells the current postion after file read
	# f.seek(0) # sets the cursor back to postion 0 of the file

"""
******************************************************************************************************
Writing to files
Opening the file in w mode overwrites it's contents
******************************************************************************************************
"""
# with open('File_test_w','w') as f:
# 	f.write('Test')
# 	f.seek(0)
# 	f.write('Rest')


# # Reading & Writing to files
# with open('File_test.txt','r') as rf:
# 	with open('File_test_w','w') as wf:
# 		for line in rf:
# 			wf.write(line)


# Writing to another file only if content matches the user's input
# Ask User for a list of 3 friends
# Tell user if friend present in file
# Write friend to file copy

rf = open('File_test.txt', 'r')
f_line = rf.readlines()  #This returns the content of the file in the form of a list with a '\n'
rf.close()

new_line = [line.strip() for line in f_line]

friends = input('Enter 3 friend names separated by (,): ').split(',')
#The split function above also returns the string contents as a list

file_line_set = set(new_line)
friends_set = set(friends)
pos_present = file_line_set.intersection(friends_set)
wf = open('File_test_w.txt', 'w')

for pos in pos_present:
	wf.write(f'{pos}\n')
	print(f'{pos} is present in file!')
wf.close()


# # Writing image files in binary mode
# with open('watercolour.jpg','rb') as rf:
# 	with open('watercolour_copy.jpg','wb') as wf:
# 		for line in rf:
# 			wf.write(line)


# # Writing image files in binary mode in chunks
# with open('watercolour.jpg','rb') as rf:
# 	with open('watercolour_copy.jpg','wb') as wf:
# 		chunk_size = 4096
# 		rf_chunk = rf.read(chunk_size)
# 		while len(rf_chunk) > 0:
# 			wf.write(rf_chunk)
# 			rf_chunk = rf.read(chunk_size)
