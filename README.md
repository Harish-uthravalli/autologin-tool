# autologin-tool

There are always these days when you just don't feel like waking up for work and logging into your system. This tool is specifically for those who have a online login portal which records the employees login details such as the login time. 
The tool does the followiong when provided with the right information.
1. Executes when PC starts
2. Logs into your portal automatically

#Pre-requisite packages
NOTE: This tool is only for Ubuntu and also only for those portals that are hosted online.
1. Python
2. Selenium  `pip install selenium`

# How to use the tool

1. Enter your portal URL in the `loginauto.py` code with the Login Credentials 
2. Execute the python file to check if its working or not. Also, change the hour value in the _if_ condition of main(). It is to specify program when not to execute.
3. In your terminal go to `~/.config/autostart`. If you don't have the folder called autostart then create one using `sudo mkdir <name>`
4. In the path `~/.config/autostart` create a file called `loginscript.desktop` 
5. Paste the following code in it. You can open the file using `gedit <filename>`
```
[Desktop Entry]
Encoding=UTF-8
Name=MyScript
Comment=MyScript
Icon=gnome-info
Exec=python <your loginauto.py path>
Terminal=false
Type=Application
Categories=

X-GNOME-Autostart-enabled=true
X-GNOME-Autostart-Delay=0
```
