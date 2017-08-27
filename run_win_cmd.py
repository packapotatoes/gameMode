import subprocess

# this function runs a windows command (cmd), printing the results
def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    
    # does this deal with empty results?
    for line in process.stdout:
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