# gameMode

[![Join the chat at https://gitter.im/game-mode/Lobby](https://badges.gitter.im/game-mode/Lobby.svg)](https://gitter.im/game-mode/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

The intention of this project is to stop or start multiple processes with a single click. 

When gaming, it is desireable to have as many computing resources available as possible;
in other words, have as few other processes running aside from the game as possible.

This project will allow the user to create a list of programs which they want to run under
non-gaming use scenerios, but not during gaming. When beginning a gaming session, the user
can click a button to have all of the listed processes stopped. When the gaming session is
complete, the user will again click the button, restarting the processes which were stopped.

## Useful development links

#### `wmic` find file path of running process
  * https://superuser.com/questions/768984/show-exe-file-path-of-running-processes-on-the-command-line-in-windows
  
#### `taskkill` kill processes from command line
  * https://technet.microsoft.com/en-us/library/bb491009.aspx
  * http://tweaks.com/windows/39559/kill-processes-from-command-prompt/
  * https://superuser.com/questions/727724/close-programs-from-the-command-line-windows
  
#### `tasklist` list running processes from command line
  * https://commandwindows.com/tasklist.htm

#### running windows shell commands from python
  * https://stackoverflow.com/questions/14894993/running-windows-shell-commands-with-python
  * https://docs.python.org/2/library/subprocess.html
