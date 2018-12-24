# File Objects


# f = open('File_test.txt','r')
# print(f.name) # prints the name of the file
# print(f.mode) # prints the mode in which the file was opened
# f.close()

#using files with context managers. This will automatically close files
#with open('File_test.txt','r') as f:


	# f_contents = f.readline()
	# print(f_contents, end='') # end='' gets rid of the newline after reading each line
	# f_contents = f.readline()
	# print(f_contents, end='')

# print(f.closed) # to check if the file is closed
# print(f.read()) # cannot read the file when closed


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


# # Writing to files

# with open('File_test_w','w') as f:
# 	f.write('Test')
# 	f.seek(0)
# 	f.write('Rest')


# # Reading & Writing to files

# with open('File_test.txt','r') as rf:
# 	with open('File_test_w','w') as wf:
# 		for line in rf:
# 			wf.write(line)


# # Writing image files in binary mode
# with open('watercolour.jpg','rb') as rf:
# 	with open('watercolour_copy.jpg','wb') as wf:
# 		for line in rf:
# 			wf.write(line)


# Writing image files in binary mode in chunks
with open('watercolour.jpg','rb') as rf:
	with open('watercolour_copy.jpg','wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)
