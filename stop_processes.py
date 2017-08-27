from run_win_cmd import *

process_list = open("processList.txt", "r")

paths = []
for process_name in process_list:
    print "getting location for " + process_name
    new_paths = run_win_cmd('''wmic process where 'name="'''
                             + process_name.strip() +
                            '''"' get ExecutablePath''')
    
    #if new_paths is not []:
    for line in new_paths:
        if line not in paths:
            paths.append(line)
         
    print "closing '" + process_name.strip() + "'"
    run_win_cmd_no_result('taskkill /t /f /IM ' + process_name.strip() + '')

process_list.close()

### Save paths

# open file to save path list to, creating file if non-existant
path_list = open("pathList.txt", "w+")

# converting to a set removes duplicates but does not preserve order
#paths = set(paths)

for line in paths:
    if line.strip() and not "ExecutablePath" in line:
        path_list.write(line.strip() + "\n")

path_list.close()