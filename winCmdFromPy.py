import subprocess

# this function runs a windows command (cmd), printing the results
def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print repr(line)
    if errcode is not None:
        raise Exception('cmd %s, failed, see above for details', cmd)
    
    return result

process_list = open("processList.txt", "r")

locations = []
for process_name in process_list:
    print "getting location for " + process_name
    new_locations = run_win_cmd('''wmic process where 'name="'''+process_name.strip()+'''"' get ExecutablePath''')
    
    for line in new_locations:
        locations.append(line)

print type(locations)

path_list = open("pathList.txt", "w+")

for line in locations:
    if line.strip() and not "ExecutablePath" in line:
        path_list.write(line.strip() + "\n")