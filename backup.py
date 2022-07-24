
#this program compares two file repositories
#and prints commands to linux to delete (or copy)
#those files that are only in one of the two repositories

import os
path1 = '' 
path2 = '' #you will copy or delete files in this storage
a = list(os.popen(f"ls '{path1}'"))
b = list(os.popen(f"ls '{path2}'"))
for i in range(len(a)):
    a[i] = a[i][:-1]
for i in range(len(b)):
    b[i] = b[i][:-1]
#print(a)
#print()
#print(b)
#print()
flag = 0
for i in range(len(b)):
    if b[i] not in a:
        command = f"rm {path2}/'{b[i]}'"
        print(command)
        flag = 1

#for i in range(len(b)):
#    if b[i] not in a:
#        command = f'cp {path2}/{b[i]} {path1}/{b[i]}'
#        print(command)
#        flag = 1
if flag == 0:
    print('complete match :)')       
