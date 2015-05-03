import sys
import os

root_dir = sys.argv[1]
target_string = sys.argv[2]

def remove_line_containing_str(file_name):
    target_file = open(file_name, "r+")
    log_file = open("log_file.txt", "a")
    log_file.write(file_name + "\n")
    file_lines_list = list(target_file)
    line_nums_to_remove = []
    
    for index, line in enumerate(file_lines_list, start=0):
        if target_string in line:
            log_file.write("\t" + line)
            line_nums_to_remove.append(index)

    for line_num in reversed(line_nums_to_remove):
        del file_lines_list[line_num]

    target_file.seek(0)
    target_file.truncate()
    for line in file_lines_list:
        target_file.write(line)
    target_file.close()
    log_file.write("*****************************************************" + "\n" +  "\n")
    log_file.close()



for path, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.txt'):
            fname = (os.path.join(path, f))
            remove_line_containing_str(fname)



