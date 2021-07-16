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

1. Enter your portal URL in `loginauto.py`.
2. Use the Inspect Element feature of your browser to find the name of your ID for each textbox ie. Username and password
3. Execute the python file to check if its working or not. Also, change the hour value in the _if_ condition of main(). It is to specify program when not to execute.
4. In your terminal go to `~/.config/autostart`. If you don't have the folder called autostart then create one using `sudo mkdir <name>`
5. In the path `~/.config/autostart` create a file called `loginscript.desktop` 
6. Paste the following code in it. You can open the file using `sudo gedit <filename>`
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
