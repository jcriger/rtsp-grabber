# Hints
This file just contains some useful hints for working with a Raspberry Pi

## Terminal
Want to use the handy Terminal, just press __ctrl + alt + t__ to open it.

### Terminal Lingo
__sudo__: Run a command as the admin. Just type sudo in front of your command and it will be run with elevated privileges. Some commands like installing software updates require this.

__CTRL + C__: Cancel whatever command is currently running.

## Software Updates
Apply system updates by running:
```sh
sudo apt update && sudo apt upgrade -y
```
"sudo apt update" gets the list of pending updates. "sudo apt upgrade" downloads and installs them.

The __&&__ just combines the two commands. Why wait around to run a seconds comamnd when you can just run both together?

The __-y__ after "sudo apt upgrade" says yes to the prompt asking you if you want to install updates.

## Disable Logging
This one is kind of controversial. 

One of the problems with microSD cards is they wear out relatively quickly. If you want to increase the lifespan of you microSD card you can disable some of the data the operating system logs to it. 

If you think the hints in this file are useful, you can probably disable this because you likely won't be looking at these logs anyways.

Run the following commands to disable the system logging service: 
```sh
sudo systemctl stop rsyslog
sudo systemctl disable rsyslog
```