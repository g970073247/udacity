import os

def rename_files():
    #1 get file names from a folder
    file_list = os.listdir("/home/wang/Desktop/udacity/prank")
    current_path = os.getcwd()
    os.chdir("/home/wang/Desktop/udacity/prank")
    print ('Current working directory : ' + current_path)

    for file_name in file_list:
        print('Old name - ' + file_name)
        print('New name - ' + file_name.translate(None, '0123456789'))
        os.rename(file_name,file_name.translate(None,'0123456789'))
    os.chdir(current_path)
    return file_list
print rename_files()




'''
file_list = os.listdir("/home/wang/Desktop/udacity/prank")
print file_list
print len(file_list)
'''
