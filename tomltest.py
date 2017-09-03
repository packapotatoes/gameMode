import toml

from run_win_cmd import *
def addpath( config, app, path):
    config[app]["path"] = path
    
def printdict( dict ):
    for key, value in dict.iteritems():
        print(key)
        print(value)

with open("config.toml") as conffile:
    config = toml.loads(conffile.read())
    
steampath = run_win_cmd('''wmic process where 'name="Steam.exe"' get ExecutablePath''')[1].strip()



print(repr(steampath))
    
if steampath != '':
    addpath( config, "steam", steampath)
    
printdict(config)

run_win_cmd_no_result('"' + steampath + '" -shutdown')

newconffile = open("newconfig.toml", 'w+')
toml.dump(config, newconffile)