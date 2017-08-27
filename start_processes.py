from run_win_cmd import *

path_list = open("pathList.txt", "r")

for path in path_list:
    print "starting '" + path.strip() + "'"
    run_win_cmd_no_result(path.strip()+'')
    #print result
        
path_list.close()