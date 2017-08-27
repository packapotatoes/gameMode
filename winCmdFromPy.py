import subprocess
import time

# this function runs a windows command (cmd), printing the results
def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    
   # print type(process)
   # print type(process.stdout)
   # print ''
    #if process.stdout is not []:
    for line in process.stdout:
        #print line
        result.append(line)
    errcode = process.returncode

    if errcode is not None:
        raise Exception('cmd %s, failed, see above for details', cmd)
    
    return result

def run_win_cmd_no_result(cmd):
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
                               
    errcode = process.returncode
    if errcode is not None:
        raise Exception('cmd %s, failed, see above for details', cmd)
    
process_list = open("processList.txt", "r")

paths = []
for process_name in process_list:
    print "getting location for " + process_name
    new_paths = run_win_cmd('''wmic process where 'name="'''+process_name.strip()+'''"' get ExecutablePath''')
    
    #if new_paths is not []:
    for line in new_paths:
        paths.append(line)
         
    print "closing '" + process_name.strip() + "'"
    run_win_cmd_no_result('taskkill /IM '+process_name.strip()+'')
        #print "killed first time...waiting"
        #time.sleep(5)
        #run_win_cmd_no_result('taskkill /t /IM '+process_name.strip()+'')
        #print "killed second time"
    #else:
    #    print "'" + process_name + "' is not running"
    
    #print result
    

process_list.close()

# open file to save path list to, creating file if non-existant
path_list = open("pathList.txt", "w+")

# converting to a set removes duplicates but does not preserve order
paths = set(paths)

for line in paths:
    if line.strip() and not "ExecutablePath" in line:
        path_list.write(line.strip() + "\n")

path_list.close()
time.sleep(10)

path_list = open("pathList.txt", "r")

for path in path_list:
    print "starting '" + path.strip() + "'"
    run_win_cmd_no_result(path.strip()+'')
    #print result
        
path_list.close()