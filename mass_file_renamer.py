
## script to rename files in a directory 
## returns a text document containing the renamed files and their corresponding new name 

import os 

##importing the extension list 
extension_file = open("EXTENSION_LIST.txt","r",encoding ="utf-8")
extension_list = []
for line in extension_file :
	extension_list.append(line.replace("\n",""))

for x in extension_list:
	print(x)



file_name = "FILE_LIST.txt"


old_files = []
new_files = []
directory = input("what is the directory for the files?")

## changing the working directory to parse files 
os.chdir(directory)


prefix = input("Should the renamed files have a prefix? y/n")
if(prefix =="y" or prefix =="yes" or prefix =="Y" or prefix =="YES" or prefix =="Yes"):
	prefixed = True
	prefix = input("What is the prefix")
else:
	prefixed = False




## parsing the directory for the files 

for path in os.listdir(directory):
	if (os.path.isfile(os.path.join(directory,path))):
		old_files.append(path)



## looping through old_files list and renaming stuff 

for x in range(0,len(old_files)):
	if(prefixed == True):
		new_name = prefix+str(x)
	else:
		new_name = str(x)

	## checking for extensions and attaching the appropriate one 
	
	for y in extension_list:
		if(y in old_files[x]):
			new_name += y
			break 

	##appending new names to list and renaming 
	
	new_files.append(new_name)

	os.rename(old_files[x],new_name)



## making list of renamed files 

file_name_open = open(file_name,"w",encoding = "utf-8")
for x in range(0,len(old_files)):
	file_name_open.write(str(old_files[x]))
	file_name_open.write("	")
	file_name_open.write(str(new_files[x]))
	file_name_open.write("\n")

file_name_open.close()
	

 
	

