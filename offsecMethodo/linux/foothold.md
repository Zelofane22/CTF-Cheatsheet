## *update shell*
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
script /dev/null -c bash
^Z
stty raw -echo; fg
reset 
screen
```

```
python -c 'import pty;pty.spawn("/bin/bash");'  
ctrl z  
echo $TERM  
stty -a  
stty raw -echo  
fg  

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH  
export TERM=xterm256-color  
export SHELL=bash  

stty rows \<> colums \<>  
```

## Automated script
```
linPEAS.sh
LinEnum.sh
linuxprivchecker.py
unix-privesc-check
Mestaploit: multi/recon/local_exploit_suggester

```
### GTFONow
https://github.com/Frissi0n/GTFONow
### lse
https://github.com/diego-treitos/linux-smart-enumeration
## _distrib info_
```
lsb_release -a
```

```
sudo -l
```
## _find SUID files_
```
find / -perm /4000 -type f -exec ls -ld {} \; 2>/dev/null

```
## _user's files_
```
find / -user admin -exec ls -ld {} \; 2>/dev/null | grep -v '^/run\|^/proc\|^/sys'
```
## _users_ (display lines finished by sh)
```
cat /etc/passwd | grep sh$

```
## _ExploitCapability_
```
getcap -r / 2>/dev/null
```
## *con.d*
```
ls -la /etc/cron.d

```
## _search ps log_
```
./pspy
```
## Proxy_chain
redirect the request to my machine
```
export http_proxy=http://adresse_du_proxy:port_du_proxy
```
